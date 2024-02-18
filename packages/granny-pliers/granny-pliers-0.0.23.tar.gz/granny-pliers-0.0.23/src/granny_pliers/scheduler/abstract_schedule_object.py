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

"""AbstractScheduleObject"""

__all__ = ["AbstractScheduleObject"]
from dataclasses import dataclass

from granny_pliers.orm import AbstractModel
from .time_table import TimeTable


@dataclass(repr=False, eq=False)
class AbstractScheduleObject(AbstractModel):
    """AbstractScheduleObject"""

    enabled: bool = True
    time_table: TimeTable = None

    name: str = "unknown"

    def __post_init__(self):
        super().__post_init__()

        if isinstance(self.time_table, dict):
            self.time_table = TimeTable(**self.time_table)
