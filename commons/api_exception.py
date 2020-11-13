# -*- coding: utf-8 -*-
from commons.error_definitions import ErrorDefinitions


class APIException(Exception):
    error_message: str = None

    def __init__(self, error=ErrorDefinitions.INTERNAL_SERVER_ERROR, error_message: str = None, stack_trace=None):
        self.error = error
        self.stack_trace = stack_trace
        self.error_message = error_message if error_message is not None else self.error.error_message

    def get_error_response(self):
        return {
                   'error-code': self.error.error_code,
                   'error-message': self.error_message,
                   'stack-trace': self.stack_trace
               }, self.error.http_status

    @staticmethod
    def get_default_response():
        return APIException(error=ErrorDefinitions.INTERNAL_SERVER_ERROR).get_error_response()
