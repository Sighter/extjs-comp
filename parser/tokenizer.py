import re

class Token(object):
    """base class for all tokens.

    all tokens have to define a match method which
    returns the length of the match or none if no match
    occured
    """
    def __init__(self, value):
        self.value = value

    @classmethod
    def match(self):
        raise NotImplementedError

    def __str__(self):
        return str(self.__class__) + " => " + self.value


#
# couple of simple detected tokens
#

class TokenSymbol(Token):
    pattern = re.compile('^[a-zA-Z0-9_.]+')
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

class TokenSquareBracket(Token):
    @classmethod
    def match(cls, string):
        return 1 if string.startswith("[") or string.startswith("]") else None

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

class TokenEquals(Token):
    @classmethod
    def match(cls, string):
        return 1 if string.startswith("=") else None

class TokenArithmetic(Token):
    @classmethod
    def match(cls, string):
        return 1 if string[:1] in ['+', '-', '/', '*'] else None

class TokenComment(Token):
    """parse a comment this works like simple statemachine
    for multiline comments"""

    MLCOMMENT_START = "/*"
    MLCOMMENT_END = "*/"

    simple_pattern = re.compile("""//.*\n""")
    @classmethod
    def match(cls, string):

        # match simple one line comment
        match = cls.simple_pattern.match(string)
        if match:
            return match if match is None else match.end() - match.start()

        # match multiline comment
        if string.startswith(cls.MLCOMMENT_START):
            string = string[2:]
            length = 2

            # slice string down till you find the end of comment
            while string != '':
                if string.startswith(cls.MLCOMMENT_END):
                    return length + 2

                length += 1
                string = string[1:]

        return None

class TokenString(Token):
    """
    class for parsing strings

    @todo add quote escaping
    """

    def __init__(self, value):
        self.value = value[1:-1]


    allowedQuotes = ['"', "'"]

    @classmethod
    def match(cls, string):

        char = string[:1]
        if char in cls.allowedQuotes:
            string = string[1:]
            length = 1

            current_quote = char

            while string != '':
                if string.startswith(current_quote):
                    return length + 1
                else:
                    string = string[1:]
                    length += 1

        return None

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
            TokenSquareBracket,
            TokenComma,
            TokenSemi,
            TokenColon,
            TokenComment,
            TokenEquals,
            TokenArithmetic,
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



