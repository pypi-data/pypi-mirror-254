import unittest

import ai21
from ai21 import Paraphrase, Summarize, GEC, Improvements, Segmentation, SummarizeBySegment
from ai21.ai21_object import AI21Object, construct_ai21_object
from ai21.utils import convert_to_ai21_object
from test_mocks import COMPLETION_MOCK, PARAPHRASE_MOCK, CORRECTIONS_MOCK, IMPROVEMENT_MOCK, SEGMENTATION_MOCK, \
    SUMMARIZATION_MOCK, SUMMARIZE_BY_SEGMENT_MOCK


class TestAI21ObjectConstruction(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        ai21.api_key = None
        ai21.organization = None
        ai21.application = None
        ai21.timeout_sec = None
        ai21.num_retries = None

    def testDummyObjectConstruction(self):
        obj = [
            {
                'id': '1234567890',
                'text': 'This is a test',
                'type': 'no_such_type_in_ai_21',
                'language': 'en',
                'entities': [
                    {'id': 123, 'text': 'This is a test'}
                ]
            },
            1,
            {
                'id': 123,
                'type': 'paraphrase',
                'text': 'This is a test'
            },
            2,
            {
                'text': 'This is a test',
                'language': 'en',
            }
        ]
        ai21_obj = convert_to_ai21_object(obj)
        self.assertIsInstance(ai21_obj[0], AI21Object)
        self.assertIsInstance(ai21_obj[1], int)
        self.assertIsInstance(ai21_obj[2], AI21Object)
        self.assertIsInstance(ai21_obj[2].id, int)
        self.assertIsInstance(ai21_obj[2].text, str)
        ai21_obj = AI21Object(obj)
        self.assertIsInstance(ai21_obj, AI21Object)

    def testCompletionObjectConstruction(self):
        ai21_obj = construct_ai21_object(COMPLETION_MOCK)
        self.assertIsInstance(ai21_obj, AI21Object)
        self.assertTrue(ai21_obj.id is not None)
        self.assertTrue(ai21_obj['id'] is not None)

    def testParaphraseObjectConstruction(self):
        ai21_obj = construct_ai21_object(PARAPHRASE_MOCK)
        self.assertIsInstance(ai21_obj, AI21Object)
        self.assertIsInstance(ai21_obj, Paraphrase)
        self.assertTrue(ai21_obj.id is not None)
        self.assertTrue(ai21_obj['id'] is not None)

    def testCorrectionsObjectConstruction(self):
        ai21_obj = construct_ai21_object(CORRECTIONS_MOCK)
        self.assertIsInstance(ai21_obj, AI21Object)
        self.assertIsInstance(ai21_obj, GEC)
        self.assertTrue(ai21_obj.id is not None)
        self.assertTrue(ai21_obj['id'] is not None)

    def testImprovementObjectConstruction(self):
        ai21_obj = construct_ai21_object(IMPROVEMENT_MOCK)
        self.assertIsInstance(ai21_obj, AI21Object)
        self.assertIsInstance(ai21_obj, Improvements)
        self.assertTrue(ai21_obj.id is not None)
        self.assertTrue(ai21_obj['id'] is not None)

    def testSummarizationObjectConstruction(self):
        ai21_obj = construct_ai21_object(SUMMARIZATION_MOCK)
        self.assertIsInstance(ai21_obj, AI21Object)
        self.assertIsInstance(ai21_obj, Summarize)
        self.assertTrue(ai21_obj.id is not None)
        self.assertTrue(ai21_obj['id'] is not None)

    def testSegmentationObjectConstruction(self):
        ai21_obj = construct_ai21_object(SEGMENTATION_MOCK)
        self.assertIsInstance(ai21_obj, AI21Object)
        self.assertIsInstance(ai21_obj, Segmentation)
        self.assertTrue(ai21_obj.id is not None)
        self.assertTrue(ai21_obj['id'] is not None)

    def testSummarizeBySegmentObjectConstruction(self):
        ai21_obj = construct_ai21_object(SUMMARIZE_BY_SEGMENT_MOCK)
        self.assertIsInstance(ai21_obj, AI21Object)
        self.assertIsInstance(ai21_obj, SummarizeBySegment)
        self.assertTrue(ai21_obj.id is not None)
        self.assertTrue(ai21_obj['id'] is not None)
