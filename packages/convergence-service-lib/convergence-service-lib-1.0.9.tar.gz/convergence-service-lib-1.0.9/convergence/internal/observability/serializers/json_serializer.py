import json

from convergence.helpers.controller_helpers import convert_object_to_dict
from convergence.internal.observability.request_log import RequestLog
from convergence.internal.observability.serializer_config import ILogSerializer


class JsonLogSerializer(ILogSerializer):
    def __init__(self, path, production):
        self.path = path
        self.production = production

    def save(self, request_log: RequestLog):
        from convergence.constants import VERSION
        # kwargs = {}
        #
        # if not self.production:
        #     kwargs['indent'] = '  '
        #
        # with open(self.path + '/' + request_log.request_identifier + '.txt', 'w') as file:
        #     json_str = jsonpickle.encode(request_log, **kwargs)
        #     file.write(json_str)
        kwargs = {}

        if not self.production:
            kwargs['indent'] = '  '

        with open(self.path + '/' + request_log.request_identifier + '.crl', 'w') as file:
            request_as_dict = convert_object_to_dict(request_log)
            request_as_dict["service_language"] = "python"
            request_as_dict["template_version"] = VERSION
            json.dump(request_as_dict, file, **kwargs)
