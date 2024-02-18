#  Copyright 2022 Dmytro Stepanenko, Granny Pliers
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.

"""Abstract db based scheduler"""

__all__ = ["AbstractScheduler", "AbstractSingleTaskScheduler", "AbstractDataBaseScheduler"]
import abc
import asyncio
from abc import ABC
from datetime import timedelta
from typing import Dict

from pymongo.errors import PyMongoError

from granny_pliers.logger import AbstractLogger
from granny_pliers.orm import AbstractMongoRepository
from .abstract_schedule_object import AbstractScheduleObject


class AbstractScheduler(AbstractLogger):
    """AbstractScheduler"""

    TOLERANCE = timedelta(seconds=5)
    FMT = "%Y-%m-%d %H:%M:%S"

    @abc.abstractmethod
    async def run(self):
        """Launch scheduler"""

    @abc.abstractmethod
    async def execute_job(self, job: AbstractScheduleObject):
        """Execute job"""

    @abc.abstractmethod
    async def schedule(self, job: AbstractScheduleObject):
        """Submit task in event loop"""


class AbstractSingleTaskScheduler(AbstractScheduler):
    """AbstractSingleTaskScheduler"""

    @property
    @abc.abstractmethod
    def job(self) -> AbstractScheduleObject:
        """Define your job here"""

    async def run(self):
        self.log.info("Starting single task scheduler %s...", self.__class__.__name__)
        asyncio.create_task(self.schedule(self.job))

    async def schedule(self, job: AbstractScheduleObject):
        self.log.info("Scheduling single job: %s", job.name)
        try:
            sleep_until_next_run = job.time_table.get_wait_until_next_run_sec()

            self.log.info(
                "Run job: %s at: %s, Wait: %s, Next run at: %s",
                job.name,
                job.time_table.run_at().strftime(self.FMT),
                str(timedelta(seconds=sleep_until_next_run)),
                job.time_table.next_run_at().strftime(self.FMT),
            )

            await asyncio.sleep(sleep_until_next_run)
            self.log.info("RUN job: %s", job.name)
            await self.execute_job(job)
            self.log.info("Rescheduling job: %s", job.name)
            asyncio.create_task(self.schedule(job))

        except asyncio.CancelledError:
            self.log.info("Schedule job: %s is stopped", job.name)


class AbstractDataBaseScheduler(AbstractScheduler, ABC):
    """AbstractDataBaseScheduler"""

    def __init__(self, repository: AbstractMongoRepository, watch=False):
        super().__init__()
        self._tasks: Dict[str, asyncio.Task] = dict()
        self._repository = repository
        self._watch = watch

    @property
    def pipeline(self):
        return None

    async def run(self):
        self.log.info("Starting scheduler %s...", self.__class__.__name__)

        jobs = await self._repository.find_many(dict(enabled=True))

        for job in jobs:
            task = self._tasks.get(str(job.id), None)
            if task is None:
                self._tasks[str(job.id)] = asyncio.create_task(self.schedule(job))

        if self._watch:
            asyncio.create_task(self.watcher())

    async def schedule(self, job: AbstractScheduleObject):
        self.log.info("Scheduling job: %s", job.name)
        try:
            # Update job status
            updated_job = await self._repository.find_by_id(job.id)

            if updated_job is None:
                self.log.info("Schedule object: %s is deleted, stop scheduler", job.name)
                return

            if not updated_job.enabled:
                self.log.info("Schedule object: %s is disabled, stop scheduler", job.name)
                return

            sleep_until_next_run = updated_job.time_table.get_wait_until_next_run_sec()

            self.log.info(
                "Run job: %s at: %s, Wait: %s, Next run at: %s",
                updated_job.name,
                updated_job.time_table.run_at().strftime(self.FMT),
                str(timedelta(seconds=sleep_until_next_run)),
                updated_job.time_table.next_run_at().strftime(self.FMT),
            )

            await asyncio.sleep(sleep_until_next_run)
            self.log.info("RUN job: %s", updated_job.name)
            await self.execute_job(updated_job)
            self.log.info("Rescheduling job: %s", updated_job.name)
            self._tasks[str(updated_job.id)] = asyncio.create_task(self.schedule(updated_job))

        except asyncio.CancelledError:
            self.log.info("Schedule job: %s is stopped", job.name)

    async def watcher(self):
        self.log.info("Starting %s watcher...", self._repository.collection_name)
        try:
            async with self._repository.collection.watch(pipeline=self.pipeline) as stream:
                async for change in stream:
                    operation = change.get("operationType")
                    doc = change.get("fullDocument", {})

                    if operation == "insert":
                        await self.on_watcher_insert(doc)
                    elif operation == "update":
                        await self.on_watcher_update(doc)
                    elif operation == "replace":
                        await self.on_watcher_replace(doc)
                    elif operation == "delete":
                        await self.on_watcher_delete(doc)

        except PyMongoError as error:
            self.log.error("ChangeStream error", error=error)

    async def on_watcher_insert(self, job: dict):
        job_id = job.get("_id", "")
        self.log.info("Inserting scheduler %s...", job_id)
        new_job = await self._repository.find_by_id(job_id)
        if new_job is None:
            return

        self._tasks[str(new_job.id)] = asyncio.create_task(self.schedule(new_job))

    async def on_watcher_update(self, job: dict):
        job_id = job.get("_id", "")
        self.log.info("Updating scheduler %s...", job_id)
        updated_job = await self._repository.find_by_id(job_id)
        if updated_job is None:
            return

        active_task = self._tasks.get(str(updated_job.id), None)
        if active_task is not None:
            active_task.cancel()

        self._tasks[str(updated_job.id)] = asyncio.create_task(self.schedule(updated_job))

    async def on_watcher_replace(self, job: dict):
        await self.on_watcher_update(job)

    async def on_watcher_delete(self, job: dict):
        job_id = job.get("_id", "")
        self.log.info("Deleting scheduler %s...", job_id)
        active_task = self._tasks.get(job_id, None)
        if active_task is not None:
            active_task.cancel()
            del self._tasks[job_id]
