
from parser.constructs import BaseContruct
from parser import tokenizer as t

class Eclass(BaseContruct):
    """docstring for Eclass"""
    def __init__(self, name, class_body):
        self.name = name
        self.class_body_tokens = class_body
        self.classbody = None

    def get_unrevealed_tokens(self):
        return self.class_body_tokens

    def expand(self):
        """parse the unparsed classbody"""
        pass


class EclassBody(BaseContruct):

    def __init__(self):
        self.properties = []

    def match(cls, token_list, startindex, endindex=None):
        endindex = endindex if endindex else len(token_list)

    def get_properties(self):
        return self.properties

    @classmethod
    def from_token_list(cls, token_list):
        """creates classbody object from a tokenlist
        this must be an object literal"""

        bracket_stack = []

        eclass_body = EclassBody()

        p = 0
        while p < len(token_list):
            tok = token_list[p]

            if isinstance(tok, t.TokenBlockBracket) and tok.value == '{':
                bracket_stack.append('{')

            if isinstance(tok, t.TokenBlockBracket) and tok.value == '}':
                bracket_stack.pop()

            if len(bracket_stack) > 1:
                p += 1
                continue

            start, end, ecp  = EclassProperty.match(token_list, p)

            if start and end and ecp:
                eclass_body.properties.append(ecp)

            p += 1

        print eclass_body.properties

        return eclass_body



class EclassProperty(BaseContruct):

    def __init__(self, name, ptype):
        self.ptype = ptype
        self.name = name

    def __repr__(self):
        return self.name + ": " + self.ptype

    @classmethod
    def match(cls, token_list, startindex, endindex=None):
        endindex = endindex if endindex else len(token_list)

        tl = token_list

        if (isinstance(tl[startindex], t.TokenSymbol) and
                isinstance(tl[startindex + 1], t.TokenColon)):

            name = tl[startindex].value
            ptype = 'plain'
            third = tl[startindex + 2]

            if (isinstance(third, t.TokenSymbol) and third.value == 'function'):
                ptype = 'function'

            ecp = EclassProperty(name, ptype)

            return startindex, startindex + 2, ecp
        else:
            return None, None, None

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
