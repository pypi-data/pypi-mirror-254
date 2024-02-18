import jwt
from jwt import DecodeError
from starlette.middleware.base import BaseHTTPMiddleware
from fastapi import Request
from starlette.responses import JSONResponse

from convergence.dto.base_dto import ApiResponse
from convergence.helpers import errors
from convergence.helpers.controller_helpers import convert_object_to_dict, update_response_with_request_ids_for_filters
from convergence.internal.observability.request_log import RequestLog
from convergence.internal.observability.serializer_config import LogSerializerConfig


class AuthorizationMiddleware(BaseHTTPMiddleware):
    def __init__(self, app, **kwargs):
        super().__init__(app)
        self.service = kwargs['service']
        self.signing_key = self.service.get_configuration('security.authentication.secret')
        self.signing_key = self.signing_key.replace('\\n', '\n')
        self.log_serializer = LogSerializerConfig.create(self.service)
        self.request_type = self.service.get_configuration('observability.request_id_prefix')

    async def dispatch(self, request: Request, call_next):
        path = request.scope.get('path')
        method = request.scope.get('method')
        endpoint_info, path_matched = self.service.get_endpoint_info(path, method)

        if endpoint_info is None:
            if path_matched:
                response = self.__not_allowed_method_response(path, request)
            else:
                response = self.__not_found_response(path, request)
        else:
            auth_header = request.headers.get('Authorization')

            payload = None
            if auth_header is not None:
                err_code, message, payload = self.__is_valid_authorization_token(auth_header)
                if err_code is not None:
                    return self.__invalid_authorization_header(err_code, message, request)

            if endpoint_info.authorization is None or self.is_authorized(endpoint_info, request, payload):
                response = await call_next(request)
            else:
                response = self.__unauthorized_response(path, request)

        return response

    def is_authorized(self, endpoint_info, request, token_payload):
        acl = self.service.acl
        return acl.is_authorized(endpoint_info.authorization, request, token_payload)

    def __is_valid_authorization_token(self, auth_header):
        err_code = None
        err_message = None

        bearer_length = len('Bearer ')
        if auth_header[0:bearer_length] != 'Bearer ':
            err_code = errors.ERR_ACCESS_DENIED
            err_message = 'Service expects an authorization token in Bearer format.'
            return err_code, err_message, None

        try:
            auth_header = auth_header[bearer_length:]
            result = jwt.decode(auth_header, key=self.signing_key, algorithms="ES512")
            return None, None, result
        except DecodeError as ex:  # noqa
            err_code = errors.ERR_ACCESS_DENIED
            err_message = 'Service expects a valid JWT token.'

            return err_code, err_message, None

    def __invalid_authorization_header(self, err_code, message, http_request):
        request_log = RequestLog.initialize(self.request_type, http_request, self.service)

        status_code = 403

        response = ApiResponse()
        response.header.status_code = status_code
        response.header.message = message
        response.header.code = err_code
        response.header.body_type = 'failure_info'

        update_response_with_request_ids_for_filters(request_log, response, http_request)
        request_log.finish(response)
        self.log_serializer.save(request_log)

        response = convert_object_to_dict(response)
        return JSONResponse(response, status_code=status_code)

    def __unauthorized_response(self, path, http_request):
        request_log = RequestLog.initialize(self.request_type, http_request, self.service)

        status_code = 403

        response = ApiResponse()
        response.header.status_code = status_code
        response.header.message = f'The authorization token is invalid for path {path}'
        response.header.code = errors.ERR_ACCESS_DENIED
        response.header.body_type = 'failure_info'

        update_response_with_request_ids_for_filters(request_log, response, http_request)
        request_log.finish(response)
        self.log_serializer.save(request_log)

        response = convert_object_to_dict(response)
        return JSONResponse(response, status_code=status_code)

    def __not_found_response(self, path, http_request):
        request_log = RequestLog.initialize(self.request_type, http_request, self.service)

        status_code = 404

        response = ApiResponse()
        response.header.status_code = status_code
        response.header.message = f'Unable to find resource at path {path}'
        response.header.code = errors.API_RESOURCE_NOT_FOUND
        response.header.body_type = 'failure_info'

        update_response_with_request_ids_for_filters(request_log, response, http_request)
        request_log.finish(response)
        self.log_serializer.save(request_log)

        response = convert_object_to_dict(response)
        return JSONResponse(response, status_code=status_code)

    def __not_allowed_method_response(self, path, http_request):
        request_log = RequestLog.initialize(self.request_type, http_request, self.service)

        status_code = 405

        response = ApiResponse()
        response.header.status_code = status_code
        response.header.message = f'Unable to find resource at path {http_request.method.upper()} {path}'
        response.header.code = errors.API_METHOD_NOT_ALLOWED
        response.header.body_type = 'failure_info'

        update_response_with_request_ids_for_filters(request_log, response, http_request)
        request_log.finish(response)
        self.log_serializer.save(request_log)

        response = convert_object_to_dict(response)
        return JSONResponse(response, status_code=status_code)
