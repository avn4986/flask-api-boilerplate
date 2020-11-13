from os import getenv

from utils.path_utils import get_base_path


class Constants(object):
    EMPTY = ''
    RUN_PORT = int(getenv('PORT', '4000'))
    RUN_ENVIRONMENT = getenv('RUN_ENVIRONMENT', '')
    LOGGER_PROPERTIES_SECTION = f"{RUN_ENVIRONMENT + '_' if RUN_ENVIRONMENT is not EMPTY else EMPTY}logger"
    X_REQUEST_ID = 'X-Request-Id'
    X_FORWARDED_FOR = 'X-Forwarded-For'
    REQUEST_START_TIMESTAMP = 'request_start_timestamp'
    BASE_PATH = get_base_path()
    CONFIG_FOLDER_PATH = f"{get_base_path()}/config"
    CONFIG_FILE_PATH = f'{CONFIG_FOLDER_PATH}/config.ini'

    def __setattr__(self, *_):
        pass


Constants = Constants()
