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

"""WEB"""

from .abstract_status_web_service import *
from .abstract_web_application import *
from .abstract_web_service import *
from .web_application_config import *

__all__ = (
    abstract_status_web_service.__all__
    + abstract_web_application.__all__
    + abstract_web_service.__all__
    + web_application_config.__all__
)
