# Geonex

Geonex is a programming language designed to combine the readability of Python with the structure and performance-oriented design of languages such as Java and C++.

The goal of Geonex is to provide a simple, readable syntax while still being suitable for building real software.

## Project Status

Geonex is currently in early development.

The lexer has been implemented and the parser is currently being developed. The parser can already recognize variable declarations, assignments, expressions, conditions, loops, printing, function declarations and function-call statements.

Several language decisions have been made that the parser does not support yet. They are listed under [Language Design](#language-design) and tracked in [`ROADMAP.md`](ROADMAP.md).

There is no AST, semantic analysis or runtime yet, so Geonex programs can be parsed but not run.

This project is not production-ready yet.

## Current Features

What the lexer and parser handle today:

* Integer, floating-point, string and boolean values
* Variable declarations with a value (`int age = 14;`)
* Assignments (`age = 15;`)
* Arithmetic operators: `+` `-` `*` `/` `%`
* Comparison operators: `==` `!=` `<` `>` `<=` `>=`
* Logical operators: `&&` `||` `!`
* Operator precedence and parentheses
* `if` / `else if` / `else`
* `while`
* `for` (`for (int i = 0; i < 10; i++)`)
* `print` and `println`
* Function declarations with an explicit return type and typed parameters
* `return` with a value
* Function calls as statements (`add(5, 10);`)
* `//` and `/* */` comments
* Line and column information for tokens
* Syntax error reporting with line and column

Example:

```gnx
int age = 14;
float height = 1.80;
string name = "Daniel";
bool active = true;
```

## Language Design

These are the decisions that have been made for the language so far. Items marked **not implemented yet** are decided but not yet supported by the compiler.

### Variables

Every variable has a fixed declared type: `int`, `float`, `string` or `bool`.

A variable does not have to be given a value when it is declared.

```gnx
int x;          // valid: declared without a value
int y = 5;      // valid
x = 10;         // valid
x = "hello";    // type error: x is an int
```

Geonex does not use Python-style dynamic types. A variable keeps the type it was declared with.

* Declaring without a value (`int x;`): **not implemented yet**
* Rejecting values of the wrong type: belongs to type checking, **not implemented yet**

### Functions

Functions have explicit return types. `void` means the function returns nothing.

```gnx
int add(int a, int b) {
    return a + b;
}

void sayHello() {
    println("Hello");
}
```

A `void` function may use `return;` to exit early. A non-void function must return a value of its return type; this is checked during semantic analysis, not by the parser.

A function call can be used as a statement or inside an expression:

```gnx
add(5, 10);
int result = add(5, 10);
println(add(5, 10));
return add(5, 10);
```

* `void` return type: **not implemented yet**
* `return;` without a value: **not implemented yet**
* Function calls inside expressions: **not implemented yet**
* Checking return types and arguments: belongs to semantic analysis, **not implemented yet**

### Global variables

Global variables must be marked with `global`. A variable is not global unless it is marked.

```gnx
global int y = 20;
```

The exact scope and shadowing rules have not been decided yet.

* `global`: **not implemented yet**

### Boolean logic

Geonex uses symbols for boolean logic:

```gnx
if (x == 5 && y > 2) {
    println("valid");
}

if (!done || ready) {
    println("continue");
}
```

`and`, `or` and `not` are not Geonex operators.

* `&&`, `||` and `!` are implemented. The lexer still accepts `and`, `or` and `not`; these are to be removed.

### Conditions

Geonex does not use Python-style truthiness. A condition must be a `bool`.

```gnx
bool ready = true;
int count = 3;

if (ready) { }   // valid
if (count) { }   // error: count is an int, not a bool
```

* Rejecting non-boolean conditions: belongs to type checking, **not implemented yet**

### Imports

Geonex will support several kinds of imports. Each import ends with a semicolon.

```gnx
import math;            // Geonex module (no .gnx extension needed)
import earnings.json;   // data file
import py.math;         // Python module, through the py namespace
```

More data formats (and Python libraries such as `py.numpy` or `py.pandas`) may be supported later. How Python code is run from Geonex has not been decided yet.

* Imports: **not implemented yet**

### Planned for later

These are intentionally not part of the language yet:

* `const`
* Arrays
* `char`
* Objects / classes (the keyword has not been chosen)
* Interoperability with languages other than Python

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

A basic Geonex program looks like this:

```gnx
int add(int a, int b) {
    return a + b;
}

int age = 14;
string name = "Daniel";
bool member = true;

if (age >= 13 && member) {
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
4. Semantic analysis and type checking
5. Code generation / runtime (planned: Geonex bytecode running on the Geonex Virtual Machine, GVM)
6. Standard library
7. Tooling
8. Self-hosting

The architecture and order of these stages may change as development continues.

## Building

Geonex is currently a development project and does not yet have a stable installation or build system for end users.

To work on the project, clone the repository and follow the development files and examples included in the repository.

To parse a Geonex file and print the parsed statements:

```sh
python geo.py path/to/file.gnx
```

## Contributing

Geonex is currently primarily a personal development project, but contributions, ideas, bug reports, and discussions may be welcome as the project develops.

Before contributing major changes, please open an issue to discuss the proposed change.

## License

Geonex is licensed under the Apache License 2.0.

See the `LICENSE` file for the complete license text.

## Disclaimer

Geonex is experimental software and is provided for development and educational purposes. It is not currently intended for production use.

## Roadmap

A short summary. See [`ROADMAP.md`](ROADMAP.md) for the full roadmap.

* [x] Initial lexer
* [x] Token types
* [x] Basic value parsing
* [x] Expression parsing
* [x] Assignment parsing
* [x] `if` / `else`
* [x] `while`
* [x] `for`
* [ ] Functions (declarations work; `void` and `return;` are missing)
* [ ] Function calls (statement calls work; calls inside expressions do not)
* [ ] `global` variables
* [ ] Imports
* [ ] Complete parser
* [ ] Abstract Syntax Tree
* [ ] Semantic analysis
* [ ] Type checking
* [ ] Code generation
* [ ] Runtime / virtual machine
* [ ] Standard library
* [ ] Self-hosting

## About

Geonex is being built as an independent programming language project with the long-term goal of becoming a complete, usable programming language and development ecosystem.
