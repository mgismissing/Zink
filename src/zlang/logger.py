from colorama import Fore as cF, Back as cB, Style as cS, init as cinit
cinit(autoreset=True)

def custom(c: str, t: str, s: str) -> str:
    return f"{cS.BRIGHT}{c}{t}: {cS.NORMAL}{s}"
def print_custom(c: str, t: str, s: str) -> None:
    print(custom(c, t, s))

def info(s: str) -> str:
    return custom(cF.LIGHTCYAN_EX, "INFO", s)
def print_info(s: str) -> None:
    print(info(s))

def warn(s: str) -> str:
    return custom(cF.LIGHTYELLOW_EX, "WARNING", s)
def print_warn(s: str) -> None:
    print(warn(s))

def error(s: str) -> str:
    return custom(cF.LIGHTRED_EX, "ERROR", s)
def print_error(s: str) -> None:
    print(error(s))