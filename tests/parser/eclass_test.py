
import unittest
from mock import patch
from nose.plugins.skip import Skip, SkipTest

from parser.eclass import EclassParser
from parser.eclass import Eclass
from parser.tokenizer import Tokenizer

class TestEclass(unittest.TestCase):

    def setUp(self):
        self.parser = EclassParser()

    def tearDown(self):
        pass

    def test_parser_parse_method(self):

        f = open("tests/files/Upload.js").read()

        t = Tokenizer()
        token_list = t.tokenizestr(f)

        self.assertTrue(len(token_list) > 0)

        tree = self.parser.parse(token_list)

        self.assertIsInstance(tree, Eclass)
        self.assertEquals(tree.name, 'Lier.media.view.Upload')
        self.assertNotEquals(tree.getUnrevealedTokens(), [])