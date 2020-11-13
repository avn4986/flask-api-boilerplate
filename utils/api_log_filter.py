import logging

from utils.api_utils import APIUtils


class APILogFilter(logging.Filter):
    def filter(self, record):
        record.ip = APIUtils.ip_address()
        record.rid = APIUtils.request_id()
        return True
