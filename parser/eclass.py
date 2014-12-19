
from parser.constructs import BaseContruct
from parser import tokenizer as t

class Eclass(BaseContruct):
    """docstring for Eclass"""
    def __init__(self, name, class_body):
        self.name = name
        self.class_body_tokens = class_body



class EclassParser(object):
    """docstring for EclassParser"""
    def __init__(self):
        pass

    def parse(self, token_list):
        """acts like a factory and onstructs Eclass objects
        out of a directory"""

        classname = ""
        tlist = None

        # consume everything till the firs TokenSymbol
        p1 = 0
        p2 = 0

        while p1 < len(token_list) and not isinstance(token_list[p1], t.TokenSymbol):
            p1 += 1

        if not isinstance(token_list[p1+1], t.TokenFunctionBracket):
            return None

        if isinstance(token_list[p1+2], t.TokenString):
            name = token_list[p1+2].value

        return Eclass(name, "lala")
