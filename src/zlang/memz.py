from sly import Lexer
from .zink import ZinkLexer as ZLexer

class ZinkLexer(ZLexer):
    tokens = ZLexer.tokens

    @_(r"yo .*\n")
    def COMMENT(self, t):
        t.value = t.value[3:].strip("\n")
        return t
    
    ID = ZLexer.ID

    ID["bet"]               = "IF"
    ID["sus"]               = "ELIF"
    ID["imp"]               = "ELSE"
    ID["while"]             = "WHILE"
    ID["spin"]              = "FOR"
    ID["bruh"]              = "ASSERT"
    ID["get"]               = "USE"
    ID["from"]              = "FROM"
    ID["as"]                = "AS"
    ID["like"]              = "LIKE"
    ID["at"]                = "AT"
    ID["in"]                = "IN"
    ID["to"]                = "TO"
    ID["fuck_around"]       = "TRY"
    ID["get_real"]          = "CATCH"
    ID["nah"]               = "PASS"
    ID["continue"]          = "CONTINUE"
    ID["next"]              = "NEXT"
    ID["global"]            = "GLOBAL"
    ID["private"]           = "LOCAL"
    ID["quit"]              = "BREAK"
    ID["nocap"]             = "TRUE"
    ID["cap"]               = "FALSE"
    ID["none"]              = "NONE"
    ID["mem"]               = "DEF"
    ID["forget"]            = "DEL"
    ID["and"]               = "AND"
    ID["or"]                = "OR"
    ID["not"]               = "NOT"
    ID["is"]                = "IS"
    ID["has"]               = "HAS"
    ID["memz"]              = "CLASS"
    ID["with"]              = "WITH"
    ID["ragequit"]          = "RAISE"
    ID["between"]           = "BETWEEN"
    ID["match"]             = "MATCH"
    ID["case"]              = "CASE"
    ID["ragebait"]          = "IGNORE"
    ID["repeat"]            = "TIMES"

    ID["same"]              = "CMP_E"
    ID["cappin"]            = "CMP_NE"
    ID["lil"]               = "CMP_LE"
    ID["big"]               = "CMP_GE"
    ID["lilbro"]            = "CMP_L"
    ID["bigbro"]            = "CMP_G"