from .zink import ZinkLexer, ZinkParser
from . import translators
from argparse import ArgumentParser

def parse_args():
    parser = ArgumentParser(prog="zink")
    parser.add_argument(
        "-l", "--lang",
        metavar="lang",
        default="py",
        help="language to translate to (default: py)"
    )
    parser.add_argument(
        "files",
        metavar=("file", "output"),
        nargs="*",
        help="Zink file(s) to translate and translated output file(s) pair"
    )
    parser.add_argument(
        "-v", "--verbose",
        action="store_true",
        help="enable verbose output"
    )
    return parser.parse_args()

def main():
    args = parse_args()
    print(args)
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

    if args.files:
        i = 0
        while i < len(args.files):
            file = args.files[i]
            with open(file, "r") as f:
                if args.verbose: print(end=f"zink: {file.ljust(16)} ... ", flush=True)
                read = f.read()
                if not read.endswith("\n"): read += "\n"
                parsed = parse(read)
                #print(parsed)
                if parsed != None:
                    out = "\n".join(parsed)
                    if len(args.files) == 1:
                        if args.verbose: print(f"\b\b\b\b--> Done!")
                        rung["__file__"] = file
                        exec(out, rung)
                    elif len(args.files) % 2 == 0:
                        with open(args.files[i+1], "w") as fout:
                            fout.write("\n".join(parsed))
                        if args.verbose: print(f"\b\b\b\b--> {args.files[i+1]}")
                    else:
                        print(f"\rUnspecified output file for \"{args.files[-1]}\"")
                        exit(5)
                else:
                    print("Parse error")
                    exit(2)
                i += 2
    else:
        try:
            while True:
                globals = {}
                cmd = input("> ")
                if cmd.lower() == "exit": exit(0)
                parsed = parse(cmd+"\n\n")
                if parsed != None:
                    if args.verbose: print("\n".join(parsed))
                    exec("\n".join(parsed), rung)
        except KeyboardInterrupt:
            print()

if __name__ == "__main__": main()