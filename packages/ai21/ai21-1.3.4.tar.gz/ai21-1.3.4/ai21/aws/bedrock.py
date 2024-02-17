import json
import re
from typing import Optional

import boto3
from botocore.exceptions import ClientError

import ai21
from ai21.errors import NotFound, AccessDenied, APITimeoutError
from ai21.http_client import handle_non_success_response
from ai21.utils import convert_to_ai21_object, log_error

RUNTIME_NAME = "bedrock-runtime"
bedrock_runtime = boto3.client(RUNTIME_NAME, region_name=ai21.aws_region)


def invoke_bedrock_model(model_id: str, input_json: str, bedrock_session: Optional["boto3.Session"]):
    bedrock_session = bedrock_session.client(RUNTIME_NAME) if bedrock_session else bedrock_runtime

    try:
        response = bedrock_session.invoke_model(
            modelId=model_id,
            contentType="application/json",
            accept="application/json",
            body=input_json,
        )

        response_body = json.loads(response.get('body').read())

        return convert_to_ai21_object(response_body)
    except ClientError as client_error:
        handle_bedrock_client_error(client_error)
    except Exception as exception:
        log_error(f"Calling {model_id} failed with Exception: {exception}")
        raise exception


def handle_bedrock_client_error(client_exception: ClientError) -> None:
    error_response = client_exception.response
    error_message = error_response.get("Error", {}).get("Message", "")
    status_code = error_response.get("ResponseMetadata", {}).get("HTTPStatusCode", None)
    # As written in https://docs.aws.amazon.com/bedrock/latest/APIReference/API_runtime_InvokeModel.html

    if status_code == 403:
        raise AccessDenied(details=error_message)

    if status_code == 404:
        raise NotFound(details=error_message)

    if status_code == 408:
        raise APITimeoutError(details=error_message)

    if status_code == 424:
        error_message_template = re.compile(
            r"Received client error \((.*?)\) from primary with message \"(.*?)\". See .* in account .* for more information.")
        model_status_code = int(error_message_template.search(error_message).group(1))
        model_error_message = error_message_template.search(error_message).group(2)
        handle_non_success_response(model_status_code, model_error_message)

    handle_non_success_response(status_code, error_message)
