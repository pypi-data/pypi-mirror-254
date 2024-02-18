import threading
import time
import uuid

from fastapi import Request

from convergence.constants import (HEADER_REQUEST_ID,
                                   HEADER_PARENT_REQUEST_ID,
                                   HEADER_CALLER_SERVICE,
                                   HEADER_CALLER_SERVICE_VERSION,
                                   HEADER_CALLER_SERVICE_HASH)


class RequestLog:
    def __init__(self):
        self.request_identifier = ''
        self.parent_request_identifier = ''
        self.caller_service = ''
        self.receiver_service = ''
        self.start_timestamp = 0
        self.end_timestamp = 0
        self.headers = {}
        self.url = ''
        self.parameters = []
        self.log_entries = []
        self.response = None

    @staticmethod
    def initialize(request_type, http_request: Request, service, *parameters):
        result = RequestLog()

        result.start_timestamp = int(time.time() * 1000)
        result.headers = RequestLog.__load_request_headers(http_request)
        result.request_identifier, result.parent_request_identifier = RequestLog.__get_request_ids(http_request,
                                                                                                   request_type)
        result.caller_service = RequestLog.__load_caller_service(result.headers)
        result.receiver_service = RequestLog.__load_current_service(service)
        result.url = RequestLog.__get_request_uri(http_request)
        result.parameters = parameters

        RequestLog.__remove_header(result.headers, HEADER_REQUEST_ID)
        RequestLog.__remove_header(result.headers, HEADER_PARENT_REQUEST_ID)
        RequestLog.__remove_header(result.headers, HEADER_CALLER_SERVICE)
        RequestLog.__remove_header(result.headers, HEADER_CALLER_SERVICE_VERSION)
        RequestLog.__remove_header(result.headers, HEADER_CALLER_SERVICE_HASH)
        RequestLog.__remove_jwt_signature_for_logging(result.headers)

        return result

    def finish(self, response):
        self.response = response
        self.end_timestamp = int(time.time() * 1000)

    def info(self, message, *args, **kwargs):
        self.__add_log_entry('info', message, *args, **kwargs)

    def error(self, message, *args, **kwargs):
        self.__add_log_entry('error', message, *args, **kwargs)

    def warning(self, message, *args, **kwargs):
        self.__add_log_entry('warning', message, *args, **kwargs)

    def debug(self, message, *args, **kwargs):
        self.__add_log_entry('debug', message, *args, **kwargs)

    def exception(self, ex, trace_back):
        entry = LogEntry()
        entry.timestamp = int(time.time() * 1000)
        entry.level = 'exception'
        entry.message = str(ex)
        entry.arguments = None
        entry.named_arguments = {
            'format': 'python: trace_back',
            'stack_trace': trace_back
        }
        entry.type = "exception_entry"
        entry.thread_id = threading.current_thread().native_id

        self.log_entries.append(entry)

    def __add_log_entry(self, level, message, *args, **kwargs):
        entry = LogEntry()
        entry.timestamp = int(time.time() * 1000)
        entry.level = level
        entry.message = message
        entry.arguments = args
        entry.named_arguments = kwargs
        entry.type = "log_entry"
        entry.thread_id = threading.current_thread().native_id

        self.log_entries.append(entry)

    @classmethod
    def __load_request_headers(cls, http_request: Request):
        names = http_request.headers.keys()
        return {header: http_request.headers[header] for header in names}

    @classmethod
    def __load_caller_service(cls, headers):
        result = LogEntryServiceInfo()

        result.name = headers.get(HEADER_CALLER_SERVICE.lower())
        result.version = headers.get(HEADER_CALLER_SERVICE_VERSION.lower())
        result.hash = headers.get(HEADER_CALLER_SERVICE_HASH.lower())

        return result

    @classmethod
    def __load_current_service(cls, service):
        result = LogEntryServiceInfo()

        info = service.get_service_info()
        result.name = info.SERVICE_NAME
        result.version = info.SERVICE_VERSION
        result.hash = info.SERVICE_VERSION_HASH

        return result

    @classmethod
    def __get_request_uri(cls, http_request: Request):
        url = http_request.url.path[len(http_request.base_url.path):]
        if not url.startswith('/'):
            url = '/' + url

        return url

    @staticmethod
    def __get_request_ids(http_request, request_type):
        request_id = http_request.headers.get(HEADER_REQUEST_ID)
        if request_id is None:
            request_id = str(uuid.uuid4())

        request_id = request_type.lower() + '_' + request_id

        parent_request_id = http_request.headers.get(HEADER_PARENT_REQUEST_ID)

        return request_id, parent_request_id

    @classmethod
    def __remove_header(cls, headers, header):
        if header in headers:
            headers.pop(header)

        if header.lower() in headers:
            headers.pop(header.lower())

    @classmethod
    def __remove_jwt_signature_for_logging(cls, headers):
        header = None
        if 'authorization' in headers:
            header = 'authorization'
        if 'Authorization' in headers:
            header = 'Authorization'

        if header is not None:
            value = headers[header]
            if '.' in value:
                value = value[0:value.rindex('.') + 1] + '***********'
            headers[header] = value


class LogEntryServiceInfo:
    def __init__(self):
        self.name = ''
        self.version = ''
        self.hash = ''


class LogEntry:
    def __init__(self):
        self.timestamp = 0
        self.level = ''
        self.message = ''
        self.type = ''
        self.arguments = None
        self.named_arguments = None
        self.thread_id = ''
