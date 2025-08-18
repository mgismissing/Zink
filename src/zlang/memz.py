from sly import Lexer

class ZinkLexer(Lexer):
    tokens = {
        "ID", "NUMBER", "STRING", "BSTRING", "RSTRING", "RAWSTRING", "TRUE", "FALSE", "NONE",
        "EQUAL",
        "DB_PLUS", "DB_MINUS",
        "PLUS", "MINUS", "ASTERISK", "SLASH", "DB_ASTERISK", "DB_SLASH", "PERCENTAGE", "MATMUL",
        "PLUS_EQUAL", "MINUS_EQUAL", "ASTERISK_EQUAL", "SLASH_EQUAL", "DOT_EQUAL", "COLON_EQUAL", "DB_ASTERISK_EQUAL", "DB_SLASH_EQUAL", "PERCENTAGE_EQUAL", "MATMUL_EQUAL", "SELF_EQUAL",
        "AMPERSAND", "PIPE", "CARET", "TILDE", "DB_LESS_THAN", "DB_GREATER_THAN",
        "AMPERSAND_EQUAL", "PIPE_EQUAL", "CARET_EQUAL", "TILDE_EQUAL", "DB_LESS_THAN_EQUAL", "DB_GREATER_THAN_EQUAL",
        "LPAREN", "RPAREN", "LBRACK", "RBRACK", "LBRACE", "RBRACE",
        "DOT", "COLON", "SEMICOLON", "COMMA", "EXCLAMATION", "QUESTION",
        "IF", "ELIF", "ELSE", "WHILE", "FOR", "ASSERT", "USE", "FROM", "AS", "LIKE", "AT", "IN", "TO", "TRY", "CATCH", "DEF", "CLASS", "WITH", "DEL", "IS", "HAS", "RAISE", "BETWEEN", "MATCH", "CASE", "IGNORE", "TIMES",
        "PASS", "CONTINUE", "NEXT", "BREAK", "GLOBAL", "LOCAL",
        "AND", "OR", "NOT",
        "CMP_L", "CMP_G", "CMP_E", "CMP_LE", "CMP_GE", "CMP_NE",
        "LQARROW", "RQARROW", "LARROW", "RARROW", "LDARROW", "RDARROW", "LSMARROW", "RSMARROW", "USMARROW", "DSMARROW", "LBARROW", "RBARROW",
        "DB_ARROW", "DB_DARROW", "DB_SMARROW",
        "DOLLAR", "HASHTAG", "ELLIPSIS", "NEW",
        "SUPER_INIT",
        "NEWLINE", "SPACE",
        "COMMENT"
    }

    ignore                  = " \t"

    @_(r"yo .*\n")
    def COMMENT(self, t):
        t.value = t.value[3:].strip("\n")
        return t

    @_(r'\\\n')
    def LINE_CONTINUATION(self, t):
        self.lineno += 1
        return None

    @_(r'"(?:[^"\\]|\\.)*"')
    def STRING(self, t):
        t.value = t.value[1:-1]
        return t

    @_(r'b"(?:[^"\\]|\\.)*"')
    def BSTRING(self, t):
        t.value = t.value[2:-1]
        return t

    @_(r'r"(?:[^"\\]|\\.)*"')
    def RSTRING(self, t):
        t.value = t.value[2:-1]
        return t
    
    @_(r'`(?:[^"\\]|\\.)*`')
    def RAWSTRING(self, t):
        t.value = t.value[1:-1]
        return t

    ID                      = r"[a-zA-Z_][a-zA-Z0-9_]*"

    ELLIPSIS                = r"\.\.\."

    DB_PLUS                 = r"\+\+"
    DB_MINUS                = r"--"

    SELF_EQUAL              = r"@<-"
    SUPER_INIT              = r"@\^"

    LQARROW                 = r"<\?-"
    RQARROW                 = r"-\?>"
    DB_ARROW                = r"<->"
    DB_DARROW               = r"<=>"
    LDARROW                 = r"<<-"
    RDARROW                 = r"->>"
    LARROW                  = r"<-"
    RARROW                  = r"->"
    DB_SMARROW              = r"←→"
    LSMARROW                = r"←"
    RSMARROW                = r"→"
    USMARROW                = r"↑"
    DSMARROW                = r"↓"
    LBARROW                 = r"<\|"
    RBARROW                 = r"\|>"

    DOLLAR                  = r"\$"
    HASHTAG                 = r"#"

    DB_ASTERISK_EQUAL       = r"\*\*="
    DB_SLASH_EQUAL          = r"//="
    PLUS_EQUAL              = r"\+="
    MINUS_EQUAL             = r"-="
    ASTERISK_EQUAL          = r"\*="
    SLASH_EQUAL             = r"/="
    DOT_EQUAL               = r"\.="
    COLON_EQUAL             = r":="
    PERCENTAGE_EQUAL        = r"%="
    MATMUL_EQUAL            = r"@="

    DB_ASTERISK             = r"\*\*"
    DB_SLASH                = r"//"
    PLUS                    = r"\+"
    MINUS                   = r"-"
    ASTERISK                = r"\*"
    SLASH                   = r"/"
    PERCENTAGE              = r"%"
    MATMUL                  = r"@"

    AMPERSAND_EQUAL         = r"&="
    PIPE_EQUAL              = r"\|="
    CARET_EQUAL             = r"\^="
    TILDE_EQUAL             = r"~="
    DB_LESS_THAN_EQUAL      = r"<<="
    DB_GREATER_THAN_EQUAL   = r">>="

    AMPERSAND               = r"&"
    PIPE                    = r"\|"
    CARET                   = r"\^"
    TILDE                   = r"~"
    DB_LESS_THAN            = r"<<"
    DB_GREATER_THAN         = r">>"

    EQUAL                   = r"="

    LPAREN                  = r"\("
    RPAREN                  = r"\)"
    LBRACK                  = r"\["
    RBRACK                  = r"\]"
    LBRACE                  = r"\{"
    RBRACE                  = r"\}"

    DOT                     = r"\."
    COLON                   = r":"
    SEMICOLON               = r";"
    COMMA                   = r","
    EXCLAMATION             = r"!"
    QUESTION                = r"\?"

    SPACE                   = r" "

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

    @_(r"0x[0-9a-fA-F_]+", r"0b[01_]+", r"[0-9_]+", r"[0-9_]\.[0-9_]", r"\.[0-9_]")
    def NUMBER(self, t):
        if t.value.startswith("0x"):
            t.value = int(t.value[2:].strip("_"), 16)
        elif t.value.startswith("0b"):
            t.value = int(t.value[2:].strip("_"), 2)
        elif "." in t.value:
            t.value = float(t.value.strip("_"))
        else:
            t.value = int(t.value)
        return t
    
    @_(r"\n")
    def NEWLINE(self, t):
        self.lineno += 1
        return t
    
    def find_column(text, token):
        last_cr = text.rfind("\n", 0, token.index)
        if last_cr < 0:
            last_cr = 0
        column = (token.index - last_cr) + 1
        return column