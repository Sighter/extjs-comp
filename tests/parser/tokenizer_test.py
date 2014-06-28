
import unittest
from mock import patch
from nose.plugins.skip import Skip, SkipTest

from parser.tokenizer import *

class TestTokenizer(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_instance(self):
        
        t = Scanner('Ext.define')

        src = """Ext.define ("Bla.class", {
                extend: "somestring"
            });
        """
        self.assertIsNotNone(t.search(' Ext.define("MyApp.pack.some.MyClass", {'))
        self.assertIsNotNone(t.search(' Ext.define ("MyApp.pack.some.MyClass", {'))


        self.assertEquals('Ext.define', 'definestatement')
        self.assertEquals('Ext.define', 'bracket')
