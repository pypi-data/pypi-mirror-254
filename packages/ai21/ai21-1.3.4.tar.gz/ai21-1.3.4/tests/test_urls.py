import uuid
from typing import Optional, Dict
from unittest import mock
import unittest
import ai21
from ai21 import AI21Destination


MOCK_FILE_STREAM = 'mock-file-stream'
MOCK_HTTP_RESPONSES = []


def mock_url_from_execute_http_request(self, method: str, url: str, params: Optional[Dict] = None, files=None):
    MOCK_HTTP_RESPONSES.append((url, method, params, files))
    return True


def mock_open(file, mode='r', buffering=None, encoding=None, errors=None, newline=None, closefd=True):
    return MOCK_FILE_STREAM


class TestUrls(unittest.TestCase):

    def setUp(self):
        ai21.api_key = 'test_api_key'

    def tearDown(self):
        ai21.api_key = None
        ai21.organization = None
        ai21.application = None
        ai21.timeout_sec = None
        ai21.num_retries = None
        MOCK_HTTP_RESPONSES.clear()

    @mock.patch('ai21.ai21_studio_client.AI21StudioClient.execute_http_request', new=mock_url_from_execute_http_request)
    def test_tokenize(self):
        ai21.Tokenization.execute(text='test prompt')
        response = MOCK_HTTP_RESPONSES.pop()
        self.assertEqual(response[0], 'https://api.ai21.com/studio/v1/tokenize')
        self.assertEqual(response[1], 'POST')

    @mock.patch('ai21.ai21_studio_client.AI21StudioClient.execute_http_request', new=mock_url_from_execute_http_request)
    def test_completion(self):
        ai21.Completion.execute(model="j2-light", prompt='test prompt')
        response = MOCK_HTTP_RESPONSES.pop()
        self.assertEqual(response[0], 'https://api.ai21.com/studio/v1/j2-light/complete')
        self.assertEqual(response[1], 'POST')

        ai21.Completion.execute(model="j2-light", custom_model='test-custom-model', prompt='test prompt')
        response = MOCK_HTTP_RESPONSES.pop()
        self.assertEqual(response[0], 'https://api.ai21.com/studio/v1/j2-light/test-custom-model/complete')
        self.assertEqual(response[1], 'POST')

    @mock.patch('ai21.ai21_studio_client.AI21StudioClient.execute_http_request', new=mock_url_from_execute_http_request)
    def test_get_custom_model(self):
        ai21.CustomModel.get('test-custom-model-id')
        response = MOCK_HTTP_RESPONSES.pop()
        self.assertEqual(response[0], 'https://api.ai21.com/studio/v1/custom-model/test-custom-model-id')
        self.assertEqual(response[1], 'GET')

    @mock.patch('ai21.ai21_studio_client.AI21StudioClient.execute_http_request', new=mock_url_from_execute_http_request)
    def test_list_custom_models(self):
        ai21.CustomModel.list()
        response = MOCK_HTTP_RESPONSES.pop()
        self.assertEqual(response[0], 'https://api.ai21.com/studio/v1/custom-model')
        self.assertEqual(response[1], 'GET')

    @mock.patch('ai21.modules.resources.uploadable_resource.open', new=mock_open)
    @mock.patch('ai21.ai21_studio_client.AI21StudioClient.execute_http_request', new=mock_url_from_execute_http_request)
    def test_upload_dataset(self):
        ai21.Dataset.upload(file_path='path/to/dataset.txt', dataset_name='test-dataset-name')
        response = MOCK_HTTP_RESPONSES.pop()
        self.assertEqual(response[0], 'https://api.ai21.com/studio/v1/dataset')
        self.assertEqual(response[1], 'POST')
        self.assertEqual(response[3], {'dataset_file': MOCK_FILE_STREAM})

    @mock.patch('ai21.ai21_studio_client.AI21StudioClient.execute_http_request', new=mock_url_from_execute_http_request)
    def test_get_dataset(self):
        ai21.Dataset.get('test-dataset-id')
        response = MOCK_HTTP_RESPONSES.pop()
        self.assertEqual(response[0], 'https://api.ai21.com/studio/v1/dataset/test-dataset-id')
        self.assertEqual(response[1], 'GET')

    @mock.patch('ai21.ai21_studio_client.AI21StudioClient.execute_http_request', new=mock_url_from_execute_http_request)
    def test_list_datasets(self):
        ai21.Dataset.list()
        response = MOCK_HTTP_RESPONSES.pop()
        self.assertEqual(response[0], 'https://api.ai21.com/studio/v1/dataset')
        self.assertEqual(response[1], 'GET')

    @mock.patch('ai21.ai21_studio_client.AI21StudioClient.execute_http_request', new=mock_url_from_execute_http_request)
    def test_list_library_files(self):
        ai21.Library.Files.list()
        response = MOCK_HTTP_RESPONSES.pop()
        self.assertEqual(response[0], 'https://api.ai21.com/studio/v1/library/files')
        self.assertEqual(response[1], 'GET')

    @mock.patch('ai21.modules.resources.uploadable_resource.open', new=mock_open)
    @mock.patch('ai21.ai21_studio_client.AI21StudioClient.execute_http_request', new=mock_url_from_execute_http_request)
    def test_upload_library_files(self):
        ai21.Library.Files.upload('path/to/file.txt')
        response = MOCK_HTTP_RESPONSES.pop()
        self.assertEqual(response[0], 'https://api.ai21.com/studio/v1/library/files')
        self.assertEqual(response[1], 'POST')
        self.assertEqual(response[3], {'file': MOCK_FILE_STREAM})

    @mock.patch('ai21.ai21_studio_client.AI21StudioClient.execute_http_request', new=mock_url_from_execute_http_request)
    def test_get_library_files(self):
        file_id = uuid.uuid4()
        ai21.Library.Files.get(file_id)
        response = MOCK_HTTP_RESPONSES.pop()
        self.assertEqual(response[0], f'https://api.ai21.com/studio/v1/library/files/{file_id}')
        self.assertEqual(response[1], 'GET')

    @mock.patch('ai21.ai21_studio_client.AI21StudioClient.execute_http_request', new=mock_url_from_execute_http_request)
    def test_delete_library_files(self):
        file_id = uuid.uuid4()
        ai21.Library.Files.delete(file_id)
        response = MOCK_HTTP_RESPONSES.pop()
        self.assertEqual(response[0], f'https://api.ai21.com/studio/v1/library/files/{file_id}')
        self.assertEqual(response[1], 'DELETE')

    @mock.patch('ai21.ai21_studio_client.AI21StudioClient.execute_http_request', new=mock_url_from_execute_http_request)
    def test_completion__when_provided_with_ai21_destination__should_perform_ai21_request(self):
        ai21.Completion.execute(model="j2-light", prompt='test prompt', destination=AI21Destination())
        response = MOCK_HTTP_RESPONSES.pop()
        self.assertEqual(response[0], 'https://api.ai21.com/studio/v1/j2-light/complete')
        self.assertEqual(response[1], 'POST')

        ai21.Completion.execute(model="j2-light", custom_model='test-custom-model', prompt='test prompt')
        response = MOCK_HTTP_RESPONSES.pop()
        self.assertEqual(response[0], 'https://api.ai21.com/studio/v1/j2-light/test-custom-model/complete')
        self.assertEqual(response[1], 'POST')
