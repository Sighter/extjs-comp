
from parser.constructs import BaseContruct
from parser import tokenizer as t

class Eclass(BaseContruct):
    """docstring for Eclass"""
    def __init__(self, name, class_body):
        self.name = name
        self.class_body_tokens = class_body

    def get_unrevealed_tokens(self):
        return self.class_body_tokens


class EclassParser(object):
    """docstring for EclassParser"""
    def __init__(self):
        pass

    def parse(self, token_list):
        """acts like a factory and onstructs Eclass objects
        from a token list"""

        classname = ""
        tlist = None

        bracket_stack = []

        # consume everything till the first TokenSymbol
        p1 = 0
        p2 = 0

        while p1 < len(token_list) and not isinstance(token_list[p1], t.TokenSymbol):
            p1 += 1

        if not isinstance(token_list[p1+1], t.TokenFunctionBracket):
            return None

        if isinstance(token_list[p1+2], t.TokenString):
            classname = token_list[p1+2].value

        if not isinstance(token_list[p1+3], t.TokenComma):
            return None

        if not isinstance(token_list[p1+4], t.TokenBlockBracket):
            return None

        p1 = p1 + 4
        p2 = p1 + 1
        bracket_stack.append(token_list[p1].value)


        print 'entering loop', bracket_stack, p2

        while p2 < len(token_list) and bracket_stack:
            tok = token_list[p2]
            if isinstance(tok, t.TokenBlockBracket) and tok.value == '{':
                bracket_stack.append('{')
            elif isinstance(tok, t.TokenBlockBracket) and tok.value == '}':
                bracket_stack.pop()

            p2 += 1

        tlist = token_list[p1:p2]

        return Eclass(classname, tlist)
