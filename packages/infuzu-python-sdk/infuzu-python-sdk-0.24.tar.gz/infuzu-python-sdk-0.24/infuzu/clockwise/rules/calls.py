from PythonAdvancedTyping import check_type
from .execution_log import Execution
from ... import constants
from ...auth import InfuzuCredentials
from .base import Rule
from ...utils.api_calls.base import APIResponse
from ...utils.api_calls.clockwise import clockwise_api_call
from ...utils.enums.api_calls import HttpMethod


def create_rule(credentials: InfuzuCredentials, rule_instance: Rule) -> str:
    check_type(
        (credentials, "credentials", InfuzuCredentials),
        (rule_instance, "rule_instance", Rule)
    )

    headers: dict[str, str] = {"Content-Type": "application/json"}

    api_response: APIResponse = clockwise_api_call(
        credentials=credentials,
        endpoint=constants.CLOCKWISE_CREATE_RULE_ENDPOINT,
        headers=headers,
        method=HttpMethod.POST,
        body=rule_instance.to_create_rule_dict()
    )

    if api_response.success:
        rule_id: str = api_response.response_content["rule_id"]
        return rule_id


def delete_rule(credentials: InfuzuCredentials, rule_id: str) -> bool:
    check_type(
        (credentials, "credentials", InfuzuCredentials),
        (rule_id, "rule_id", str)
    )

    api_response: APIResponse = clockwise_api_call(
        credentials=credentials,
        endpoint=constants.CLOCKWISE_DELETE_RULE_ENDPOINT.replace("<str:rule_id>", rule_id),
        method=HttpMethod.DELETE
    )

    if api_response.success:
        return True
    else:
        return False


def get_rule_logs(credentials: InfuzuCredentials, rule_id: str) -> list[Execution]:
    check_type(
        (credentials, "credentials", InfuzuCredentials),
        (rule_id, "rule_id", str)
    )

    api_response: APIResponse = clockwise_api_call(
        credentials=credentials,
        endpoint=constants.CLOCKWISE_RULE_LOGS_ENDPOINT.replace("<str:rule_id>", rule_id),
        method=HttpMethod.GET
    )

    if api_response.success:
        return Execution.from_logs_api_call(api_response.response_content)
