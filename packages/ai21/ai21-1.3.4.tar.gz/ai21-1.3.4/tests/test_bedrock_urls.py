import json
import unittest
from typing import Optional, Dict, Any, Tuple, cast
from unittest import mock
from unittest.mock import Mock

import boto3

import ai21
from ai21.errors import UnsupportedDestinationException
from ai21.modules.resources.nlp_task import NLPTask


# noinspection PyUnusedLocal
def mock_url_from_execute_http_request(model_id: str, input_json: str, bedrock_session: Optional[boto3.Session]) -> \
        Tuple[str, Dict[str, Any], Optional[boto3.Session]]:
    return model_id, json.loads(input_json), bedrock_session


BEDROCK_INVOKE_PATCH_PATH = "ai21.aws.bedrock.invoke_bedrock_model"


class TestBedrockUrls(unittest.TestCase):

    def setUp(self):
        ai21.aws_region = 'us-east-1'

    def tearDown(self):
        ai21.api_key = None
        ai21.organization = None
        ai21.application = None
        ai21.timeout_sec = None
        ai21.num_retries = None

    @mock.patch(BEDROCK_INVOKE_PATCH_PATH, new=mock_url_from_execute_http_request)
    def test_bedrock_completion(self):
        model_id, response, boto_session = ai21.Completion.execute(
            prompt='test prompt',
            destination=ai21.BedrockDestination(model_id=ai21.BedrockModelID.J2_ULTRA),
        )

        self.assertEqual(model_id, ai21.BedrockModelID.J2_ULTRA_V1)
        self.assertDictEqual(response, {'prompt': 'test prompt', 'stopSequences': []})
        self.assertIsNone(boto_session)

    @mock.patch(BEDROCK_INVOKE_PATCH_PATH, new=mock_url_from_execute_http_request)
    def test_bedrock_completion__when_using_a_deprecated_model__it_gets_remapped(self):
        for deprecated_model_id, new_model_id in [
            (ai21.BedrockModelID.J2_JUMBO_INSTRUCT, ai21.BedrockModelID.J2_ULTRA_V1),
            (ai21.BedrockModelID.J2_GRANDE_INSTRUCT, ai21.BedrockModelID.J2_MID_V1),
            (ai21.BedrockModelID.J2_MID, ai21.BedrockModelID.J2_MID_V1),
            (ai21.BedrockModelID.J2_ULTRA, ai21.BedrockModelID.J2_ULTRA_V1),
        ]:
            model_id, response, boto_session = ai21.Completion.execute(
                prompt='test prompt',
                destination=ai21.BedrockDestination(model_id=deprecated_model_id),
            )

            self.assertEqual(model_id, new_model_id)
            self.assertDictEqual(response, {'prompt': 'test prompt', 'stopSequences': []})
            self.assertIsNone(boto_session)

    @mock.patch(BEDROCK_INVOKE_PATCH_PATH, new=mock_url_from_execute_http_request)
    def test_bedrock_completion_with_custom_boto_session(self):
        mock_boto_session = Mock()
        model_id, response, boto_session = ai21.Completion.execute(
            prompt='test prompt',
            destination=ai21.BedrockDestination(model_id=ai21.BedrockModelID.J2_ULTRA, boto_session=mock_boto_session),
        )

        self.assertEqual(model_id, ai21.BedrockModelID.J2_ULTRA_V1)
        self.assertDictEqual(response, {'prompt': 'test prompt', 'stopSequences': []})
        self.assertEqual(mock_boto_session, boto_session)

    def test_non_supported_tasks_execute__when_executing_with_bedrock_destination__should_raise_client_exception(self):
        tasks = [
            ("Answer", dict(
                context='context',
                question='question',
            )),
            ("Summarize", dict(
                sourceType='sourceType',
                source='source',
            )),
            ("Paraphrase", dict(
                text='text'
            )),
            ("GEC", dict(
                text='text'
            )),
            ("Paraphrase", dict(
                text='text'
            )),
            ("Improvements", dict(
                text="text",
                types=["fluency"],
            )),
        ]

        for task_name, task_args in tasks:
            task_name = cast(NLPTask, getattr(ai21, task_name))

            with self.assertRaises(UnsupportedDestinationException):
                task_name.execute(
                    prompt='test prompt',
                    destination=ai21.BedrockDestination(model_id=ai21.BedrockModelID.J2_ULTRA),
                    **task_args,
                )
