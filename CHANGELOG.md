# Changelog

All notable changes to Geonex will be documented in this file.

The format is based on Keep a Changelog.

## [Unreleased]

### Added

* Initial Geonex lexer
* Token system
* Integer values
* Floating-point values
* String values
* Boolean values
* Basic variable declarations
* Basic operators
* Syntax error reporting
* Line and column information for tokens
* `//` and `/* */` comments
* Initial parser
* Expressions with operator precedence and parentheses
* Logical operators `&&`, `||` and `!`
* Assignments
* `if` / `else if` / `else`
* `while`
* `for`
* `print` / `println`
* Function declarations with explicit return types and typed parameters
* `return` with a value
* Function calls as statements

### Changed

Language decisions documented in `README.md` and `ROADMAP.md`:

* Variables can be declared without a value (`int x;`)
* A variable keeps its declared type; assigning a value of another type is a type error
* Functions can return `void`, and `void` functions may use `return;`
* Global variables must be marked with `global`
* Boolean logic uses `&&`, `||` and `!`, not `and`, `or` and `not`
* Conditions must be `bool`; there is no truthiness
* Imports end with a semicolon: `import math;`, `import earnings.json;`, `import py.math;`
* `const`, arrays, `char`, objects/classes and other-language interoperability are planned for later

### Known Issues

* The lexer still accepts `and`, `or` and `not`
* `int x;` (declaration without a value) is rejected
* `y += 5;` and `y++;` are rejected as statements; they only work in a `for` update
* `void` functions and `return;` are rejected
* A function call inside an expression fails (`int x = add(5, 10);`) because the call consumes the `;`; this also stops `examples/hello.gnx` from parsing
* Function arguments are not required to be separated by commas (`add(5 6);` is accepted)
* A file ending right after a type (`int`) crashes with a Python `IndexError` instead of a syntax error
* The lexer reads `examples/hello.gnx` whenever it is imported

### In Progress

* Started Abstract Syntax Tree
* Functions: `void`, `return;` and calls inside expressions
* Function calls

### Planned

* `global` variables
* Imports
* Semantic analysis
* Type checking
* Code generation
* Runtime / virtual machine
* Standard library
* Self-hosting

## Version History

Geonex has not reached its first official release yet.
