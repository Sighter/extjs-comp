
import unittest
from mock import patch
from nose.plugins.skip import Skip, SkipTest

from parser.tokenizer import *

class TestTokenizer(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_tokens(self):
        s = 'Ext.panel("dajdskal")'
        s2 = '("dajdskal")'

        l = TokenSymbol.match(s)
        self.assertEquals(9, l)

        l = TokenSymbol.match(s2)
        self.assertEquals(None, l)



    def test_instance(self):
        f = open("tests/files/Upload.js").read()

        t = Tokenizer()
        token_list = t.tokenizestr(f)

        for tok in token_list:

            print tok.__class__, tok.value
