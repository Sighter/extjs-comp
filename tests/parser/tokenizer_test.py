
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
        self.assertEquals(3, l)

        l = TokenSymbol.match(s2)
        self.assertEquals(None, l)



    def test_instance(self):
        
        src = """ Ext.define ("Bla.class", {
                extend: "somestring"
            });
        """

        t = Tokenizer()
        token_list = t.tokenizestr(src)

        for tok in token_list:

            print tok.__class__, tok.value
