from starlette.middleware.base import BaseHTTPMiddleware
from fastapi import Request
from starlette.responses import JSONResponse

from convergence.dto.bad_request_details import BadRequestDetails, BadFieldRequest
from convergence.dto.base_dto import ApiResponse
from convergence.helpers import errors
from convergence.helpers.controller_helpers import convert_object_to_dict, update_response_with_request_ids_for_filters
from convergence.internal.observability.request_log import RequestLog
from convergence.internal.observability.serializer_config import LogSerializerConfig
from convergence.constants import (HEADER_REQUEST_ID,
                                   HEADER_PARENT_REQUEST_ID,
                                   HEADER_CALLER_SERVICE,
                                   HEADER_CALLER_SERVICE_VERSION,
                                   HEADER_CALLER_SERVICE_HASH)


RESERVED_MANDATORY_GATEWAY_HEADERS = [
    HEADER_REQUEST_ID,
    HEADER_CALLER_SERVICE,
    HEADER_CALLER_SERVICE_HASH,
    HEADER_CALLER_SERVICE_VERSION,
]

RESERVED_OPTIONAL_GATEWAY_HEADERS = [
    HEADER_PARENT_REQUEST_ID
]


class GatewayHeaderValidationMiddleware(BaseHTTPMiddleware):
    def __init__(self, app, **kwargs):
        super().__init__(app)
        self.service = kwargs['service']
        self.is_behind_gateway = self.service.get_configuration('security.is_behind_gateway')
        self.log_serializer = LogSerializerConfig.create(self.service)

    async def dispatch(self, request: Request, call_next):
        if self.is_behind_gateway:
            # Behind gateway, no need to validate token
            is_missing, missing_headers = self.__is_missing_any_of_gateway_headers(request)
            if is_missing:
                response = self.__request_is_missing_gateway_headers(request, missing_headers)
            else:
                response = await call_next(request)
        elif len(self.__get_independent_service_request_invalid_headers(request)) > 0:
            # Independent service, but contains reserved headers, must fail
            response = self.__request_has_reserved_headers_response(request)
        elif self.__request_has_authorization_header(request):
            # Independent service, has authorization, so must be validated
            if self.__is_authorization_header_valid(request):
                response = await call_next(request)
            else:
                response = self.__unauthorized_response(request)
        else:
            # Independent service, no authorization, can proceed. If the endpoint need authorization, it will be
            # dropped by authorization filter
            response = await call_next(request)

        return response

    def __is_missing_any_of_gateway_headers(self, request):
        headers = request.headers.keys()
        headers = [header.upper() for header in headers]

        missing_headers = []
        for header in RESERVED_MANDATORY_GATEWAY_HEADERS:
            if header not in headers:
                missing_headers.append(header)

        return len(missing_headers) > 0, missing_headers

    def __request_is_missing_gateway_headers(self, http_request, missing_headers):
        request_type = self.service.get_configuration('observability.request_id_prefix')
        request_log = RequestLog.initialize(request_type, http_request, self.service)

        status_code = 502

        response = ApiResponse()
        response.header.status_code = status_code
        response.header.message = 'The request input was invalid, missing the mandatory API gateway headers.'
        response.header.code = errors.INVALID_DATA
        response.body = BadRequestDetails()
        response.header.body_type = response.body.get_response_body_type()

        for header in missing_headers:
            details = BadFieldRequest()
            details.location = 'header'
            details.field = header
            details.error_messages = ['Request is missing header.']
            response.body.errors.append(details)

        update_response_with_request_ids_for_filters(request_log, response, http_request)
        request_log.finish(response)
        self.log_serializer.save(request_log)

        response = convert_object_to_dict(response)
        return JSONResponse(response, status_code=status_code)

    def __get_independent_service_request_invalid_headers(self, request):
        headers = request.headers.keys()
        headers = [header.upper() for header in headers]

        invalid_headers = []
        for header in RESERVED_MANDATORY_GATEWAY_HEADERS:
            if header in headers:
                invalid_headers.append(header)

        return invalid_headers

    def __request_has_reserved_headers_response(self, request):
        request_type = self.service.get_configuration('observability.request_id_prefix')
        request_log = RequestLog.initialize(request_type, request, self.service)

        invalid_headers = self.__get_independent_service_request_invalid_headers(request)

        status_code = 400

        response = ApiResponse()
        response.header.status_code = status_code
        response.header.message = 'The request input was invalid, including reserved API gateway headers.'
        response.header.code = errors.INVALID_DATA
        response.body = BadRequestDetails()
        response.header.body_type = response.body.get_response_body_type()

        for header in invalid_headers:
            details = BadFieldRequest()
            details.location = 'header'
            details.field = header
            details.error_messages = ['Request includes reserved header.']
            response.body.errors.append(details)

        update_response_with_request_ids_for_filters(request_log, response, request)
        request_log.finish(response)
        self.log_serializer.save(request_log)

        response = convert_object_to_dict(response)
        return JSONResponse(response, status_code=status_code)

    def __request_has_authorization_header(self, request):
        headers = request.headers.keys()
        headers = [header.lower() for header in headers]

        return 'authorization' in headers

    def __is_authorization_header_valid(self, request):
        # TODO: implement
        return True

    def __unauthorized_response(self, http_request):
        request_type = self.service.get_configuration('observability.request_id_prefix')
        request_log = RequestLog.initialize(request_type, http_request, self.service)

        status_code = 403

        response = ApiResponse()
        response.header.status_code = status_code
        response.header.message = 'Unable to verify the validity of the Authorization token provided.'
        response.header.code = errors.ERR_ACCESS_DENIED
        response.header.body_type = 'failure_info'

        update_response_with_request_ids_for_filters(request_log, response, http_request)
        request_log.finish(response)
        self.log_serializer.save(request_log)

        response = convert_object_to_dict(response)
        return JSONResponse(response, status_code=status_code)
