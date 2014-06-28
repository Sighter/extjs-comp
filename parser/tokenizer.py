import re

class Token(object):
    def __init__(self, value, ttype):
        self.value = value
        self.ttype = ttype

class Scanner():
    def __init__(self, pattern):
        self.pattern = pattern
        self.cpattern = re.compile(pattern, re.MULTILINE)

    def search(self, string_to_match_on):
        m = self.cpattern.search(string_to_match_on)
        return m

class TokenTree:


class Tokenizer(object):
    """docstring for Tokenizer"""
    def __init__(self):
        pass

