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
* [ ] Parse expressions
* [ ] Parse arithmetic operators
* [ ] Parse comparison operators
* [ ] Parse logical operators
* [ ] Parse assignments
* [ ] Parse `if`
* [ ] Parse `else`
* [ ] Parse `while`
* [ ] Parse `for`
* [ ] Parse functions
* [ ] Parse function parameters
* [ ] Parse explicit function return types
* [ ] Parse `return`
* [ ] Parse function calls
* [ ] Improve parser error handling
* [ ] Add EOF handling

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
* [ ] Detect invalid assignments
* [ ] Check function arguments
* [ ] Check function return types
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
