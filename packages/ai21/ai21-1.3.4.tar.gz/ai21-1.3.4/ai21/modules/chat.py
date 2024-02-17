from typing import List

from ai21.modules.resources.execution_utils import execute_studio_request
from ai21.modules.resources.nlp_task import NLPTask
from ai21.utils import validate_mandatory_field


class Chat(NLPTask):
    MODULE_NAME = "chat"

    @classmethod
    def _get_call_name(cls) -> str:
        return cls.MODULE_NAME

    @classmethod
    def _validate_params(cls, params):
        validate_mandatory_field(key="system", call_name=cls.MODULE_NAME, params=params, validate_type=True,
                                 expected_type=str)
        validate_mandatory_field(key="messages", call_name=cls.MODULE_NAME, params=params, validate_type=True,
                                 expected_type=List)
        for message in params["messages"]:
            validate_mandatory_field(key="text", call_name=cls.MODULE_NAME, params=message, validate_type=True,
                                     expected_type=str)
            validate_mandatory_field(key="role", call_name=cls.MODULE_NAME, params=message, validate_type=True,
                                     expected_type=str)

    @classmethod
    def _execute_studio_api(cls, params):
        validate_mandatory_field(key="model", call_name=cls._get_call_name(), params=params, validate_type=True,
                                 expected_type=str)
        model = params.get("model", None)

        return execute_studio_request(task_url=f"{cls.get_base_url(**params)}/{model}/{cls.MODULE_NAME}",
                                      params=params)
