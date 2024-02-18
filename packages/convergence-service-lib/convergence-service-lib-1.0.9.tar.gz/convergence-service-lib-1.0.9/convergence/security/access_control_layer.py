from fastapi import Request

from convergence.security.rule_expression import AuthorizationRuleExpression


class AccessControlLayer:
    def __init__(self):
        self.__rule_expression_cache = {}

    def is_authorized(self, rule: str, request: Request, token: dict):
        rule_expression = self.__parse_rule_expression(rule)
        context = {
            'acl': self,
            'req': request, 'request': request,
            'false': False, 'true': True,
            'token': token
        }

        return rule_expression.evaluate(context)

    def allow_all(self, **kwargs):
        return True

    def is_signed_in(self, **kwargs):
        token = kwargs.get('token')
        return token is not None

    def not_signed_in(self, **kwargs):
        token = kwargs.get('token')
        return token is None

    def has_authority(self, authority, **kwargs):
        token = kwargs.get('token')
        if token is None:
            return False
        authorities = token.get('authorities')
        if authorities is None:
            return False
        return authorities is not None and authority in authorities

    def is_service(self, **kwargs):
        token = kwargs.get('token')
        if token is None:
            return False
        return token is not None and 'is_inter_service_call' in token and token['is_inter_service_call']

    def is_system_admin(self, **kwargs):
        token = kwargs.get('token')
        if token is None:
            return False
        return self.has_authority(token, 'authority::*')

    def __parse_rule_expression(self, rule):
        if rule in self.__rule_expression_cache:
            return self.__rule_expression_cache[rule]

        result = AuthorizationRuleExpression()
        result.parse(rule)

        self.__rule_expression_cache[rule] = result
        return result
