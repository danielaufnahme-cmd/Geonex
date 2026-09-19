expected = [
    "STRING_TYPE",
    "INT_TYPE",
    "FLOAT_TYPE",
    "BOOL_TYPE",
    "IF",
    "ELSE",
    "TRUE",
    "FALSE",
    "PRINT",
    "PRINTLN",
    "WHILE",
    "FOR",
    "RETURN",
    "PLUS",
    "MINUS",
    "STAR",
    "SLASH",
    "PERCENT",
    "LESS",
    "GREATER",
    "NOT",
    "EQUAL_EQUAL",
    "NOT_EQUAL",
    "LESS_EQUAL",
    "GREATER_EQUAL",
    "AND",
    "OR",
    "PLUS_EQUALS",
    "MINUS_EQUALS",
    "STAR_EQUALS",
    "SLASH_EQUALS",
    "PLUS_PLUS",
    "MINUS_MINUS",
    "LPAREN",
    "RPAREN",
    "LBRACE",
    "RBRACE",
    "LBRACKET",
    "RBRACKET",
    "COMMA",
    "DOT",
    "EQUALS",
    "SEMICOLON",
    "IDENTIFIER",
    "INTEGER",
    "FLOAT",
    "STRING",
    "EOF",
]

type_tokens = ["STRING_TYPE", "INT_TYPE", "FLOAT_TYPE", "BOOL_TYPE"]

value_tokens = ["INTEGER", "FLOAT", "STRING", "TRUE", "FALSE"]

arithmetic_operators = ["PLUS", "MINUS", "STAR", "SLASH", "PERCENT"]

higher_precedence_arithmetic_operators = ["STAR", "SLASH", "PERCENT"]

lower_precedence_arithmetic_operators = ["PLUS", "MINUS"]


class Parser:
    def __init__(self, lexer_tokens):
        self.tokens = lexer_tokens
        self.position = 0

    def current_token(self):
        return self.tokens[self.position]

    def advance(self):
        self.position += 1
        return self.position

    def expect(self, expected_type):
        if self.current_token().type == expected_type:
            self.advance()
            token_expected = True
            return token_expected
        else:
            token = self.current_token()
            raise SyntaxError(
                f"Expected {expected_type}, but got {token.type} "
                f"at line {token.line}, column {token.column}"
            )

    def parse_variable_declaration(self):
        type_token = self.current_token()
        if type_token.type in type_tokens:
            self.expect(type_token.type)
        else:
            raise SyntaxError(
                f"Expected a type, but got {type_token.type} "
                f"at line {type_token.line}, column {type_token.column}"
            )

        name_token = self.current_token()
        self.expect("IDENTIFIER")
        self.expect("EQUALS")
        value = self.parse_expression()
        self.expect("SEMICOLON")

        return {
            "type": type_token.type,
            "name": name_token.value,
            "value": value,
        }

    def parse_value(self):
        token = self.current_token()
        if token.type == "LPAREN":
            self.expect("LPAREN")
            node = self.parse_expression()
            self.expect("RPAREN")
            return node
        if token.type not in value_tokens:
            raise SyntaxError(
                f"Expected a value, but got {token.type} "
                f"at line {token.line}, column {token.column}"
            )
        self.expect(token.type)
        return {"kind": "literal", "type": token.type, "value": token.value}

    def parse_term(self):
        node = self.parse_value()
        while self.current_token().type in higher_precedence_arithmetic_operators:
            operator = self.current_token().type
            self.expect(operator)
            right = self.parse_value()
            node = {"kind": "binary", "operator": operator, "left": node, "right": right}
        return node

    def parse_expression(self):
        node = self.parse_term()
        while self.current_token().type in lower_precedence_arithmetic_operators:
            operator = self.current_token().type
            self.expect(operator)
            right = self.parse_term()
            node = {"kind": "binary", "operator": operator, "left": node, "right": right}
        return node


operator_symbols = {
    "PLUS": "+",
    "MINUS": "-",
    "STAR": "*",
    "SLASH": "/",
    "PERCENT": "%",
}


def format_expression(node):
    if node["kind"] == "literal":
        return node["value"]

    left = format_expression(node["left"])
    right = format_expression(node["right"])
    if node["left"]["kind"] == "binary":
        left = f"({left})"
    if node["right"]["kind"] == "binary":
        right = f"({right})"
    return f"{left} {operator_symbols[node['operator']]} {right}"


if __name__ == "__main__":
    from lexer import tokens

    parser = Parser(tokens)
    try:
        while parser.current_token().type in type_tokens:
            declaration = parser.parse_variable_declaration()
            declaration["value"] = format_expression(declaration["value"])
            print(declaration)
    except SyntaxError as error:
        print(f"Syntax error: {error}")
