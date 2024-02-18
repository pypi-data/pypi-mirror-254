import enum
import logging

from looqbox.config.config_reader import ConfigReader


class LogLevel(enum.Enum):
    DEBUG = logging.DEBUG
    INFO = logging.INFO
    WARNING = logging.WARNING
    ERROR = logging.ERROR

    @classmethod
    def from_str(cls, level: str):
        return cls[level.upper()]


class Logger:
    configReader = ConfigReader()
    configReader.set_path_from_root("resources/application-config.ini")
    log_level: LogLevel = LogLevel.from_str(configReader.read("DEFAULT", "LOG_LEVEL", default="INFO"))

    logging.basicConfig(level=log_level.value)

    @classmethod
    def get_logger(cls, name) -> logging.Logger:
        return logging.getLogger(name)

    @classmethod
    def get_log_level(cls) -> LogLevel:
        return cls.log_level
