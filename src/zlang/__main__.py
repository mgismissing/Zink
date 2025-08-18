from .zink import ZinkLexer, ZinkParser
from . import translators
from .logger import print_info, print_warn, print_error
from argparse import ArgumentParser, SUPPRESS as ARG_HELP_HIDE
from sly.lex import LexError
import colorama

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
    parser.add_argument(
        "-p", "--pretty",
        action="store_true",
        help="keep comments and empty lines in translated output"
    )
    parser.add_argument(
        "--ignore-obsolete",
        action="store_true",
        help="suppress obsolete warnings"
    )
    parser.add_argument(
        "--memz",
        action="store_true",
        help=ARG_HELP_HIDE
    )
    return parser.parse_args()

def main():
    colorama.init(autoreset=True)
    args = parse_args()
    lexer = ZinkLexer() if not args.memz else translators.mem()
    parser = ZinkParser(
        ignore_obsolete=args.ignore_obsolete,
        include_comments=args.pretty,
        include_empty_lines=args.pretty
    )

    try: translator: translators.T = getattr(translators, f"_{args.lang}")()
    except AttributeError: print_error(f"Missing ruleset for language \"{args.lang}\""); exit(3)

    def strip_paren(s):
        return str(s).removeprefix("(").removesuffix(")")
        
    def parse(s: str):
        parsed = parser.parse(lexer.tokenize(s))
        #print(parsed)
        return None if parsed == None else translator(parsed, "None", 0)

    rung = {
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
                if parsed != None:
                    out = "\n".join(parsed)
                    if len(args.files) == 1:
                        if args.verbose: print(f"\b\b\b\b--> Done!")
                        if args.lang == "py":
                            rung["__file__"] = file
                            exec(out, rung)
                        else: print(out)
                    elif len(args.files) % 2 == 0:
                        with open(args.files[i+1], "w") as fout:
                            fout.write("\n".join(parsed))
                        if args.verbose: print(f"\b\b\b\b--> {args.files[i+1]}")
                    else:
                        print(end="\r"); print_error(f"Unspecified output file for \"{args.files[-1]}\"")
                        exit(5)
                else:
                    print_error("Unknown parser error")
                    exit(2)
                i += 2
    else:
        try:
            while True:
                cmd = input(colorama.Fore.LIGHTGREEN_EX+"> "+colorama.Fore.RESET)
                if cmd.lower() == "exit": exit(0)
                try:
                    parsed = parse(cmd+"\n")
                except LexError as e:
                    print_error(e)
                else:
                    if parsed:
                        if args.verbose or args.lang != "py": print("\n".join(parsed))
                        if args.lang == "py":
                            try:
                                exec("\n".join(parsed), rung)
                            except Exception as e:
                                print_error(f"Python {e.__class__.__name__}: {e}")
        except KeyboardInterrupt:
            print()

if __name__ == "__main__": main()