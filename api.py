# -*- coding: utf-8 -*-
from flask import Flask, jsonify

from commons.api_exception import APIException, ErrorDefinitions

app = Flask(__name__)


@app.errorhandler(Exception)
def error_handler(error):
    if isinstance(error, APIException):
        response, status = error.get_error_response()
    else:
        response, status = APIException.get_default_response()
    return jsonify(response), status


@app.route('/success', methods=['GET'])
def success_sample():
    response, status = {'message': 'hello-word'}, 200
    return jsonify(response), status


@app.route('/failure', methods=['GET'])
def failure_sample():
    raise APIException(ErrorDefinitions.INTERNAL_SERVER_ERROR)


if __name__ == '__main__':
    app.run()
