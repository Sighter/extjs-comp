import re

class Token(object):
    def __init__(self, value):
        self.value = value

    @classmethod
    def match(self):
        raise NotImplementedError

    def __str__(self):
        return self.__class__ + " => " + self.value

class TokenString(Token):
    pattern = re.compile("""^".*"|^'.*'""")
    @classmethod
    def match(cls, string):
        m = cls.pattern.match(string)
        return m if m is None else m.end() - m.start()

class TokenSymbol(Token):
    pattern = re.compile('^[a-zA-Z0-9_]+')
    @classmethod
    def match(cls, string):
        m = cls.pattern.match(string)
        return m if m is None else m.end() - m.start()

class TokenFunctionBracket(Token):
    @classmethod
    def match(cls, string):
        return 1 if string.startswith("(") or string.startswith(")") else None

class TokenBlockBracket(Token):
    @classmethod
    def match(cls, string):
        return 1 if string.startswith("{") or string.startswith("}") else None

class TokenDot(Token):
    @classmethod
    def match(cls, string):
        return 1 if string.startswith(".") else None

class TokenComma(Token):
    @classmethod
    def match(cls, string):
        return 1 if string.startswith(",") else None

class TokenSemi(Token):
    @classmethod
    def match(cls, string):
        return 1 if string.startswith(";") else None

class TokenColon(Token):
    @classmethod
    def match(cls, string):
        return 1 if string.startswith(":") else None

class TokenTree:
    pass


class Tokenizer(object):
    """docstring for Tokenizer"""
    def __init__(self):
        self.token_classes = [
            TokenString,
            TokenDot,
            TokenSymbol,
            TokenFunctionBracket,
            TokenBlockBracket,
            TokenComma,
            TokenSemi,
            TokenColon
        ]

    def match_str_against_classes(self, s):
        for c in self.token_classes:
            length = c.match(s)

            if length is not None:
                print "matched: " + str(c)
                c = c(s[:length])
                s = s[length:]
                return length, c

        raise TokenizerError("No Token found for string:" + s)




    def tokenizestr(self, s):

        idx = 0
        s = s.lstrip()
        token_list = []

        while s != "":

            match_length, token = self.match_str_against_classes(s)
            token_list.append(token)
            s = s[match_length:]
            s = s.lstrip()

        return token_list


            

class TokenizerError(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value)



