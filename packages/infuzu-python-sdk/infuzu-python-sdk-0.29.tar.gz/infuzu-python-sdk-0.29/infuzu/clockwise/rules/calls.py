from requests import Response
from .execution_log import Execution
from ... import constants
from .base import Rule
from ...http_requests import signed_requests


def create_rule(rule_instance: Rule) -> str:
    api_response: Response = signed_requests.post(
        url=f"{constants.CLOCKWISE_BASE_URL}{constants.CLOCKWISE_CREATE_RULE_ENDPOINT}",
        json=rule_instance.to_create_rule_dict()
    )

    if api_response.status_code == 200:
        rule_id: str = api_response.json()["rule_id"]
        return rule_id


def delete_rule(rule_id: str) -> bool:
    api_response: Response = signed_requests.delete(
        url=f'{constants.CLOCKWISE_BASE_URL}'
            f'{constants.CLOCKWISE_DELETE_RULE_ENDPOINT.replace("<str:rule_id>", rule_id)}'
    )

    if api_response.status_code == 200:
        return True
    else:
        return False


def get_rule_logs(rule_id: str) -> list[Execution]:
    api_response: Response = signed_requests.get(
        url=f'{constants.CLOCKWISE_BASE_URL}'
            f'{constants.CLOCKWISE_RULE_LOGS_ENDPOINT.replace("<str:rule_id>", rule_id)}'
    )

    if api_response.status_code == 200:
        return Execution.from_logs_api_call(api_response.json())
