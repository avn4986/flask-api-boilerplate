# -*- coding: utf-8 -*-
from enum import Enum


class ErrorDefinitions(Enum):
    INTERNAL_SERVER_ERROR = (1000, 'Internal server occurred, please contact support team.', 500)

    def __init__(self, error_code, error_message, http_status):
        self._err_code = error_code
        self._err_msg = error_message
        self._err_http_status = http_status

    @property
    def error_code(self):
        return 'API-ERR-{}'.format(self._err_code)

    @property
    def error_message(self):
        return self._err_msg

    @property
    def http_status(self):
        return self._err_http_status
