import sys
from compiler.lexer import lex
from compiler.parser import Parser, print_statement

gnx_file = sys.argv[1]

source = open(gnx_file, "r").read()

lexer_output = lex(source)

parser = Parser(lexer_output)

while parser.current_token().type != "EOF":
    statement = parser.parse_statement()
    print_statement(statement)
