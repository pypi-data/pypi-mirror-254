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

"""LoggerConfig"""
import logging
import sys
from dataclasses import dataclass, field
from logging import config

import structlog

from granny_pliers.logger import add_proc_name, add_logger_name
from .abstract_config import AbstractConfig
from .autowired_config import AutoWiredConfig
from .project_environment import ProjectEnvironment

__all__ = ["LoggerConfig"]


@dataclass()
class LoggerConfig(AbstractConfig):
    """LoggerConfig"""

    log_level: int = field(
        default=None,
        metadata={"env_var_name": "LOG_LEVEL", "type": str},
    )
    log_output_format: int = field(
        default="plain",
        metadata={"env_var_name": "LOG_OUTPUT_FORMAT", "type": str},
    )

    is_timestamp_enabled: bool = field(
        default=True,
        metadata={"type": bool},
    )
    is_process_name_enabled: bool = field(
        default=True,
        metadata={"type": bool},
    )

    is_logger_name_enabled: bool = field(
        default=True,
        metadata={"type": bool},
    )

    auto_wired: AutoWiredConfig = field(
        default=None,
        metadata={"type": AutoWiredConfig},
    )

    def get_log_level_from_env(self) -> int:
        """get_log_level_from_env"""
        return {
            ProjectEnvironment.LOCAL: logging.DEBUG,
            ProjectEnvironment.DEV: logging.DEBUG,
            ProjectEnvironment.STAGE: logging.DEBUG,
            ProjectEnvironment.TEST: logging.DEBUG,
            ProjectEnvironment.PROD: logging.INFO,
        }.get(self.auto_wired.environment, logging.INFO)

    def __post_init__(self):
        super().__post_init__()
        if self.auto_wired is None:
            self.auto_wired = AutoWiredConfig()

        if self.log_level is None:
            self.log_level = self.get_log_level_from_env()
        elif isinstance(self.log_level, str):
            self.log_level = {
                "CRITICAL": logging.CRITICAL,
                "FATAL": logging.FATAL,
                "ERROR": logging.ERROR,
                "WARN": logging.WARNING,
                "WARNING": logging.WARNING,
                "INFO": logging.INFO,
                "DEBUG": logging.DEBUG,
                "NOTSET": logging.NOTSET,
            }.get(self.log_level.upper(), logging.INFO)

    def setup(self):
        """Initialize and setup logger"""

        config.dictConfig(
            {
                "version": 1,
                "disable_existing_loggers": False,
                "loggers": {
                    "": {
                        "level": self.log_level,
                        "handlers": [self.auto_wired.environment],
                        "propagate": 1,
                    }
                },
                "handlers": {
                    ProjectEnvironment.LOCAL.value: {
                        "class": "logging.StreamHandler",
                        "formatter": ProjectEnvironment.LOCAL.value,
                        "stream": sys.stdout,
                    },
                    ProjectEnvironment.DEV.value: {
                        "class": "logging.StreamHandler",
                        "formatter": ProjectEnvironment.DEV.value,
                        "stream": sys.stdout,
                    },
                    ProjectEnvironment.STAGE.value: {
                        "class": "logging.StreamHandler",
                        "formatter": ProjectEnvironment.STAGE.value,
                        "stream": sys.stdout,
                    },
                    ProjectEnvironment.PROD.value: {
                        "class": "logging.StreamHandler",
                        "formatter": ProjectEnvironment.PROD.value,
                        "stream": sys.stdout,
                    },
                    ProjectEnvironment.TEST.value: {
                        "class": "logging.StreamHandler",
                        "formatter": ProjectEnvironment.TEST.value,
                        "stream": sys.stdout,
                    },
                },
                "formatters": {
                    ProjectEnvironment.LOCAL.value: {
                        "()": structlog.stdlib.ProcessorFormatter,
                        "processor": structlog.dev.ConsoleRenderer(pad_event=100, colors=True),
                    },
                    ProjectEnvironment.DEV.value: {
                        "()": structlog.stdlib.ProcessorFormatter,
                        "processor": structlog.dev.ConsoleRenderer(colors=False),
                    },
                    ProjectEnvironment.PROD.value: {
                        "()": structlog.stdlib.ProcessorFormatter,
                        "processor": structlog.dev.ConsoleRenderer(colors=False),
                    },
                    ProjectEnvironment.STAGE.value: {
                        "()": structlog.stdlib.ProcessorFormatter,
                        "processor": structlog.dev.ConsoleRenderer(colors=False),
                    },
                    ProjectEnvironment.TEST.value: {
                        "()": structlog.stdlib.ProcessorFormatter,
                        "processor": structlog.dev.ConsoleRenderer(colors=False),
                    },
                },
            }
        )
        log_processors = [
            structlog.stdlib.add_log_level,
            structlog.stdlib.PositionalArgumentsFormatter(),
        ]
        if self.is_timestamp_enabled:
            log_processors.append(structlog.processors.TimeStamper(fmt="iso"))

        if self.is_logger_name_enabled:
            log_processors.append(add_proc_name)

        if self.is_logger_name_enabled:
            log_processors.append(add_logger_name)

        if self.log_output_format == "json":
            log_processors.extend(
                [
                    structlog.processors.format_exc_info,
                    structlog.processors.UnicodeDecoder(),
                    structlog.processors.JSONRenderer(),
                ]
            )
        else:
            log_processors.extend(
                [
                    structlog.processors.StackInfoRenderer(),
                    structlog.processors.format_exc_info,
                    structlog.stdlib.ProcessorFormatter.wrap_for_formatter,
                ]
            )
        structlog.configure(
            processors=log_processors,
            context_class=dict,
            logger_factory=structlog.stdlib.LoggerFactory(),
            cache_logger_on_first_use=True,
        )
