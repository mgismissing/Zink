# Syntax

Follows the entire Zink syntax and some examples.

## Line continuation

Line continuations are used to tell the parser that the line where the line continuation character `\` is and the one below it should be joined together.

## Strings

Zink allows for 3 types of strings: the normal string `"hello"`, byte strings `b"hello"` and regex strings `r"myregex"`.

## Raw strings

Zink also allows to include snippets of code that will be converted as-is: raw strings ```print("Hello, World!")```. They can be either alone as statements or inside expressions.

## Numbers

Numbers can be integers `10`, decimals `0.10` (or abbreviated `.10`), hexadecimal `0x10` or binary `0b10`. Any number of underscores are allowed anywhere in between, at the start and at the end `_1__0__` &rarr; `10`.

## Line endings

Lines can be terminated with a newline character (pressing `Enter` on the keyboard to insert `LF`) or with a semicolon `;` used to concatenate multiple lines on the same one. Only one is required at the end of a line, not both (putting a semicolon and pressing `Enter` should be avoided to prevent confusion).

## Program

A Zink program is made of statements (expressions are also statements).

## Naming convention

Variables must start with an uppercase or lowercase letter (A-Z) or with an underscore and can also contain numbers. Examples of this are `myVar`, `myVar2`, `My_Var_2`. This `2_myVar` is not allowed.