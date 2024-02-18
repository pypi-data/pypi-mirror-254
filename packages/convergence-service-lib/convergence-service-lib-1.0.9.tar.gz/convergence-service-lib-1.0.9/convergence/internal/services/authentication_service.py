from convergence.internal.services.base_internal_service import BaseExternalService


class AuthenticationMicroService(BaseExternalService):
    def __init__(self, service, url):
        super().__init__(service, url, service_jwt=True)

    def register_service_authority(self, request):
        return self.post_request('/authentication/internal-services/register-authority', request)
