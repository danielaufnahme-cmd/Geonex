import os


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

            if word == "string":
                kind = "STRING_TYPE"
            else:
                kind = "IDENTIFIER"

            tokens.append(Token(kind, word, start_line, start_column))

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
