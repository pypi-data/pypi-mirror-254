import encodings.utf_8
import json

from starlette.middleware.base import BaseHTTPMiddleware
from fastapi import Request
from starlette.responses import JSONResponse

from convergence.dto.bad_request_details import BadRequestDetails, BadFieldRequest
from convergence.dto.base_dto import ApiResponse
from convergence.helpers import errors
from convergence.helpers.controller_helpers import convert_object_to_dict, update_response_with_request_ids_for_filters
from convergence.internal.observability.request_log import RequestLog
from convergence.internal.observability.serializer_config import LogSerializerConfig


def convert_pydantic_error_to_convergence(error_response) -> BadRequestDetails:
    result = BadRequestDetails()

    errors = {}
    for entry in error_response['detail']:
        map_id = create_map_id(entry['loc'])
        error_entry = None
        if map_id in errors:
            error_entry = errors[map_id]
        else:
            error_entry = BadFieldRequest()
            error_entry.location = entry['loc'][0]
            error_entry.field = create_map_id(entry['loc'][1:])
            result.errors.append(error_entry)
            errors[map_id] = error_entry

        error_entry.error_messages.append(entry['msg'])

    return result


def create_map_id(list_of_fields):
    result = ''

    sep = ''
    for field in list_of_fields:
        if isinstance(field, int):
            result += f'[{field}]'
        else:
            result += f'{sep}{field}'
        sep = '.'

    return result


class InputValidationMiddleware(BaseHTTPMiddleware):
    def __init__(self, app, **kwargs):
        super().__init__(app)
        self.service = kwargs['service']
        self.log_serializer = LogSerializerConfig.create(self.service)

    async def dispatch(self, request: Request, call_next):
        response = await call_next(request)

        if response.status_code == 422:
            error_response = await self.__extract_pydantic_response(response)
            if response is None:
                response = self.__internal_error_response(request)
            elif self.__is_invalid_json(error_response):
                response = self.__invalid_json_input(request)
            else:
                response = self.__build_convergence_unified_bad_request(error_response, request)

        return response

    def __internal_error_response(self, http_request):
        request_type = self.service.get_configuration('observability.request_id_prefix')
        request_log = RequestLog.initialize(request_type, http_request, self.service)

        status_code = 500

        response = ApiResponse()
        response.header.status_code = status_code
        response.header.message = 'The request input was invalid, but failed to create a proper problem detail.'
        response.header.code = errors.INVALID_DATA
        response.header.body_type = 'failure_info'

        update_response_with_request_ids_for_filters(request_log, response, http_request)
        request_log.finish(response)
        self.log_serializer.save(request_log)

        response = convert_object_to_dict(response)
        return JSONResponse(response, status_code=status_code)

    async def __extract_pydantic_response(self, response):
        try:
            chunks = []
            async for chunk in response.body_iterator:
                chunk = encodings.utf_8.decode(chunk)[0]
                chunks.append(chunk)
            chunks = ''.join(chunks)
            return json.loads(chunks)
        except:
            return None

    def __build_convergence_unified_bad_request(self, error_response, http_request):
        request_type = self.service.get_configuration('observability.request_id_prefix')
        request_log = RequestLog.initialize(request_type, http_request, self.service)

        status_code = 400

        response = ApiResponse()
        response.header.status_code = status_code
        response.header.message = 'The request input is invalid, refer to body for details.'
        response.header.code = errors.INVALID_DATA
        response.body = convert_pydantic_error_to_convergence(error_response)
        response.header.body_type = response.body.get_response_body_type()

        update_response_with_request_ids_for_filters(request_log, response, http_request)
        request_log.finish(response)
        self.log_serializer.save(request_log)

        response = convert_object_to_dict(response)
        return JSONResponse(response, status_code=status_code)

    def __is_invalid_json(self, response):
        try:
            path = ['detail', 0, 'msg']
            msg = response

            for component in path:
                msg = msg[component]

            return msg is not None and msg == 'JSON decode error'
        except:  # noqa
            return False

    def __invalid_json_input(self, http_request):
        request_type = self.service.get_configuration('observability.request_id_prefix')
        request_log = RequestLog.initialize(request_type, http_request, self.service)

        status_code = 400

        response = ApiResponse()
        response.header.status_code = status_code
        response.header.message = 'The request input is not a valid JSON.'
        response.header.code = errors.API_UNPARSABLE_JSON
        response.header.body_type = "api_failure"
        response.body = None

        update_response_with_request_ids_for_filters(request_log, response, http_request)
        request_log.finish(response)
        self.log_serializer.save(request_log)

        response = convert_object_to_dict(response)
        return JSONResponse(response, status_code=status_code)
