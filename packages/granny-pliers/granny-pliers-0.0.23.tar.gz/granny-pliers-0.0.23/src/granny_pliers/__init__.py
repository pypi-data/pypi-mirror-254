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

"""Granny Pliers is a Python library that contains a collection of useful
and helpful tools, designed to simplify developers' lives."""

__version__ = "0.0.23"
__author__ = "Dmytro Stepanenko"
__copyright__ = "Copyright 2022, Dmytro Stepanenko, Granny Pliers"
__credits__ = ["Dmytro Stepanenko"]
__license__ = "Apache License Version 2.0"
__email__ = "dmitrijstepanenko@gmail.com"


from .config import *
from .logger import *
from .worker import *

__all__ = logger.__all__ + config.__all__ + worker.__all__
