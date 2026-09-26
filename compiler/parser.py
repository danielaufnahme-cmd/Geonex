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

print_tokens = ["PRINT", "PRINTLN"]

arithmetic_operators = ["PLUS", "MINUS", "STAR", "SLASH", "PERCENT"]

higher_precedence_arithmetic_operators = ["STAR", "SLASH", "PERCENT"]

lower_precedence_arithmetic_operators = ["PLUS", "MINUS"]

comparison_operators = [
    "LESS",
    "GREATER",
    "LESS_EQUAL",
    "GREATER_EQUAL",
    "EQUAL_EQUAL",
    "NOT_EQUAL",
]

logical_operators = ["AND", "OR"]

unary_operators = ["NOT"]

assignment_operators = [
    "EQUALS",
    "PLUS_EQUALS",
    "MINUS_EQUALS",
    "STAR_EQUALS",
    "SLASH_EQUALS",
]

increment_operators = ["PLUS_PLUS", "MINUS_MINUS"]


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

    def parse_statement(self):
        token = self.current_token()
        if token.type in type_tokens:
            return self.parse_variable_declaration()
        if token.type == "IDENTIFIER":
            return self.parse_assignment()
        if token.type == "IF":
            return self.parse_if()
        if token.type == "FOR":
            return self.parse_for()
        if token.type == "WHILE":
            return self.parse_while()
        if token.type in print_tokens:
            return self.parse_print()
        raise SyntaxError(
            f"Expected a statement, but got {token.type} "
            f"at line {token.line}, column {token.column}"
        )

    def parse_assignment(self, expect_semicolon=True):
        name_token = self.current_token()
        self.expect("IDENTIFIER")
        operator_token = self.current_token()

        if operator_token.type in assignment_operators:
            self.expect(operator_token.type)
            value = self.parse_expression()
            if expect_semicolon:
                self.expect("SEMICOLON")
            return {
                "kind": "assignment",
                "name": name_token.value,
                "operator": operator_token.value,
                "value": value,
            }

        if operator_token.type in increment_operators:
            self.expect(operator_token.type)
            if expect_semicolon:
                self.expect("SEMICOLON")
            return {
                "kind": "increment",
                "name": name_token.value,
                "operator": operator_token.value,
            }

        raise SyntaxError(
            f"Expected an assignment after '{name_token.value}', "
            f"but got {operator_token.type} "
            f"at line {operator_token.line}, column {operator_token.column}"
        )

    def parse_block(self):
        open_token = self.current_token()
        self.expect("LBRACE")
        statements = []
        while self.current_token().type != "RBRACE":
            if self.current_token().type == "EOF":
                raise SyntaxError(
                    f"Expected RBRACE to close the block opened "
                    f"at line {open_token.line}, column {open_token.column}"
                )
            statements.append(self.parse_statement())
        self.expect("RBRACE")
        return statements

    def parse_for(self):
        self.expect("FOR")
        self.expect("LPAREN")
        init = self.parse_variable_declaration()
        condition = self.parse_expression()
        self.expect("SEMICOLON")
        update = self.parse_assignment(expect_semicolon=False)
        self.expect("RPAREN")
        body = self.parse_block()

        return {
            "kind": "for",
            "init": init,
            "condition": condition,
            "update": update,
            "body": body,
        }

    def parse_while(self):
        self.expect("WHILE")
        self.expect("LPAREN")
        condition = self.parse_expression()
        self.expect("RPAREN")
        body = self.parse_block()

        return {"kind": "while", "condition": condition, "body": body}

    def parse_if(self):
        self.expect("IF")
        self.expect("LPAREN")
        condition = self.parse_expression()
        self.expect("RPAREN")
        body = self.parse_block()

        else_body = None
        if self.current_token().type == "ELSE":
            self.expect("ELSE")
            if self.current_token().type == "IF":
                else_body = [self.parse_if()]
            else:
                else_body = self.parse_block()

        return {
            "kind": "if",
            "condition": condition,
            "body": body,
            "else_body": else_body,
        }

    def parse_print(self):
        print_token = self.current_token()
        self.expect(print_token.type)
        self.expect("LPAREN")

        value = None
        if print_token.type == "PRINT" or self.current_token().type != "RPAREN":
            value = self.parse_expression()

        self.expect("RPAREN")
        self.expect("SEMICOLON")
        return {
            "kind": "print",
            "newline": print_token.type == "PRINTLN",
            "value": value,
        }

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
            "kind": "declaration",
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
        if token.type == "IDENTIFIER":
            self.expect("IDENTIFIER")
            return {"kind": "identifier", "name": token.value}
        if token.type not in value_tokens:
            raise SyntaxError(
                f"Expected a value, but got {token.type} "
                f"at line {token.line}, column {token.column}"
            )
        self.expect(token.type)
        return {"kind": "literal", "type": token.type, "value": token.value}

    def parse_unary(self):
        token = self.current_token()
        if token.type in unary_operators:
            self.expect(token.type)
            operand = self.parse_unary()
            return {"kind": "unary", "operator": token.type, "operand": operand}
        return self.parse_value()

    def parse_term(self):
        node = self.parse_unary()
        while self.current_token().type in higher_precedence_arithmetic_operators:
            operator = self.current_token().type
            self.expect(operator)
            right = self.parse_unary()
            node = {
                "kind": "binary",
                "operator": operator,
                "left": node,
                "right": right,
            }
        return node

    def parse_additive(self):
        node = self.parse_term()
        while self.current_token().type in lower_precedence_arithmetic_operators:
            operator = self.current_token().type
            self.expect(operator)
            right = self.parse_term()
            node = {
                "kind": "binary",
                "operator": operator,
                "left": node,
                "right": right,
            }
        return node

    def parse_comparison(self):
        node = self.parse_additive()
        while self.current_token().type in comparison_operators:
            operator = self.current_token().type
            self.expect(operator)
            right = self.parse_additive()
            node = {
                "kind": "binary",
                "operator": operator,
                "left": node,
                "right": right,
            }
        return node

    def parse_logical(self):
        node = self.parse_comparison()
        while self.current_token().type in logical_operators:
            operator = self.current_token().type
            self.expect(operator)
            right = self.parse_comparison()
            node = {
                "kind": "binary",
                "operator": operator,
                "left": node,
                "right": right,
            }
        return node

    def parse_expression(self):
        return self.parse_logical()


operator_symbols = {
    "PLUS": "+",
    "MINUS": "-",
    "STAR": "*",
    "SLASH": "/",
    "PERCENT": "%",
    "LESS": "<",
    "GREATER": ">",
    "LESS_EQUAL": "<=",
    "GREATER_EQUAL": ">=",
    "EQUAL_EQUAL": "==",
    "NOT_EQUAL": "!=",
    "AND": "AND",
    "OR": "OR",
    "NOT": "NOT",
}


def format_expression(node):
    if node["kind"] == "literal":
        return node["value"]

    if node["kind"] == "identifier":
        return node["name"]

    if node["kind"] == "unary":
        operand = format_expression(node["operand"])
        if node["operand"]["kind"] == "binary":
            operand = f"({operand})"
        return f"{operator_symbols[node['operator']]} {operand}"

    left = format_expression(node["left"])
    right = format_expression(node["right"])
    if node["left"]["kind"] == "binary":
        left = f"({left})"
    if node["right"]["kind"] == "binary":
        right = f"({right})"
    return f"{left} {operator_symbols[node['operator']]} {right}"


def print_statement(statement, indent=0):
    padding = "    " * indent

    if statement["kind"] == "if":
        print(f"{padding}if {format_expression(statement['condition'])}")
        for inner in statement["body"]:
            print_statement(inner, indent + 1)
        if statement["else_body"] is not None:
            print(f"{padding}else")
            for inner in statement["else_body"]:
                print_statement(inner, indent + 1)
        return

    if statement["kind"] == "for":
        print(f"{padding}for {format_expression(statement['condition'])}")
        print(f"{padding}  init:   ", end="")
        print_statement(statement["init"])
        print(f"{padding}  update: ", end="")
        print_statement(statement["update"])
        for inner in statement["body"]:
            print_statement(inner, indent + 1)
        return

    if statement["kind"] == "while":
        print(f"{padding}while {format_expression(statement['condition'])}")
        for inner in statement["body"]:
            print_statement(inner, indent + 1)
        return

    statement = dict(statement)
    if statement.get("value") is not None:
        statement["value"] = format_expression(statement["value"])
    print(f"{padding}{statement}")


if __name__ == "__main__":
    from lexer import tokens

    parser = Parser(tokens)
    try:
        while parser.current_token().type != "EOF":
            statement = parser.parse_statement()
            print_statement(statement)
    except SyntaxError as error:
        print(f"Syntax error: {error}")
