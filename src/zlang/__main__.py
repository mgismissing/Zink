from .zink import ZinkLexer, ZinkParser
from . import translators
from argparse import ArgumentParser

def parse_args():
    parser = ArgumentParser(prog="zink")
    parser.add_argument(
        "-l", "--lang", "--language",
        default="py",
        help="language to translate to (default: py)"
    )
    parser.add_argument(
        "file",
        metavar="file",
        nargs="?",
        help="Zink source file to translate"
    )
    parser.add_argument(
        "output",
        metavar="output",
        nargs="?",
        help="output file"
    )
    parser.add_argument(
        "-v", "--verbose",
        action="store_true",
        help="enable verbose output"
    )
    return parser.parse_args()

def main():
    args = parse_args()
    lexer = ZinkLexer()
    parser = ZinkParser()

    try: translator: translators.T = getattr(translators, f"_{args.lang}")()
    except AttributeError: print(f"Missing ruleset for language \"{args.lang}\""); exit(3)

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

    if args.file:
        with open(args.file, "r") as f:
            if args.verbose: print(end=f"zink: {args.file.ljust(16)} ... ", flush=True)
            read = f.read()
            if not read.endswith("\n"): read += "\n"
            parsed = parse(read)
            #print(parsed)
            if parsed != None:
                out = "\n".join(parsed)
                if args.output:
                    with open(args.output, "w") as fout:
                        fout.write("\n".join(parsed))
                    if args.verbose: print(f"\b\b\b\b--> {args.output}.py")
                else:
                    if args.verbose: print(f"\b\b\b\b--> Done!")
                    rung["__file__"] = args.file
                    exec(out, rung)
            else:
                print("Parse error")
                exit(2)
    else:
        try:
            while True:
                globals = {}
                cmd = input("> ")
                if cmd.lower() == "exit": exit()
                parsed = parse(cmd+"\n\n")
                if parsed != None:
                    if args.verbose: print("\n".join(parsed))
                    exec("\n".join(parsed), rung)
        except KeyboardInterrupt:
            print()

if __name__ == "__main__": main()