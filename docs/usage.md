# Usage

Zink can be either directly called from the command line or imported and used in a python file.

# Command line

Running the command `z` (or `python -m zlang`) starts the REPL that, given valid Zink syntax, will return and execute the Python equivalent.

# Usage in Python

Zink exposes all of its API through python's `import`.

## Parsing Zink

To parse Zink code and pass it to a built-in translator:

```py
from zlang import ZinkLexer, ZinkParser
from zlang.translators import _py

def parse(s: str) -> str:
    lexer, parser = ZinkLexer(), ZinkParser()
    translator = _py()
    return translator(parser.parse(lexer.tokenize(s)))
```

## Creating a custom translator

Zink also exposes all its built-in translators in the form of classes, so creating and using a custom translator is as easy as inheriting their class methods. It is recommended to use the `py` translator instead of using the `t` one.

Handlers are defined as functions preceded by an underscore.

In this example, we're going to modify Zink's `True` and `False` to convert them to `1` and `0`:

```py
from zlang.translators import _py

class mylang(_py):
    def _TRUE(self): return "1"
    def _FALSE(self): return "0"
```

We can then plug this into our `parse` function, that will return a list of lines:

```py
from zlang import ZinkLexer, ZinkParser

# include the code from above here
# ================================

def parse(s: str) -> list[str]:
    lexer, parser = ZinkLexer(), ZinkParser()
    translator = mylang()
    #            ^^^^^^ notice mylang instead of _py
    return translator(parser.parse(lexer.tokenize(s)))
```

Testing our code:

```py
print(parse("True\n")[0])  # 1
print(parse("False\n")[0]) # 0
```