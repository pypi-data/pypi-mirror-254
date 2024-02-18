from convergence.convergence_service import ConvergenceService


def convergence_endpoint(router, url, method='GET', exposed_through_gateway=True, authorization=None):
    ConvergenceService.register_endpoint_info(url, method, authorization, exposed_through_gateway)

    def wrapper(func):
        if method.upper() == 'GET':
            router.get(url)(func)
        elif method.upper() == 'POST':
            router.post(url)(func)
        elif method.upper() == 'PUT':
            router.put(url)(func)
        elif method.upper() == 'PATCH':
            router.patch(url)(func)
        elif method.upper() == 'DELETE':
            router.delete(url)(func)

        return func

    return wrapper
