import traceback

from convergence.dto.base_dto import FailureInfoDTO, create_api_response
import convergence.helpers.errors as errors
from convergence.internal.observability.request_log import RequestLog
from convergence.internal.observability.serializer_config import LogSerializerConfig

LOG_SERIALIZER = None


class ManagedApiError(BaseException):
    def __init__(self, status_code, code, message):
        self.status_code = status_code
        self.code = code
        self.message = message


def update_response_with_request_ids_for_filters(request_log: RequestLog, response, http_request):
    response.header.request_id = __remove_request_id_prefix(request_log.request_identifier)
    response.header.parent_request_id = request_log.parent_request_identifier


def __remove_request_id_prefix(request_identifier):
    if '_' in request_identifier:
        request_identifier = request_identifier[request_identifier.rindex('_') + 1:]
    return request_identifier


def run_api_method(request_log: RequestLog, service, http_request, http_response, func):
    global LOG_SERIALIZER
    if LOG_SERIALIZER is None:
        LOG_SERIALIZER = LogSerializerConfig.create(service)

    api_response = None
    try:
        api_response = create_api_response(func(), http_request)
    except BaseException as ex:
        tb = traceback.format_exc()
        request_log.exception(ex, tb)
        api_response = create_internal_error_response(service, http_request, errors.API_INTERNAL_ERROR, ex)

    http_response.status_code = api_response.header.status_code

    api_response.header.request_id = __remove_request_id_prefix(request_log.request_identifier)
    api_response.header.parent_request_id = request_log.parent_request_identifier

    request_log.finish(api_response)
    LOG_SERIALIZER.save(request_log)
    return api_response


def create_internal_error_response(service, http_request, code: str, ex: BaseException):
    failure = FailureInfoDTO()
    message = str(ex)

    if isinstance(ex, ManagedApiError):
        failure.code = ex.code
        failure.message = ex.message
        failure.status_code = ex.status_code

        return create_api_response(failure, http_request)
    elif service.get_configuration('application.mode') == 'production':
        message = "An unexpected error happened during API execution"

    failure.code = code
    failure.message = message
    failure.status_code = 500

    return create_api_response(failure, http_request)


def convert_object_to_dict(obj):
    if isinstance(obj, dict):
        return {str(key): convert_object_to_dict(item) for key, item in obj.items()}
    elif obj is None:
        return None
    elif isinstance(obj, int) or isinstance(obj, float):
        return obj
    elif not hasattr(obj, "__dict__"):
        return str(obj)

    result = {}
    skip_field = '_SKIP_LOGGING_FIELDS'
    secret_fields = getattr(obj, skip_field) if hasattr(obj, skip_field) else []
    for key, val in obj.__dict__.items():
        if key.startswith("_"):
            continue

        if isinstance(val, list):
            element = []
            for item in val:
                element.append(convert_object_to_dict(item))
        elif isinstance(val, set) or isinstance(val, tuple):
            element = []
            val = list(val)
            for item in val:
                element.append(convert_object_to_dict(item))
        else:
            element = convert_object_to_dict(val)
        result[key] = element

    for field in secret_fields:
        result[field] = '***********'

    return result
