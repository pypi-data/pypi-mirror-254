import unittest
from unittest import mock
from unittest.mock import Mock

import ai21
from ai21.errors import ModelPackageDoesntExistException
from ai21.utils import convert_to_ai21_object

MOCK_MODEL_PACKAGE_DICT = convert_to_ai21_object({
    "id": "id",
    "arn": "some-model-package-id1",
})

MOCK_NON_EXISTING_MODEL_PACKAGE_DICT = convert_to_ai21_object({
    "id": "id",
    "arn": None,
})

MOCK_LIST_MODEL_PACKAGE_VERSIONS = convert_to_ai21_object({
    "id": "id",
    "versions": ["1-0-001", "1-0-002", "latest"],
})


class TestSageMakerModule(unittest.TestCase):
    @mock.patch("ai21.ai21_studio_client.AI21StudioClient.execute_http_request")
    def test_get_module_package_id__when_the_model_and_region_exist__should_return_arn(self, mock_request: Mock):
        mock_request.return_value = MOCK_MODEL_PACKAGE_DICT

        self.assertEqual(ai21.SageMaker.get_model_package_arn(model_name="j2-mid", region="us-east-1"),
                         "some-model-package-id1")

        mock_request.assert_called_once()
        self.assertEqual(mock_request.mock_calls[0].kwargs["params"]["version"], "latest")
        self.assertTrue(mock_request.mock_calls[0].kwargs["url"].endswith("get_model_version_arn"))

    @mock.patch("ai21.ai21_studio_client.AI21StudioClient.execute_http_request")
    def test_get_model_package_id__when_the_response_doesnt_contain_arn__should_raise_exception(self,
                                                                                                mock_request: Mock):
        mock_request.return_value = MOCK_NON_EXISTING_MODEL_PACKAGE_DICT

        with self.assertRaises(ModelPackageDoesntExistException):
            ai21.SageMaker.get_model_package_arn(model_name="j2-mid", region="us-east-1",
                                                 version="non-existing_version")

    @mock.patch("ai21.ai21_studio_client.AI21StudioClient.execute_http_request")
    def test_get_model_package_id__when_the_model_doesnt_exist__should_raise_exception(self, mock_request: Mock):
        with self.assertRaises(ModelPackageDoesntExistException):
            ai21.SageMaker.get_model_package_arn(model_name="non-existing_model", region="us-east-1")

        mock_request.assert_not_called()

    @mock.patch("ai21.ai21_studio_client.AI21StudioClient.execute_http_request")
    def test_list_model_package_versions__when_model_doesnt_exist__should_raise_exception(self, mock_request: Mock):
        with self.assertRaises(ModelPackageDoesntExistException):
            ai21.SageMaker.get_model_package_arn(model_name="non-existing_model", region="us-east-1")

        mock_request.assert_not_called()

    @mock.patch("ai21.ai21_studio_client.AI21StudioClient.execute_http_request")
    def test_list_model_package_versions__when_model_exists__should_return_versions(self, mock_request: Mock):
        mock_request.return_value = MOCK_LIST_MODEL_PACKAGE_VERSIONS
        self.assertEqual(ai21.SageMaker.list_model_package_versions(model_name="j2-mid", region="us-east-1"),
                         ["1-0-001", "1-0-002", "latest"])

        self.assertTrue(mock_request.mock_calls[0].kwargs["url"].endswith("list_versions"))
