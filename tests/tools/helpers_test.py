import unittest
from mock import patch
from nose.plugins.skip import Skip, SkipTest

from tools import helpers
class TestHelpers(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_string_itarator(self):

        it = helpers.StringHangingIterator("hello")

        self.assertEquals("h", it.next())
        self.assertEquals("he", it.next())
        self.assertEquals("hel", it.next())
        self.assertEquals("hell", it.next())
        self.assertEquals("hello", it.next())

        self.assertRaises(StopIteration, it.next)

        it = helpers.StringHangingIterator("Some.class(")
        self.assertEquals("S", it.next())
        self.assertEquals("So", it.next())
        it.consume()
        self.assertEquals("m", it.next())
        self.assertEquals("me", it.next())
        self.assertEquals("me.", it.next())
