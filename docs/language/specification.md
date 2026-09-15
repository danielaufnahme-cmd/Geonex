# Geonex Language Specification

## Overview

Geonex is a statically typed programming language designed to be
readable and easier to use than C++ and Java while still providing
strong performance.

Geonex programs are compiled into Geonex bytecode and executed by
the Geonex Virtual Machine (GVM).

## Execution Model

Geonex source
    ↓
Compiler
    ↓
Geonex bytecode
    ↓
GVM
    ↓
Operating system

## Variables

int age = 14;
string name = "Daniel";
float height = 1.80;
bool isFlying = true;

## Printing

print("Hello");
println("Hello");

## Conditions

if (condition) {
    // code
} else {
    // code
}

## Loops

for (int i = 0; i < 10; i++) {
    println(i);
}

while (condition) {
    // code
}

## Functions

int add(int a, int b) {
    return a + b;
}
