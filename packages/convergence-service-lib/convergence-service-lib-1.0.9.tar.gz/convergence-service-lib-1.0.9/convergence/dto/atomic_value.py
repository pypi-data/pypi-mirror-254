from convergence.dto.base_dto import ApiResponseBody


class AtomicValueDTO(ApiResponseBody):
    def __init__(self, value=None):
        self.value = value

    def get_response_body_type(self) -> str:
        return 'atomic_value'
