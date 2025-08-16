# Zink
Zink is a programming language that simplifies scripting with many tweaks and additions.

## Why Zink and not other languages?
One of the problems developers face when writing in other languages is that it can sometimes be very complex to write simple expressions, like for example iterating through a list while also getting the current item's position in that list in Python, which uses the `enumerate` function.

Zink simplifies these kinds of operations by letting the developer write shorter code and still converting it to the correct functions.

## Quick comparison
This Python script determines if a number is prime:

```py
def is_prime(n: int) -> bool:
    if n <= 1: return False
    if n <= 3: return True
    if n % 2 == 0 or n % 3 == 0: return False

    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True
```

This here is that same code written in Zink:

```zink
def is_prime(n: int): bool
    if n <= 1; <-False;.
    if n <= 3; <-True;.
    if n % 2 == 0 or n % 3 == 0; <-False;.

    i = 5
    while i * i <= n
        if n % i == 0 or n % (i + 2) == 0
            <-False
        .
        i += 6
    .
    <-True
.
```

It may seem stupid (and longer), but now look at Python classes:

```py
class Animal:
    def __init__(self, name: str) -> None:
        self.name = name
    def eat(self, food: str) -> None:
        print(self.name, "is eating", food)

class Bird(Animal):
    def __init__(self, name: str, color: str) -> None:
        super().__init__(name=name)
        self.color = color
    def fly(self) -> None:
        print(self.color, self.name, "is flying")
```

And look at those same classes in Zink:

```zink
class Animal
    /init @name: str;;.
    def eat(@, food: str): None
        print(@.name, "is eating", food)
    .
.

class Bird from Animal
    /init ^name: str, @color: str;;.
    def fly(@): None
        print(@.color, @.name, "is flying")
    .
.
```

You can start to notice that it simplifies many things that require a lot of time to type: it replaces entire lines spent typing `self.foo = foo` to simply putting a `@` before the argument, or automatically passing those arguments to the `super().__init__` function with `^`. In fact, that very function is abbreviated to `@^`.

Getting the length of an object is as easy as typing `#` before the object, and converting an object to a type is done with the repurposed keyword `as`.

## Language support
Zink is also built with the idea of writing the same code while still converting it to many languages, like for example writing the source code in Zink and then converting it to both Python and Ruby.