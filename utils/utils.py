import logging
from configparser import SafeConfigParser
from logging import Formatter
from logging.handlers import RotatingFileHandler
from os import getenv, environ

from flask import Flask

from commons.constants import Constants
from utils.api_log_filter import APILogFilter
from utils.path_utils import mkdir_safe

config = SafeConfigParser()
config.read(Constants.CONFIG_FILE_PATH)

# Update Environment
environ['TZ'] = config.get('global', 'timezone')

# Setup Log Details
log_folder = config.get(Constants.LOGGER_PROPERTIES_SECTION, 'location')
log_folder = log_folder if log_folder is not None and log_folder is not '' \
    else getenv('LOGGING_LOCATION', f"{Constants.BASE_PATH}/logs")
mkdir_safe(log_folder)
log_file = config.get(Constants.LOGGER_PROPERTIES_SECTION, 'file_name')
log_file = log_file if log_folder is not None and log_folder is not '' else 'api.log'

log_file_max_size = config.getint(Constants.LOGGER_PROPERTIES_SECTION, 'max_file_size')
max_files = config.getint(Constants.LOGGER_PROPERTIES_SECTION, 'max_files')

# Disable Logger in Flask
logging.getLogger('werkzeug').disabled = True

# Setup formatter for log file
formatter = Formatter(config.get(Constants.LOGGER_PROPERTIES_SECTION, 'pattern'))

# Setup console handler
console_handler = logging.StreamHandler()
console_handler.setFormatter(formatter)

# Setup File handler
file_handler = RotatingFileHandler(filename=f"{log_folder}/{log_file}", maxBytes=log_file_max_size,
                                   backupCount=max_files)
file_handler.setFormatter(formatter)

# Global logging configuration
logging.basicConfig(
    level=logging.DEBUG,
    format=config.get(Constants.LOGGER_PROPERTIES_SECTION, 'pattern'),
    datefmt=config.get(Constants.LOGGER_PROPERTIES_SECTION, 'date_format'),
)

# Custom Filters
api_log_filter = APILogFilter()


class Utils:
    @staticmethod
    def logger(name: str) -> logging.Logger:
        logger = logging.getLogger(name)
        logger.propagate = False
        # If the handlers are not available, only then add them
        if not logger.handlers:
            logger.addHandler(console_handler)
            logger.addHandler(file_handler)
        if not logger.filters:
            logger.addFilter(api_log_filter)
        return logger

    @staticmethod
    def create_flask_app(name: str) -> Flask:
        app = Flask(name)
        app.logger.addFilter(api_log_filter)
        return app
