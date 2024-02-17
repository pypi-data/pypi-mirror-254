import json
import unittest
from typing import Optional, Dict, cast
from unittest import mock

import boto3

import ai21
from ai21.errors import UnsupportedDestinationException
from ai21.modules.resources.nlp_task import NLPTask


def mock_invoke_sm_endpoint(
        endpoint_name: str,
        input_json: str,
        sm_session: Optional["sagemaker.session.Session"] = None,
):
    return endpoint_name, input_json, sm_session


class TestSagemakerUrls(unittest.TestCase):

    def setUp(self):
        ai21.aws_region = 'us-east-1'
        ai21.api_key = 'test_api_key'

    def tearDown(self):
        ai21.api_key = None
        ai21.aws_region = None
        ai21.organization = None
        ai21.application = None
        ai21.timeout_sec = None
        ai21.num_retries = None

    @mock.patch('ai21.AWS_utils.invoke_sm_endpoint', new=mock_invoke_sm_endpoint)
    def test__completion_execute__when_provided_with_an_endpoint__should_use_provided_endpoint(self):
        response = ai21.Completion.execute(sm_endpoint='test-endpoint', prompt='test prompt')
        self.assertEqual(response[0], 'test-endpoint')
        self.assertEqual(response[1], json.dumps({"prompt": "test prompt", "stopSequences": []}))

    @mock.patch('ai21.AWS_utils.invoke_sm_endpoint', new=mock_invoke_sm_endpoint)
    def test__completion_execute__when_provided_with_a_sm_destination__should_use_provided_endpoint(self):
        response = ai21.Completion.execute(
            destination=ai21.SageMakerDestination(endpoint_name='test-endpoint'),
            prompt='test prompt',
        )

        self.assertEqual(response[0], 'test-endpoint')
        self.assertEqual(response[1], json.dumps({"prompt": "test prompt", "stopSequences": []}))

    @mock.patch('ai21.AWS_utils.invoke_sm_endpoint', new=mock_invoke_sm_endpoint)
    def test__completion_execute__when_provided_with_a_sm_destination__should_use_provided_sm_session(self):
        sm_runtime = boto3.client("sagemaker-runtime", region_name=ai21.aws_region)
        response = ai21.Completion.execute(
            destination=ai21.SageMakerDestination(endpoint_name='test-endpoint', sm_session=sm_runtime),
            prompt='test prompt',
        )

        self.assertEqual(response[0], 'test-endpoint')
        self.assertEqual(response[1], json.dumps({"prompt": "test prompt", "stopSequences": []}))
        self.assertEqual(response[2], sm_runtime)

    @mock.patch('ai21.AWS_utils.invoke_sm_endpoint', new=mock_invoke_sm_endpoint)
    def test__answer_execute__when_provided_with_a_sm_destination__should_use_provided_endpoint(self):
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
        ]
        endpoint_name = 'test-endpoint'

        for task_name, task_args in tasks:
            task = cast(NLPTask, getattr(ai21, task_name))

            response = task.execute(
                destination=ai21.SageMakerDestination(endpoint_name=endpoint_name),
                **task_args,
            )

            self.assertEqual(response[0], endpoint_name)
            self.assertEqual(response[1], json.dumps(task_args))

    def test_non_supported_tasks_execute__when_executing_with_bedrock_destination__should_raise_client_exception(self):
        tasks = [("Improvements", dict(
            text="text",
            types=["fluency"],
        )),
                 ]

        for task_name, task_args in tasks:
            task_name = cast(NLPTask, getattr(ai21, task_name))

            with self.assertRaises(UnsupportedDestinationException):
                task_name.execute(
                    prompt='test prompt',
                    destination=ai21.SageMakerDestination(endpoint_name='example-endpoint'),
                    **task_args,
                )
