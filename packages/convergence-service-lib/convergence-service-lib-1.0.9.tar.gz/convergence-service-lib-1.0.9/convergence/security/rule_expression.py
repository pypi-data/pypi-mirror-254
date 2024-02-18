IDENTIFIER_CHARACTERS = 'qwertyuiopasdfghjklzxcvbnm1234567890QWERTYUIOPASDFGHJKLZXCVBNM_'


class AuthorizationRuleExpression:
    def __init__(self):
        self._tokens = []
        self._postfix_tokens = []
        self.rule = None

    def parse(self, rule):
        self.rule = rule
        self._tokens = self.__tokenize()
        self._postfix_tokens = self.__to_postfix()

    def evaluate(self, context):
        stack = []
        kwargs = {
            'token': context['token'],
            'req': context['req'],
            'request': context['request'],
        }

        for token in self._postfix_tokens:
            if self.__is_field(token):
                field_name = token[1:]
                if field_name not in context:
                    raise ValueError(f'Undefined field @{field_name} in authorization rule.')
                stack.append(context[field_name])
            elif token == '.':
                stack, a, b = self.__pop_top_two(stack)
                value = getattr(b, a)
                stack.append(value)
            elif token == 'and':
                stack, a, b = self.__pop_top_two(stack)
                stack.append(a and b)
            elif token == 'or':
                stack, a, b = self.__pop_top_two(stack)
                stack.append(a or b)
            elif self.__is_string(token):
                stack.append(token[1:-1])
            elif self.__is_identifier(token):
                stack.append(token)
            elif token.startswith('__call__:'):
                count = int(token[9:])
                params = []
                for i in range(count):
                    params.append(self.__peek_stack(stack))
                    stack = self.__pop_stack(stack)

                function = self.__peek_stack(stack)
                stack = self.__pop_stack(stack)

                value = function(*params, **kwargs)
                stack.append(value)
            else:
                raise ValueError(f'Unsupported token: {token}')

        if len(stack) != 1:
            raise ValueError("Invalid expression as the stack is not down to a single value!")

        return stack[0]

    def __pop_top_two(self, stack):
        a = self.__peek_stack(stack)
        stack = self.__pop_stack(stack)
        b = self.__peek_stack(stack)
        stack = self.__pop_stack(stack)

        return stack, a, b

    def __tokenize(self):
        result = []
        temp = self.rule

        while len(temp) > 0:
            ch = temp[0]
            if ch == ' ':
                temp = temp[1:]
            elif ch == '@':
                token = self.__read_field(temp)
                result.append(token)
                temp = temp[len(token):]
            elif ch == '"' or ch == '\'':
                token = self.__read_string(temp)
                result.append(token)
                temp = temp[len(token):]
            elif ch in ['.', '(', ')', ',']:
                token = ch
                result.append(token)
                temp = temp[len(token):]
            elif ch in 'qwertyuiopasdfghjklzxcvbnm1234567890QWERTYUIOPASDFGHJKLZXCVBNM_':
                token = self.__read_identifier(temp)
                result.append(token)
                temp = temp[len(token):]
            else:
                raise ValueError(f'Unable to parse expression: {self.rule}')

        return result

    def __read_field(self, temp):
        result = ['@']

        i = 1
        while i < len(temp) and temp[i] in IDENTIFIER_CHARACTERS:
            result.append(temp[i])
            i += 1

        return ''.join(result)

    def __read_string(self, temp):
        ch = temp[0]
        temp = temp[1:]

        if ch in temp:
            result = ch + temp[0:temp.index(ch)] + ch
        else:
            raise ValueError('Looks like one of the string is not properly closed.')

        return result

    def __read_identifier(self, temp):
        result = []

        i = 0
        while i < len(temp) and temp[i] in IDENTIFIER_CHARACTERS:
            result.append(temp[i])
            i += 1

        return ''.join(result)

    def __to_postfix(self):
        stack = []
        result = []
        function_call_tokens = self.__insert_function_call_operator()
        for token in function_call_tokens:
            if token.startswith('__call__:'):
                result.append(token)
            elif self.__is_operator(token):
                while self.__get_operator_precedence(token) <= self.__get_operator_precedence(self.__peek_stack(stack)):
                    result.append(self.__peek_stack(stack))
                    stack = self.__pop_stack(stack)

                stack.append(token)
            elif self.__is_string(token) or self.__is_field(token) or self.__is_identifier(token):
                result.append(token)
            elif token == ',':
                while self.__peek_stack(stack) != '(':
                    result.append(self.__peek_stack(stack))
                    stack = self.__pop_stack(stack)
            elif token == '(':
                while self.__peek_stack(stack) == '.':
                    stack = self.__pop_stack(stack)
                    result.append('.')

                stack.append('(')
            elif token == ')':
                while self.__peek_stack(stack) != '(' and self.__peek_stack(stack) is not None:
                    result.append(self.__peek_stack(stack))
                    stack = self.__pop_stack(stack)

                if self.__peek_stack(stack) == '(':
                    stack = self.__pop_stack(stack)
        while self.__peek_stack(stack) is not None:
            result.append(self.__peek_stack(stack))
            stack = self.__pop_stack(stack)

        return result

    def __is_string(self, token):
        return token.startswith('"') or token.startswith("'")

    def __is_field(self, token):
        return token.startswith('@') and self.__is_identifier(token[1:])

    def __is_identifier(self, token):
        result = True

        for ch in token:
            result = result and ch in IDENTIFIER_CHARACTERS

        return result

    def __is_operator(self, token):
        return token in ['and', 'or', '.']

    def __insert_function_call_operator(self):
        result = []
        stack = []

        depth = 0
        last_token_type = '('

        for index, token in enumerate(self._tokens):
            result.append(token)
            if self.__is_operator(token):
                last_token_type = 'operator'
            elif token == ',':
                last_token_type = 'coma'
                top_stack = self.__peek_stack(stack)
                top_stack['seen_coma'] += 1
            elif self.__is_string(token):
                last_token_type = 'string'
            elif self.__is_field(token):
                last_token_type = 'field'
            elif self.__is_identifier(token):
                last_token_type = 'identifier'
            elif token == '(':
                if last_token_type == 'identifier':
                    stack.append({
                        'depth': depth,
                        'start': index,
                        'seen_coma': 0
                    })
                last_token_type = '('
                depth += 1
                pass
            elif token == ')':
                depth -= 1
                top_stack = self.__peek_stack(stack)
                if top_stack is not None:
                    prev_depth = top_stack['depth']
                    param_count = 0
                    if index != top_stack['start'] + 1:
                        param_count = top_stack['seen_coma'] + 1

                    if prev_depth == depth:
                        result.append(f'__call__:{param_count}')
                        stack = self.__pop_stack(stack)
                last_token_type = ')'

        return result

    def __peek_stack(self, stack):
        if len(stack) > 0:
            return stack[-1]

        return None

    def __pop_stack(self, stack):
        return stack[0:-1]

    def __get_operator_precedence(self, token):
        if token is None or token == '(':
            return -1

        priorities = {
            '.': 10,
            'and': 2,
            'or': 2,
        }

        return priorities[token]
