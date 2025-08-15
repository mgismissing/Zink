from .zink import ZinkLexer, ZinkParser
from . import translators
import sys

def main():
    lexer = ZinkLexer()
    parser = ZinkParser()

    if len(sys.argv) == 1:
        lang = "py"
        print(f"WARNING: Language not specified, defaulting to \"{lang}\"")
    else:
        lang = sys.argv[1]

    try: translator: translators.T = getattr(translators, f"_{lang}")()
    except AttributeError: print(f"Missing ruleset for language \"{lang}\""); exit(3)

    def strip_paren(s):
        return str(s).removeprefix("(").removesuffix(")")
        
    def parse(s: str):
        parsed = parser.parse(lexer.tokenize(s))
        return None if parsed == None else translator(parsed, "None", 0)

    rung  = {
        "__name__": "__main__",
        "__file__": __file__,
        "__package__": None,
        "__cached__": None,
        "__doc__": None,
        "__builtins__": __builtins__
    }

    if len(sys.argv) == 3:
        with open((file := sys.argv[2]) + ".z", "r") as f:
            read = f.read()
            if not read.endswith("\n"): read += "\n"
            parsed = parse(read)
            #print(parsed)
            if parsed != None:
                out = "\n".join(parsed)
                rung["__file__"] = file
                exec(out, rung)
    elif len(sys.argv) > 4:
        src = sys.argv[-2]
        out = sys.argv[-1]
        for file in sys.argv[2:-2]:
            with open(f"{src}/{file}.z", "r") as f:
                print(end=f"zink: {f"{src}/{file}.z".ljust(16)} ... ", flush=True)
                read = f.read()
                if not read.endswith("\n"): read += "\n"
                parsed = parse(read)
                if parsed != None:
                    with open(f"{out}/{file}.py", "w") as fout:
                        fout.write("\n".join(parsed))
                    print(f"\b\b\b\b--> {out}/{file}.py")
                else:
                    print(f"ERR")
                    exit(2)
    else:
        try:
            while True:
                globals = {}
                cmd = input("> ")
                if cmd.lower() == "exit": exit()
                parsed = parse(cmd+"\n\n")
                if parsed != None:
                    print("\n".join(parsed))
                    exec("\n".join(parsed), rung)
        except KeyboardInterrupt:
            print()

if __name__ == "__main__": main()