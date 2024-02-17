import unittest

import ai21
from ai21.ai21_studio_client import AI21StudioClient
from ai21.errors import MissingApiKeyException, MissingInputException, WrongInputTypeException, EmptyMandatoryListException


class TestExceptions(unittest.TestCase):

    def setUp(self):
        ai21.api_key = 'test_api_key'

    def tearDown(self):
        ai21.api_key = None
        ai21.organization = None
        ai21.application = None
        ai21.timeout_sec = None
        ai21.num_retries = None

    def testMissingInputException(self):
        with self.assertRaises(MissingInputException):
            ai21.Paraphrase.execute(forot_to="pass_text")

    def testWrongInputTypeException(self):
        with self.assertRaises(WrongInputTypeException):
            ai21.Paraphrase.execute(text=5)

    def testEmptyMandatoryListException(self):
        with self.assertRaises(EmptyMandatoryListException):
            ai21.Improvements.execute(text="some text")
        with self.assertRaises(EmptyMandatoryListException):
            ai21.Improvements.execute(text="some text", types=[])
