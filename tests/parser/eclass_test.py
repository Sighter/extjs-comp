
import unittest
from mock import patch
from nose.plugins.skip import Skip, SkipTest

from parser.eclass import EclassParser
from parser.eclass import Eclass
from parser.eclass import EclassBody
from parser.tokenizer import Tokenizer
from parser import tokenizer as t

class TestEclass(unittest.TestCase):

    def setUp(self):
        self.parser = EclassParser()

    def tearDown(self):
        pass

    def test_parser_parse_method(self):

        f = open("tests/files/Upload.js").read()

        tz = Tokenizer()
        token_list = tz.tokenizestr(f)

        self.assertTrue(len(token_list) > 0)

        tree = self.parser.parse(token_list)

        self.assertIsInstance(tree, Eclass)
        self.assertEquals(tree.name, 'Lier.media.view.Upload')
        class_body = tree.get_unrevealed_tokens()
        self.assertNotEquals(class_body, [])
        self.assertIsInstance(class_body[0], t.TokenBlockBracket)
        self.assertIsInstance(class_body[len(class_body) - 1], t.TokenBlockBracket)

    def test_eclassbody_from_token_list(self):

        f = open("tests/files/Upload.js").read()
        tz = Tokenizer()
        token_list = tz.tokenizestr(f)
        eclass = self.parser.parse(token_list)

        body = EclassBody.from_token_list(eclass.get_unrevealed_tokens())

        self.assertIsInstance(body, EclassBody)
        self.assertEqual(len(body.properties), 7)

