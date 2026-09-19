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

    def parse_expression(self):
        token = self.current_token()
        if token.type in value_tokens:
            self.expect(token.type)
            return token.value
        else:
            raise SyntaxError(
                f"Expected a value, but got {token.type} "
                f"at line {token.line}, column {token.column}"
            )


if __name__ == "__main__":
    from lexer import tokens

    parser = Parser(tokens)
    try:
        while parser.current_token().type in type_tokens:
            declaration = parser.parse_variable_declaration()
            print(declaration)
    except SyntaxError as error:
        print(f"Syntax error: {error}")
