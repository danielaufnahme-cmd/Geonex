# Geonex Roadmap

This roadmap describes the planned development of Geonex.

The roadmap may change as the language develops.

## Phase 1 — Lexer

* [x] Create lexer
* [x] Create token system
* [x] Add keywords
* [x] Add operators
* [x] Add punctuation
* [x] Add identifiers
* [x] Add integers
* [x] Add floats
* [x] Add strings
* [x] Add booleans
* [x] Add line and column tracking
* [x] Add basic lexer error handling
* [x] Add `//` and `/* */` comments
* [x] Add `&&`, `||` and `!` operators
* [ ] Remove the `and`, `or` and `not` keywords (Geonex uses `&&`, `||`, `!`)
* [ ] Add the `void` keyword
* [ ] Add the `global` keyword
* [ ] Add the `import` keyword
* [ ] Stop the lexer from reading `examples/hello.gnx` when it is imported

## Phase 2 — Parser

* [x] Create parser
* [x] Parse type declarations
* [x] Parse variable names
* [x] Parse assignment operator
* [x] Parse integer values
* [x] Parse float values
* [x] Parse string values
* [x] Parse boolean values
* [x] Parse semicolons
* [x] Parse expressions
* [x] Parse arithmetic operators
* [x] Parse comparison operators
* [x] Parse logical operators
* [x] Parse `!`
* [x] Parse assignments (`x = 10;`)
* [ ] Parse variable declarations without a value (`int x;`)
* [ ] Parse compound assignments as statements (`y += 5;`); today they only work in a `for` update
* [ ] Parse `++` / `--` as statements (`y++;`); today they only work in a `for` update
* [x] Parse `if`
* [x] Parse `else`
* [x] Parse `else if`
* [x] Parse `while`
* [x] Parse `for`
* [x] Parse `print` / `println`
* [x] Parse function declarations
* [x] Parse function parameters
* [x] Parse explicit function return types (`int`, `float`, `string`, `bool`)
* [ ] Parse the `void` return type
* [x] Parse `return` with a value
* [ ] Parse `return;` without a value
* [x] Parse function calls as statements (`add(5, 10);`)
* [ ] Parse function calls inside expressions (`int x = add(5, 10);`, `println(add(5, 10));`, `return add(5, 10);`); the call currently consumes the statement's `;`
* [ ] Require commas between function arguments (`add(5 6);` is currently accepted)
* [ ] Parse `global` variable declarations (`global int y = 20;`)
* [ ] Parse imports (`import math;`, `import earnings.json;`, `import py.math;`)
* [x] Improve parser error handling
* [x] Add EOF handling
* [ ] Report a syntax error instead of crashing when a file ends right after a type (`int` alone raises a Python `IndexError`)

## Phase 3 — Abstract Syntax Tree

* [ ] Create AST architecture
* [ ] Create variable declaration nodes
* [ ] Create literal nodes
* [ ] Create identifier nodes
* [ ] Create binary expression nodes
* [ ] Create unary expression nodes
* [ ] Create assignment nodes
* [ ] Create conditional nodes
* [ ] Create loop nodes
* [ ] Create function declaration nodes
* [ ] Create function call nodes
* [ ] Create return nodes
* [ ] Create program/root node

## Phase 4 — Semantic Analysis

* [ ] Create semantic analyzer
* [ ] Implement symbol tables
* [ ] Implement variable scope
* [ ] Implement type checking
* [ ] Detect undefined variables
* [ ] Detect invalid assignments (a variable keeps its declared type: `int x = 5; x = "hello";` is an error)
* [ ] Require `bool` conditions in `if`, `while` and `for` (no truthiness)
* [ ] Check function arguments
* [ ] Check function return types
* [ ] Check that non-void functions return a value
* [ ] Allow `return;` only in `void` functions
* [ ] Implement `global` variables (scope rules still to be decided)
* [ ] Detect invalid operations
* [ ] Improve semantic error messages

## Phase 5 — Execution

* [ ] Decide final execution architecture
* [ ] Design Geonex runtime
* [ ] Design memory management
* [ ] Implement runtime values
* [ ] Implement execution of expressions
* [ ] Implement execution of statements
* [ ] Implement function execution
* [ ] Implement standard runtime functionality
* [ ] Import Geonex modules (`import math;` finds `math.gnx`)
* [ ] Import data files (`import earnings.json;`)
* [ ] Import Python modules through the `py` namespace (`import py.math;`)

## Phase 6 — Standard Library

* [ ] Create standard library structure
* [ ] String utilities
* [ ] Math utilities
* [ ] File handling
* [ ] Input/output
* [ ] Collections
* [ ] Useful system functionality

## Phase 7 — Tooling

* [ ] Geonex command-line interface
* [ ] Geonex formatter
* [ ] Better error messages
* [ ] Project/package system
* [ ] Documentation tooling
* [ ] Testing framework
* [ ] Language server
* [ ] Editor integration

## Phase 8 — Cross-Platform Support

* [ ] Linux
* [ ] macOS
* [ ] Windows

## Phase 9 — Self-Hosting

* [ ] Implement more Geonex tooling in Geonex
* [ ] Implement Geonex standard library in Geonex where practical
* [ ] Begin implementing compiler/runtime components in Geonex
* [ ] Build Geonex using Geonex
* [ ] Reduce dependence on the original implementation

## Phase 10 — Stable Release

* [ ] Finalize language specification
* [ ] Stabilize syntax
* [ ] Stabilize standard library
* [ ] Complete documentation
* [ ] Comprehensive test suite
* [ ] Performance testing
* [ ] Security review
* [ ] Release candidate
* [ ] Geonex 1.0

## Future Language Features

Planned, but intentionally not part of the language yet:

* [ ] `const`
* [ ] Arrays
* [ ] `char`
* [ ] Objects / classes (keyword not chosen yet)
* [ ] More data-file formats for imports
* [ ] Interoperability with languages other than Python

## Open Design Decisions

These need a decision before they can be implemented:

* Scope and shadowing rules for `global` variables, e.g. whether a local variable may have the same name as a global
* Whether `global` declarations and imports may appear only at the top of a file or anywhere
* How `import a.b;` is told apart: a data file (`earnings.json`) or a nested module
* How Python modules are loaded and called at runtime
* Whether Geonex has a unary minus (`int z = -5;` is not accepted today)
