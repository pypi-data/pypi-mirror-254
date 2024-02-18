from convergence.internal.services.base_internal_service import BaseExternalService


class InfrastructureMicroService(BaseExternalService):
    def __init__(self, service):
        super().__init__(service, service.get_configuration('application.convergence_core_service_url'), service_jwt=True)

    def get_service_connection_details(self, service_name):
        request = {
            'service_name': service_name
        }

        return self.post_request('/infrastructure/get-service-info', request)
