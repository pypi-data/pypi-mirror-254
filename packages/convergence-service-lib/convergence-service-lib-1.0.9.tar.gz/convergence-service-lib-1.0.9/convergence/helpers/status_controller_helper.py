from convergence.dto.service_status import ServiceEndpointDTO


def matches_any(internal_endpoint_urls, path):
    return path in internal_endpoint_urls


def __get_expected_authorization(authorization):
    if authorization == "@acl.allow_all()":
        return "@allow_all"
    elif authorization == "@acl.is_signed_in()":
        return "@signed_in"
    elif authorization == "@acl.not_signed_in()":
        return "@not_signed_in"
    elif authorization == "@acl.is_service()":
        return "@service_call"
    elif authorization is not None and authorization.startswith("@acl.has_authority("):
        authority = "@acl.has_authority("
        authority = authorization[len(authority) + 1:-2]
        if ')' in authority:
            return '<authorization_expression>'
        else:
            return authority
    else:
        # Python service allows expression and can't be generalized here, so allow all will pass it to the service
        # for evaluation
        return "@allow_all"


def load_service_urls(service):
    endpoints = []
    for route in service.app.routes:
        if route.include_in_schema:
            for method in route.methods:
                (info, _) = service.get_endpoint_info(route.path, method)
                ep = ServiceEndpointDTO()
                ep.url = route.path
                ep.method = method
                ep.exposed_through_gateway = info.exposed_through_gateway
                ep.expected_authorization = __get_expected_authorization(info.authorization)

                endpoints.append(ep)

    return endpoints
