from typing import List

from convergence.dto.base_dto import ApiResponseBody


class BadFieldRequest:
    def __init__(self):
        self.location = ''
        self.field = ''
        self.error_messages = []


class BadRequestDetails(ApiResponseBody):
    def __init__(self):
        self.errors: List[BadFieldRequest] = []

    def get_response_body_type(self) -> str:
        return 'request_error_info'
