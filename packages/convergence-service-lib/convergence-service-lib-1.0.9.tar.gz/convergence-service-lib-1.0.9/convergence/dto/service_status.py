from typing import List, Dict
from convergence.dto.base_dto import ApiResponseBody


class ServiceEndpointDTO:
    def __init__(self):
        self.url = ''
        self.method = ''
        self.exposed_through_gateway = False
        self.expected_authorization = ''


class ServiceStatusInfoDTO(ApiResponseBody):
    def __init__(self):
        self.service_name = ''
        self.version_hash = ''
        self.version = ''
        self.status = ''
        self.endpoints: List[ServiceEndpointDTO] = []
        self.extra: Dict[str, str] = {}

    def get_response_body_type(self) -> str:
        return 'service_status'
