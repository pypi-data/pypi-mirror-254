import unittest
import ai21
from ai21.errors import MissingInputException, WrongInputTypeException, UnsupportedInputException, OnlyOneInputException


class TestInputValidation(unittest.TestCase):

    def setUp(self):
        ai21.api_key = 'test_api_key'

    def tearDown(self):
        ai21.api_key = None
        ai21.organization = None
        ai21.application = None
        ai21.timeout_sec = None
        ai21.num_retries = None

    def testCompletionNoPromptOrModel(self):
        with self.assertRaises(MissingInputException):
            ai21.Completion.execute(model='test')
        with self.assertRaises(MissingInputException):
            ai21.Completion.execute(prompt='test')

    def testCompletionWrongTypeInput(self):
        with self.assertRaises(WrongInputTypeException):
            ai21.Completion.execute(model=1, prompt='test')
        with self.assertRaises(WrongInputTypeException):
            ai21.Completion.execute(model='test', prompt={'a': 1})

    def testCompletionSMWithCM(self):
        with self.assertRaises(UnsupportedInputException):
            ai21.Completion.execute(sm_endpoint='test-endpoint', prompt='test', custom_model='test-cm')

    def testCompletionOneOfModelOrSMEndpoint(self):
        with self.assertRaises(UnsupportedInputException):
            ai21.Completion.execute(sm_endpoint='test-endpoint', model='test', prompt='test')
        with self.assertRaises(MissingInputException):
            ai21.Completion.execute(prompt='test')