import os

dictionary = {"string": "STRING_TYPE", "int": "INT_TYPE", "float": "FLOAT_TYPE"}
operators = {"+": "PLUS", "-": "MINUS", "*": "STAR", "/": "SLASH", "%": "PERCENT"}
two_digit_operators = {
    "==": "EQUAL_EQUAL",
    "!=": "NOT_EQUAL",
    "<=": "LESS_EQUAL",
    ">=": "GREATER_EQUAL",
    "&&": "AND",
    "||": "OR",
    "+=": "PLUS_EQUALS",
    "-=": "MINUS_EQUALS",
    "*=": "STAR_EQUALS",
    "/=": "SLASH_EQUALS",
    "++": "PLUS_PLUS",
    "--": "MINUS_MINUS",
}


class Token:
    def __init__(self, type, value, line, column):
        self.type = type
        self.value = value
        self.line = line
        self.column = column


path = os.path.join(os.path.dirname(__file__), "..", "examples", "hello.gnx")
with open(path) as f:
    source = f.read()


def lex(source):
    tokens = []
    i = 0
    line = 1
    column = 1
    start_line = 1
    start_column = 1

    while i < len(source):
        if source[i].isalpha():
            word = ""
            start_line = line
            start_column = column

            while i < len(source) and source[i].isalnum():
                word += source[i]
                i += 1
                column += 1

            if word in dictionary:
                kind = dictionary.get(word)
            else:
                kind = "IDENTIFIER"

            tokens.append(Token(kind, word, start_line, start_column))

        elif source[i].isdigit():
            word = ""
            start_line = line
            start_column = column
            is_float = False

            while i < len(source):
                if source[i].isdigit():
                    word += source[i]
                elif source[i] == ".":
                    if is_float:
                        raise Exception(
                            f"Second '.' in number at line {line}, column {column}"
                        )
                    is_float = True
                    word += source[i]
                else:
                    break

                i += 1
                column += 1

            if word.endswith("."):
                raise Exception(
                    f"Number ends with '.' at line {start_line}, column {start_column}"
                )

            if is_float:
                kind = "FLOAT"
            else:
                kind = "INT"

            tokens.append(Token(kind, word, start_line, start_column))

        elif i + 1 < len(source) and source[i] + source[i + 1] in two_digit_operators:
            two = source[i] + source[i + 1]
            tokens.append(Token(two_digit_operators[two], two, line, column - 1))
            i += 2
            column += 2

        elif source[i] in operators:
            tokens.append(Token(operators[source[i]], source[i], line, column))
            i += 1
            column += 1

        elif source[i] == "=":
            tokens.append(Token("EQUALS", "=", line, column))
            i += 1
            column += 1

        elif source[i] == ";":
            tokens.append(Token("SEMICOLON", ";", line, column))
            i += 1
            column += 1

        elif source[i] == '"':
            start = column
            word = ""
            i += 1
            column += 1

            while i < len(source) and source[i] != '"':
                word += source[i]
                i += 1
                column += 1

            i += 1
            column += 1

            tokens.append(Token("STRING", word, line, start))

        elif source[i] == "\n":
            line += 1
            column = 1
            i += 1

        elif source[i].isspace():
            column += 1
            i += 1

        else:
            raise Exception(
                f"Unknown character {source[i]!r} at line {line}, column {column}"
            )

    return tokens


tokens = lex(source)

for token in tokens:
    print(f"{token.type} {token.value!r} line {token.line} col {token.column}")
