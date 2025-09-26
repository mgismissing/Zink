# Syntax

Follows the entire Zink syntax and some examples.

## Line continuation

Line continuations are used to tell the parser that the line where the line continuation character `\` is and the one below it should be joined together.

## Strings

Zink allows for 3 types of strings: the normal string `"hello"`, byte strings `b"hello"` and regex strings `r"myregex"`.

## Raw strings

Zink also allows to include snippets of code that will be converted as-is: raw strings ``` `print("Hello, World!")` ```. They can be either alone as statements or inside expressions.

## Numbers

Numbers can be integers `10`, decimals `0.10` (or abbreviated `.10`), hexadecimal `0x10` or binary `0b10`. Any number of underscores are allowed anywhere in between, at the start and at the end (`_1__0__` &rarr; `10`).

## Line endings

Lines can be terminated with a newline character (pressing `Enter` on the keyboard to insert `LF`) or with a semicolon `;` used to concatenate multiple lines on the same one. Only one is required at the end of a line, not both (putting a semicolon and pressing `Enter` should be avoided to prevent confusion).

## Program

A Zink program is made of statements (expressions are also statements).

## Naming convention

Variables must start with an uppercase or lowercase letter (A-Z) or with an underscore and can also contain numbers. Examples of this are `myVar`, `myVar2`, `My_Var_2`. This `2_myVar` is not allowed.

## Assignment

Variable assignment works exactly like in Python, where a variable `a` or a group of them `a, b, c` can be assigned to a value `= 1` or multiple of them `= 1, 2, 3`. Variables can also be scoped with the dedicated keywords `local`, `!local` and `global`.

## Compound assignment

In some cases, assignment can be abbreviated with a compound assignment operator. Here is a list of the normal assignment compared to the compound one:

| Normal            | Compound  |
|-------------------|-----------|
| `a = a + b`       | `a += b`  |
| `a = a - b`       | `a -= b`  |
| `a = a * b`       | `a *= b`  |
| `a = a / b`       | `a /= b`  |
| `a = a . b`       | `a .= b`  |
| `a = a % b`       | `a %= b`  |
| `a = a ** b`      | `a **= b` |
| `a = a // b`      | `a //= b` |
| `a = a @ b`       | `a @= b`  |
| `a = a & b`       | `a &= b`  |
| `a = a \| b`      | `a \|= b` |
| `a = a ^ b`       | `a ^= b`  |
| `a = ~ a`         | `a ~`     |
| `a = a << b`      | `a <<= b` |
| `a = a >> b`      | `a >>= b` |
| `self.a = a`      | `@<-a`    |
| `a = a .. b`      | `a ..= b` |
| `a = b(a)`        | `a to b`  |
| `a = b.pop()`     | `{b}->a`  |
| `a = b.pop(c)`    | `{b:c}->a`|
| `a.append(b)`     | `{a}<-b`  |
| `a.insert(b, c)`  | `{a:b}<-c`|

## General statements

These statements are made up of a keyword and can be followed by an expression. Here is a list of them:

| Name                  | Description                                                               |
|-----------------------|---------------------------------------------------------------------------|
| `assert a`            | Raises `AssertionError` if `a` is falsy.                                  |
| `raise a`             | Raises `a`.                                                               |
| `use a`               | Imports the module named `a`.                                             |
| `use a as b`          | Imports the module named `a` as `b`.                                      |
| `use a from b`        | Imports `a` from the module named `b`.                                    |
| `use a as b from c`   | Imports `a` as `c` from the module named `c`.                             |
| `pass`                | Doesn't do anything.                                                      |
| `next`                | Skips to the next iteration in a loop.                                    |
| `break`               | Exits out of the current loop.                                            |
| `global a`            | Specifies that the global `a` should be used.                             |
| `global a = b`        | Assigns `b` to the global `a`.                                            |
| `!local a`            | Specifies that the nonlocal `a` should be used.                           |
| `!local a = b`        | Assigns `b` to the nonlocal `a`.                                          |
| `local a`             | Specifies that the local `a` should be used.                              |
| `local a = b`         | Assigns `b` to the local `a`.                                             |
| `<-`                  | Returns `None`.                                                           |
| `<-a`                 | Returns `a`.                                                              |
| `del a`               | Deletes `a`.                                                              |
| `<\|a`                | Prints `a`.                                                               |
| `@a`                  | Decorates a function with the decorator `a`.                              |

## Loops, conditional branches and error catching

### While loop

```zink
while a
    ...
.
```

### For loop

```zink
for a -> b
    ...
.
```

### Enumerated for loop

```zink
for a at b -> c
    ...
.
```

### Repetition

```zink
times x
    ...
.
```

### Repetition with count

```zink
for i to a
    ...
.
```

### Repetition with count and set start

```zink
for i from a to b
    ...
.
```

### If branch

```zink
if a
    ...
.
```

### If-else branch

```zink
if a
    ...
.else
    ...
.
```

### If-elif branch

```zink
if a
    ...
.elif b
    ...
.
```

Elif branches can be chained one after the other.

### If-elif-else branch

```zink
if a
    ...
.elif b
    ...
.else
    ...
.
```

## Error catching

### Try

When using `try` on its own, it will catch any exception.

```zink
try
    ...
.
```

### Try-catch

```zink
try
    ...
.catch a
    ...
.
```

Catches can be chained one after the other.

### Try-else

```zink
try
    ...
.else
    ...
.
```

### Try-catch-else

```zink
try
    ...
.catch a
    ...
.else
    ...
.
```

## Match and case

```zink
match a
    case b
        ...
    .
.
```

Cases can be chained one after the other.

For empty cases, use ignore instead:

```zink
match a
    ignore b
.
```

## Functions

Functions are defined like this:

```zink
def a(b: type): type
    ...
.
```

Functions can have "attributes":

```zink
=== asynchronous
def ?a(b)
    ...
.

=== method
def @a(b)
    ...
.
```

Functions can also be prefixed with one of the scoping keywords.

Dunder methods (`__add__`, `__sub__` and so on) can also be declared with this other syntax (`@` is implicit when declaring with `/`):

```zink
/add a, b, c
    ...
.
```

Except these, which instead have special names:

| Symbol    | Dunder method |
|-----------|---------------|
| `*`       | `__init__`    |
| `+`       | `__enter__`   |
| `-`       | `__exit__`    |
| `!`       | `__call__`    |

To call a function:

```zink
a(b)
```

### Anonymous functions

Some languages support defining functions without naming them. To do so in Zink, we use the `anon` keyword:

```zink
a = anon(b)
    ...
.
```

These functions can have attributes too:

```zink
=== asynchronous
a = anon?(b)
    ...
.

=== method
a = anon@(b)
    ...
.
```

## Macros

Macros are functions that don't need any argument. All function syntaxes are valid except the arguments, which are omitted:

```zink
def a: type
    ...
.
```

To call a macro:

```zink
a!
```

## Classes

```zink
class a
    ...
.
```

Classes can be prefixed with one of the scoping keywords.

## Descendants

Descendants are classes that inherit code from other classes.

```zink
class a from b
    ...
.
```

### With

```zink
with a as b
    ...
.
```

## Lists, tuples and dictionaries

### Lists

A list `[a, b, c,]` (note the comma) is defined as an expandable container for the same type of element. An example is a list of strings `list(str)` or a list of strings or numbers `list(str | int)`. An empty list is defined as `[,]`.

### Tuples

A tuple `[a, b, c]` (note the missing comma) is defined as a set-size container for different types of elements. An example is a pair of coordinates `tuple(10, 20)`. An empty tuple is defined as `[]`.

### Dictionaries

A dictionary `[a=b, c=d]` is defined as an expandable key-value container that associates a key to a value. An example is a dictionary of settings `dict(str, bool)`. An empty dict is defined as `[=]`.

## Ranges

A range can be defined in 5 total ways:
- Inclusive-Exclusive `[0 <-> 4]` &rarr; `0, 1, 2, 3, 4`;
- Inclusive-Exclusive `[0 <-> 4)` &rarr; `0, 1, 2, 3`;
- Exclusive-Inclusive `(0 <-> 4]` &rarr; `1, 2, 3, 4`;
- Exclusive-Exclusive `(0 <-> 4)` &rarr; `1, 2, 3`;
- Python default (Inclusive-Exclusive) `{0 <-> 4}` &rarr; `0, 1, 2, 3`. This one should be used as much as possible since it also allows defining ranges that by default start from `0`: `{->4}` &rarr; still `0, 1, 2, 3`.

## Incrementation and decrementation

Variables can be incremented and decremented (and also returned) before and after the operation is done:
- Increment, then return: `++a`
- Decrement, then return: `--a`
- Return, then increment: `a++`
- Return, then decrement: `a--`

## Contains operator

The contains operator `a in b` is used when it is needed to determine whether an element `a` is contained in a list, tuple or dictionary (as a key) `b`.

## Abbreviations

Many parts of programming languages can seem very long and seem to serve no purpose. These abbreviations offer a solution to that problem:

| Name              | Description                                               |
|-------------------|-----------------------------------------------------------|
| `↓a`              | Returns `a` converted to lowercase.                       |
| `↑a`              | Returns `a` converted to uppercase.                       |
| `#a`              | Returns the length of `a`.                                |
| `a?`              | Returns the type of `a`.                                  |
| `a as b`          | Returns `a` converted to `b` (`b(a)`).                    |
| `a like b`        | Returns `a` converted to the type of `b` (`type(b)(a)`).  |
| `@`               | Returns `self`.                                           |
| `^`               | Returns `super()`.                                        |
| `@^`              | Returns `super().__init__`.                               |
| `a between b, c`  | Returns `b <= a <= c`.                                    |

## Dollar

To eliminate unnecessary repetition of the same variable, the dollar `$` is used. The dollar defaults to empty and can be any expression. Here are some examples:

| Dollar            | Equivalent        |
|-------------------|-------------------|
| `a += $`          | `a += a`          |
| `a = a[b]`        | `a = $[b]`        |
| `a.b(a, c)`       | `a.b$(c)`         |

## Comments

Finally, comments need to be at the start of a line and are defined like this:

```zink
=== this is a line comment!
```

Multiline comments are still defined like line comments:

```zink
=== This is a multiline comment.
=== It spans multiple lines.
```