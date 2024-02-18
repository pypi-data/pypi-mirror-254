from abc import ABC, abstractmethod

from convergence.internal.observability.request_log import RequestLog


class ILogSerializer(ABC):
    @abstractmethod
    def save(self, request_log: RequestLog):
        pass


class LogSerializerConfig:
    @staticmethod
    def create(service) -> ILogSerializer:
        from convergence.internal.observability.serializers.json_serializer import JsonLogSerializer
        path = service.get_configuration('observability.path')
        production = service.get_configuration('application.mode') == 'production'
        return JsonLogSerializer(path, production)
