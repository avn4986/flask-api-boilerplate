import json

from flask import Response

from commons.api_exception import APIException
from utils.api_utils import APIUtils


class ResponseObj(object):
    def __init__(self, data=None, error: APIException = None):
        self.data = data
        if error is not None:
            self.error_desc = error.error_message
            self.error_code = error.error.error_code
        else:
            self.error_desc = None
            self.error_code = None
        self.duration = int(APIUtils.duration())
        self.request_id = APIUtils.request_id()

    @staticmethod
    def make_response(data, status, error=None, mime_type: str = 'application/json'):
        response = ResponseObj(data, error)
        return Response(json.dumps(response, default=lambda o: o.__dict__), status=status, mimetype=mime_type)
