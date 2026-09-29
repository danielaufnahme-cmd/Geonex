import sys
from compiler.lexer import lex
from compiler.parser import Parser, print_statement


def compile_file(gnx_file):
    source = open(gnx_file, "r").read()

    lexer_output = lex(source)

    parser = Parser(lexer_output)

    while parser.current_token().type != "EOF":
        statement = parser.parse_statement()
        print_statement(statement)


try:
    gnx_file = sys.argv[1]
    compile_file(gnx_file)
except IndexError:
    print("GEONEX: no file to compile given")
