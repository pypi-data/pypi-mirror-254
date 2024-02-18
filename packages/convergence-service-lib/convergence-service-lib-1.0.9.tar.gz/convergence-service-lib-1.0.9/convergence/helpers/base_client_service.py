import abc
import uuid
from datetime import datetime, timezone, timedelta
from enum import Enum
from typing import Any, Dict, Optional

import jwt
import requests

from convergence.constants import HEADER_REQUEST_ID, HEADER_PARENT_REQUEST_ID, HEADER_CALLER_SERVICE, \
    HEADER_CALLER_SERVICE_HASH, HEADER_CALLER_SERVICE_VERSION
from convergence.dto.bad_request_details import BadRequestDetails, BadFieldRequest
from convergence.dto.base_dto import ApiResponse, ApiResponseHeader
from convergence.helpers.errors import ERR_UNABLE_PARSE_SERVICE_RESPONSE
from convergence.internal.observability.request_log import RequestLog


class ServiceClientMode(Enum):
    INTERNAL = 1,
    EXTERNAL = 2,


class BaseServiceClient(abc.ABC):
    def __init__(self, mode: ServiceClientMode, url: Optional[str], verify_ssl: bool, type_mapper: Dict[str, Any]):
        self.__mode = mode
        self.__url = url
        self.__verify_ssl = verify_ssl
        self.__type_mapper = type_mapper

    def _make_get_call(self, request_log: RequestLog, url, required_authorization):
        headers = {
            'Content-Type': 'application/json'
        }
        self.__fill_authorization_header(required_authorization, headers)
        self.__fill_request_id_headers(request_log, headers)
        target_url = self.__get_service_url() + url

        response = requests.get(target_url, verify=self.__verify_ssl, headers=headers)
        parsed = self.__parse_json_output(response)

        return self.__build_response(parsed)

    def _make_post_call(self, request_log: RequestLog, url, required_authorization, request_body=None):
        headers = {
            'Content-Type': 'application/json'
        }
        self.__fill_authorization_header(required_authorization, headers)
        self.__fill_request_id_headers(request_log, headers)
        target_url = self.__get_service_url() + url

        content = request_body.to_dict() if request_body is not None else None
        response = requests.post(target_url, verify=self.__verify_ssl, headers=headers, json=content)
        parsed = self.__parse_json_output(response)

        return self.__build_response(parsed)

    def _make_patch_call(self, request_log: RequestLog, url, required_authorization, request_body=None):
        headers = {
            'Content-Type': 'application/json'
        }
        self.__fill_authorization_header(required_authorization, headers)
        self.__fill_request_id_headers(request_log, headers)
        target_url = self.__get_service_url() + url

        content = request_body.to_dict() if request_body is not None else None
        response = requests.patch(target_url, verify=self.__verify_ssl, headers=headers, json=content)
        parsed = self.__parse_json_output(response)

        return self.__build_response(parsed)

    def _make_put_call(self, request_log: RequestLog, url, required_authorization, request_body=None):
        headers = {
            'Content-Type': 'application/json'
        }
        self.__fill_authorization_header(required_authorization, headers)
        self.__fill_request_id_headers(request_log, headers)
        target_url = self.__get_service_url() + url

        content = request_body.to_dict() if request_body is not None else None
        response = requests.put(target_url, verify=self.__verify_ssl, headers=headers, json=content)
        parsed = self.__parse_json_output(response)

        return self.__build_response(parsed)

    def _make_delete_call(self, request_log: RequestLog, url, required_authorization, request_body=None):
        headers = {
            'Content-Type': 'application/json'
        }
        self.__fill_authorization_header(required_authorization, headers)
        self.__fill_request_id_headers(request_log, headers)
        target_url = self.__get_service_url() + url

        content = request_body.to_dict() if request_body is not None else None
        response = requests.delete(target_url, verify=self.__verify_ssl, headers=headers, json=content)
        parsed = self.__parse_json_output(response)

        return self.__build_response(parsed)

    def __build_response(self, parsed):
        if isinstance(parsed, ApiResponse):
            return parsed

        response_type = parsed['header']['body_type']
        if response_type in self.__type_mapper:
            result = ApiResponse()
            result.header = self.__parse_header(parsed['header'])
            result.body = self.__type_mapper[response_type].from_dict(parsed['body'])
            return result
        elif response_type in ['empty', 'api_failure']:
            result = ApiResponse()
            result.header = self.__parse_header(parsed['header'])
            return result
        elif response_type == 'request_error_info':
            result = ApiResponse()
            result.header = self.__parse_header(parsed['header'])
            result.body = self.__parse_bad_request_error_info(parsed['body'])
            return result
        else:
            raise ValueError('Unexpected error occurred while parsing the API response.')

    def __fill_authorization_header(self, authorization, headers):
        if authorization in ["@allow_all", "@not_signed_in"]:
            # No need to include an authorization header
            pass
        elif authorization == "@signed_in":
            jwt_header = f'Bearer {self.__create_jwt(None, False)}'
            headers['Authorization'] = jwt_header
        elif authorization == "@service_call":
            jwt_header = f'Bearer {self.__create_jwt(None, True)}'
            headers['Authorization'] = jwt_header
        else:
            jwt_header = f'Bearer {self.__create_jwt(authorization, False)}'
            headers['Authorization'] = jwt_header

    def __create_jwt(self, authorities, service_jwt):
        signing_key = self.get_jwt_signing_key()
        info = self.get_service_info()

        payload = {
            "sub": info.SERVICE_NAME,
            "iss": info.SERVICE_NAME,
            "exp": datetime.now(tz=timezone.utc) + timedelta(minutes=1),
        }

        if service_jwt:
            payload['is_inter_service_call'] = True

        if authorities is not None:
            authorities = [] if authorities is None else authorities
            authorities = [authorities] if not isinstance(authorities, list) else authorities
            payload['authorities'] = authorities

        return jwt.encode(payload, signing_key, algorithm="ES512")

    def __get_service_url(self):
        if self.__url is None:
            raise ValueError('To be implemented: get the service URL from core-service')

        return self.__url

    def __parse_json_output(self, response):
        try:
            return response.json()
        except:  # noqa
            result = ApiResponse()

            result.header.body_type = 'api_failure'
            result.header.status_code = response.status_code
            result.header.code = ERR_UNABLE_PARSE_SERVICE_RESPONSE
            result.header.message = 'The response got from the service is not valid JSON and can not be parsed.'
            result.header.request_id = None
            result.header.parent_request_id = None

            return result

    def __parse_header(self, parsed):
        result = ApiResponseHeader()

        result.body_type = parsed['body_type']
        result.status_code = parsed['status_code']
        result.code = parsed['code']
        result.message = parsed['message']
        result.request_id = parsed['request_id']
        result.parent_request_id = parsed['parent_request_id']

        return result

    def __fill_request_id_headers(self, request_log, headers):
        info = self.get_service_info()

        if self.__mode == ServiceClientMode.INTERNAL:
            headers[HEADER_REQUEST_ID] = str(uuid.uuid4())
            headers[HEADER_PARENT_REQUEST_ID] = request_log.request_identifier
            headers[HEADER_CALLER_SERVICE] = info.SERVICE_NAME
            headers[HEADER_CALLER_SERVICE_HASH] = info.SERVICE_VERSION_HASH
            headers[HEADER_CALLER_SERVICE_VERSION] = info.SERVICE_VERSION

    @abc.abstractmethod
    def get_jwt_signing_key(self):
        pass

    @abc.abstractmethod
    def get_service_info(self):
        pass

    def __parse_bad_request_error_info(self, data):
        result = BadRequestDetails()

        for e in data['errors']:
            detail = BadFieldRequest()
            detail.location = e['location']
            detail.field = e['field']
            detail.error_messages = e['error_messages']

            result.errors.append(detail)

        return result
