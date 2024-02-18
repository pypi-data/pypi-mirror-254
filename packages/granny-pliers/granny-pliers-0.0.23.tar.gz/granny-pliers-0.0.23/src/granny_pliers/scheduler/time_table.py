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

"""Scheduling TimeTable"""

__all__ = ["TimePeriod", "TimeTable"]
import calendar
from dataclasses import dataclass, field
from datetime import datetime, timedelta
from enum import IntEnum
from zoneinfo import ZoneInfo

from granny_pliers.orm import BaseModel


class TimePeriod(IntEnum):
    """TimePeriod"""

    EVERY_MINUTE = 0
    EVERY_HOUR = 1
    EVERY_DAY = 2
    EVERY_WEEK = 3
    EVERY_MONTH = 5
    EVERY_YEAR = 6


@dataclass(repr=False, eq=False)
class TimeTable(BaseModel):
    """TimeTable"""

    second: int = 0
    minute: int = 0
    hour: int = 0
    day_of_week: int = 0
    day_of_month: int = 0
    month: int = 0
    timezone: str = "Europe/Berlin"
    tolerance_sec: int = 5
    weekend: list[int] = field(default_factory=list)

    def __post_init__(self):
        if len(self.weekend) == 0:
            self.weekend = [6, 7]

    def period(self) -> TimePeriod:
        """Get execute period"""

        if self.month > 0:
            return TimePeriod.EVERY_YEAR

        if self.day_of_month > 0:
            return TimePeriod.EVERY_MONTH

        if self.day_of_week > 0:
            return TimePeriod.EVERY_WEEK

        if self.hour > 0:
            return TimePeriod.EVERY_DAY

        if self.minute > 0:
            return TimePeriod.EVERY_HOUR

        if self.second > 0:
            return TimePeriod.EVERY_MINUTE

        return TimePeriod.EVERY_YEAR

    def run_at(self, period: TimePeriod = None) -> datetime:
        """Get exact execution time"""
        if period is None:
            period = self.period()
        now = datetime.now().replace(microsecond=0).astimezone(ZoneInfo(self.timezone))

        if period == TimePeriod.EVERY_YEAR:
            return now.replace(
                month=self.month,
                day=max(1, self.day_of_month),
                hour=self.hour,
                minute=self.minute,
                second=self.second,
            )

        if period == TimePeriod.EVERY_MONTH:
            return now.replace(
                day=self.day_of_month,
                hour=self.hour,
                minute=self.minute,
                second=self.second,
            )

        if period == TimePeriod.EVERY_WEEK:
            days_delta = timedelta(days=self.day_of_week - now.isoweekday())
            return now.replace(hour=self.hour, minute=self.minute, second=self.second) + days_delta

        if period == TimePeriod.EVERY_DAY:
            return now.replace(hour=self.hour, minute=self.minute, second=self.second)

        if period == TimePeriod.EVERY_HOUR:
            return now.replace(minute=self.minute, second=self.second)

        if period == TimePeriod.EVERY_MINUTE:
            return now.replace(second=self.second)

        return now

    def next_run_at(self, period: TimePeriod = None, run_at: datetime = None) -> datetime:
        """Get exact next execution time"""
        if period is None:
            period = self.period()
        if run_at is None:
            run_at = self.run_at()

        if period == TimePeriod.EVERY_YEAR:
            return run_at.replace(year=run_at.year + 1)

        if period == TimePeriod.EVERY_MONTH:
            days_in_month = calendar.monthrange(run_at.year, run_at.month)[1]
            return run_at + timedelta(days=days_in_month)

        if period == TimePeriod.EVERY_WEEK:
            return run_at + timedelta(days=7)

        if period == TimePeriod.EVERY_DAY:
            return run_at + timedelta(days=1)

        if period == TimePeriod.EVERY_HOUR:
            return run_at + timedelta(hours=1)

        # if period == TimePeriod.EVERY_MINUTE:
        return run_at + timedelta(minutes=1)

    def get_wait_until_next_run_sec(self) -> int:
        """Get delay until next run"""
        period = self.period()
        run_at = self.run_at(period)
        next_run_at = self.next_run_at(period, run_at)
        tolerance = timedelta(seconds=self.tolerance_sec)
        now = datetime.now().replace(microsecond=0).astimezone(ZoneInfo(self.timezone))
        if run_at < now - tolerance:
            wait_until_next_run = next_run_at - now
        elif run_at > now + tolerance:
            wait_until_next_run = run_at - now
        else:
            wait_until_next_run = next_run_at - now
        return round(wait_until_next_run.total_seconds())
