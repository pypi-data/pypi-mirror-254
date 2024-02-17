import unittest

import ai21
from ai21.ai21_studio_client import AI21StudioClient
from ai21.errors import MissingApiKeyException


class TestClientConstruction(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        ai21.api_key = None
        ai21.organization = None
        ai21.application = None
        ai21.timeout_sec = None
        ai21.num_retries = None

    def testClientWithMissingAPIKey(self):
        with self.assertRaises(MissingApiKeyException):
            client = AI21StudioClient(**{})

    def testSimpleClientWithPassedAPIKey(self):
        params = {
            'api_key': 'test_api_key',
        }
        client = AI21StudioClient(**params)
        self.assertIsInstance(client, AI21StudioClient)

    def testSimpleClientWithGlobalAPIKey(self):
        ai21.api_key = 'test_global_api_key'
        client = AI21StudioClient(**{})
        self.assertIsInstance(client, AI21StudioClient)

    def testSimpleClientWithPassedAndGlobalAPIKey(self):
        ai21.api_key = 'test_global_api_key'
        params = {
            'api_key': 'test_api_key',
        }
        client = AI21StudioClient(**params)
        self.assertEqual(client.api_key, 'test_api_key')

    def testClientWithPassedOverrides(self):
        params = {
            'api_key': 'test_api_key',
            'timeout_sec': 10,
            'num_retries': 5
        }
        client = AI21StudioClient(**params)
        self.assertEqual(client.api_key, 'test_api_key')
        self.assertEqual(client.http_client.timeout_sec, 10)
        self.assertEqual(client.http_client.num_retries, 5)

    def testClientWithGlobalOverrides(self):
        ai21.timeout_sec = 10
        ai21.num_retries = 5
        ai21.application = 'test_app'
        ai21.organization = 'test_org'
        params = {
            'api_key': 'test_api_key'
        }
        client = AI21StudioClient(**params)
        self.assertEqual(client.api_key, 'test_api_key')
        self.assertEqual(client.http_client.timeout_sec, 10)
        self.assertEqual(client.http_client.num_retries, 5)
        self.assertTrue(f'organization: test_org application: test_app' in client.http_client.headers['User-Agent'])
