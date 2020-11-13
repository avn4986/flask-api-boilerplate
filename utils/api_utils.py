import datetime
from datetime import datetime
from uuid import uuid4

import flask

from commons.constants import Constants


class APIUtils:
    @staticmethod
    def request_id():
        if APIUtils.__has_request_context():
            if getattr(flask.request, Constants.X_REQUEST_ID, None):
                return flask.request.request_id
            original_request_id = flask.request.headers.get(Constants.X_REQUEST_ID)
            # Set to globals for flask request
            flask.request.request_id = APIUtils.__generate_request_id(original_request_id)
            return flask.request.request_id
        return Constants.EMPTY

    @staticmethod
    def ip_address():
        if APIUtils.__has_request_context():
            user_ip = Constants.EMPTY
            if Constants.X_FORWARDED_FOR in flask.request.headers:
                proxy_data = flask.request.headers[Constants.X_FORWARDED_FOR]
                user_ip = proxy_data.split(',')[0]
            return user_ip if user_ip is not None and user_ip is not '' else flask.request.remote_addr
        return Constants.EMPTY

    @staticmethod
    def request_uri():
        if APIUtils.__has_request_context():
            return flask.request.path
        return Constants.EMPTY

    @staticmethod
    def method():
        if APIUtils.__has_request_context():
            return flask.request.method
        return Constants.EMPTY

    @staticmethod
    def query_params():
        if APIUtils.__has_request_context():
            return flask.request.query_string.decode("utf-8")
        return Constants.EMPTY

    @staticmethod
    def duration():
        if APIUtils.__has_request_context():
            if getattr(flask.request, Constants.REQUEST_START_TIMESTAMP, None):
                milliseconds_since_epoch = datetime.now().timestamp() * 1000
                return milliseconds_since_epoch - flask.request.request_start_timestamp
        return -1

    @staticmethod
    def __has_request_context():
        return flask.has_request_context()

    @staticmethod
    def __generate_request_id(original_id):
        if original_id is None or original_id is Constants.EMPTY:
            return str(uuid4())
        return original_id
