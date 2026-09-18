# Geonex

Geonex is a programming language designed to combine the readability of Python with the structure and performance-oriented design of languages such as Java and C++.

The goal of Geonex is to provide a simple, readable syntax while still being suitable for building real software.

## Project Status

Geonex is currently in early development.

The lexer has been implemented and the parser is currently being developed. The language can already recognize and parse basic values, types, operators, and variable declarations.

This project is not production-ready yet.

## Current Features

* Integer values
* Floating-point values
* String values
* Boolean values
* Variable declarations
* Basic operators
* `if` / `else` syntax support in the lexer
* `while` and `for` syntax support in the lexer
* Function-related keywords
* Line and column information for tokens
* Syntax error reporting

Example:

```gnx
int age = 14;
float height = 1.80;
string name = "Daniel";
bool active = true;
```

## Language Goals

Geonex is being designed with the following goals:

* Readable syntax
* Simple language design
* Predictable behavior
* Good performance
* Automatic memory management
* A useful standard library
* Cross-platform support
* Interoperability with existing libraries where practical
* A language and toolchain that can eventually become largely self-hosted

## Example

A basic Geonex program is intended to look like this:

```gnx
int age = 14;
string name = "Daniel";

if (age >= 13) {
    println("Hello " + name);
}
```

The syntax is still being developed, so examples may change as the language evolves.

## Development

Geonex is currently being developed from the ground up.

The current development process includes:

1. Lexer
2. Parser
3. Abstract Syntax Tree
4. Semantic analysis
5. Code generation / runtime
6. Standard library
7. Tooling
8. Self-hosting

The architecture and order of these stages may change as development continues.

## Building

Geonex is currently a development project and does not yet have a stable installation or build system for end users.

To work on the project, clone the repository and follow the development files and examples included in the repository.

## Contributing

Geonex is currently primarily a personal development project, but contributions, ideas, bug reports, and discussions may be welcome as the project develops.

Before contributing major changes, please open an issue to discuss the proposed change.

## License

Geonex is licensed under the Apache License 2.0.

See the `LICENSE` file for the complete license text.

## Disclaimer

Geonex is experimental software and is provided for development and educational purposes. It is not currently intended for production use.

## Roadmap

* [x] Initial lexer
* [x] Token types
* [x] Basic value parsing
* [ ] Complete parser
* [ ] Abstract Syntax Tree
* [ ] Expression parsing
* [ ] Assignment parsing
* [ ] `if` / `else`
* [ ] `while`
* [ ] `for`
* [ ] Functions
* [ ] Function calls
* [ ] Semantic analysis
* [ ] Type checking
* [ ] Code generation
* [ ] Runtime / virtual machine
* [ ] Standard library
* [ ] Self-hosting

## About

Geonex is being built as an independent programming language project with the long-term goal of becoming a complete, usable programming language and development ecosystem.
