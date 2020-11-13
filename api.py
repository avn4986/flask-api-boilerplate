# -*- coding: utf-8 -*-
from datetime import datetime

from flask import request

from commons.api_exception import APIException, ErrorDefinitions
from commons.constants import Constants
from commons.response_obj import ResponseObj
from utils.api_utils import APIUtils
from utils.utils import Utils

app = Utils.create_flask_app(__name__)
log = Utils.logger(__name__)


@app.before_request
def before_request_func():
    request.request_start_timestamp = datetime.now().timestamp() * 1000


@app.after_request
def after_request_func(response):
    log.info(
        f'method="{APIUtils.method()}" uri="{APIUtils.request_uri()}" query="{APIUtils.query_params()}" '
        f'duration={APIUtils.duration():.2f}ms status={response.status}')
    return response


@app.errorhandler(Exception)
def error_handler(error):
    user_error: APIException
    if isinstance(error, APIException):
        user_error = error
    else:
        log.error("Failed to execute request", exc_info=error)
        user_error = APIException()
    return ResponseObj.make_response(data=None, status=user_error.error.http_status, error=user_error)


@app.route('/success', methods=['GET'])
def success_sample():
    response, status = {'message': 'hello-word'}, 200
    return ResponseObj.make_response(data=response, status=status)


@app.route('/failure', methods=['GET'])
def failure_sample():
    raise APIException(ErrorDefinitions.INTERNAL_SERVER_ERROR)


if __name__ == '__main__':
    log.info('Starting API..')
    app.run(port=Constants.RUN_PORT)
