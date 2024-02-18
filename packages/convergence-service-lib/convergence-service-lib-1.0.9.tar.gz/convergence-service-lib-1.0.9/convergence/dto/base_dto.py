import abc


class ApiResponseHeader:
    def __init__(self):
        self.body_type: str = 'empty'
        self.status_code: int = 0
        self.code: str = ''
        self.message: str = ''
        self.request_id: str = ''
        self.parent_request_id: str = ''


class ApiResponseBody(abc.ABC):
    @abc.abstractmethod
    def get_response_body_type(self) -> str:
        pass


class ApiResponse:
    def __init__(self):
        self.header = ApiResponseHeader()
        self.body: ApiResponseBody | None = None


class FailureInfoDTO(ApiResponseBody):
    def __init__(self):
        self.status_code: int = 0
        self.code: str = ''
        self.message: str = ''

    def get_response_body_type(self) -> str:
        return 'api_failure'


def __get_list_response_body_type(body):
    result = 'empty'

    if body is not None and len(body) > 0:
        obj = body[0]
        if isinstance(obj, str):
            result = 'list[String]'
        else:
            type = obj.get_response_body_type()
            result = f'list[{type}]'

    return result


def __get_header_value(http_request, name):
    result = None
    name = name.lower()

    headers = http_request.headers.keys()
    for key in headers:
        if key.lower() == name:
            result = http_request.headers.get(key)
            break

    return result


def create_api_response(body, http_request, status_code=200) -> ApiResponse:
    if isinstance(body, ApiResponse):
        return body

    result = ApiResponse()

    if body is None:
        result.header.status_code = status_code
        result.header.body_type = 'empty'
        result.header.message = 'OK'
    elif isinstance(body, list):
        result.header.body_type = __get_list_response_body_type(body)
        result.header.status_code = status_code
        result.header.code = ''
        result.header.message = 'OK'
        result.body = body
    elif not isinstance(body, ApiResponseBody):
        raise ValueError('Api responses must be a sub class of ApiResponseBody')
    elif isinstance(body, FailureInfoDTO):
        result.header.body_type = body.get_response_body_type()
        result.header.status_code = body.status_code
        result.header.code = body.code
        result.header.message = body.message
    else:
        result.header.body_type = body.get_response_body_type()
        result.header.status_code = status_code
        result.header.code = ''
        result.header.message = 'OK'
        result.body = body

    return result
