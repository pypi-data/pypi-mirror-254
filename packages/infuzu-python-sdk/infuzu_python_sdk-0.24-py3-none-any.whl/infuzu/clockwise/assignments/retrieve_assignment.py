"""
clockwise/retrieve_assignment.py
This module provides utilities to retrieve assignments from Clockwise using the Infuzu authentication.

Dependencies:
    - `PythonAdvancedTyping` for static type checking.
    - `constants` module for default values and constants, including CLOCKWISE_RETRIEVE_ASSIGNMENT_ENDPOINT.
    - `InfuzuCredentials` for Clockwise authentication.
    - `HttpMethod` from the enums module for HTTP method typing.
    - `clockwise_api_call` for interacting with the Clockwise API.
    - `NoContentError` for error handling when no content is available.
    - `APIResponse` for handling API responses.
"""
from types import NoneType
from PythonAdvancedTyping import check_type
from ... import constants
from ...auth import InfuzuCredentials
from ...utils.enums.api_calls import HttpMethod
from ...utils.api_calls.clockwise import clockwise_api_call
from ..errors import NoContentError
from ...utils.api_calls.base import APIResponse


class Assignment:
    """
    Represents an Assignment fetched from Clockwise.

    Attributes:
        rule_id (str): The rule ID for the assignment.
        url (str): URL for the assignment.
        http_method (HttpMethod): The HTTP method for the API call.
        headers (dict[str, any] | None): Headers for the API call.
        body (dict[str, any] | None): Body of the request if applicable.
        max_retries (int): Maximum number of retries.
        timeout (int): Maximum duration (in seconds) to wait for a response.
    """
    def __init__(
            self,
            rule_id: str,
            url: str,
            http_method: HttpMethod = HttpMethod.GET,
            headers: dict[str, any] | None = None,
            body: dict[str, any] | None = None,
            max_retries: int = 0,
            timeout: int = 30
    ) -> None:
        check_type(
            (rule_id, "rule_id", str),
            (url, "url", str),
            (http_method, "http_method", HttpMethod),
            (headers, "headers", (dict, NoneType)),
            (body, "body", (dict, NoneType)),
            (max_retries, "max_retries", int),
            (timeout, "timeout", int)
        )
        self.rule_id: str = rule_id
        self.url: str = url
        self.http_method: HttpMethod = http_method
        self.headers: dict[str, any] | None = headers
        self.body: dict[str, any] | None = body
        self.max_retries: int = max_retries
        self.timeout: int = timeout

    @classmethod
    def from_dict(cls, assignment_dict: dict[str, any]) -> 'Assignment':
        """
        Instantiate an Assignment from a dictionary.

        Args:
            assignment_dict (dict[str, any]): Dictionary with assignment details.

        Returns:
            Assignment: An instantiated Assignment object.
        """
        check_type(assignment_dict, "assignment_dict", dict)
        rule_id: str = assignment_dict.get("rule_id")
        url: str = assignment_dict.get("url")
        http_method: str = assignment_dict.get("http_method")
        headers: dict[str, any] | None = assignment_dict.get("headers")
        body: dict[str, any] | None = assignment_dict.get("body")
        max_retries: int = assignment_dict.get("max_retries")
        timeout: int = assignment_dict.get("timeout")

        check_type(
            (rule_id, "rule_id", str),
            (url, "url", str),
            (http_method, "http_method", str),
            (headers, "headers", (dict, NoneType)),
            (body, "body", (dict, NoneType)),
            (max_retries, "max_retries", int),
            (timeout, "timeout", int)
        )

        http_method: HttpMethod = HttpMethod.from_name(http_method)

        return cls(
            rule_id=rule_id,
            url=url,
            http_method=http_method,
            headers=headers,
            body=body,
            max_retries=max_retries,
            timeout=timeout
        )

    @classmethod
    def from_api_response(cls, api_response: APIResponse) -> 'Assignment':
        check_type(api_response, "api_response", APIResponse)
        if api_response.response_object.status_code == 200:
            return cls.from_dict(api_response.response_content)
        else:
            raise ValueError("Invalid status for an assignment.")

    def to_dict(self) -> dict[str, any]:
        return {
            "rule_id": self.rule_id,
            "url": self.url,
            "http_method": self.http_method,
            "headers": self.headers,
            "body": self.body,
            "max_retries": self.max_retries,
            "timeout": self.timeout
        }


def get_assignment(credentials: InfuzuCredentials) -> Assignment:
    """
    Fetches an assignment from Clockwise using the given credentials.

    Args:
        credentials (InfuzuCredentials): Clockwise authentication credentials object.

    Returns:
        Assignment: An instantiated Assignment object if successful.

    Raises:
        NoContentError: If the API call returns a 204 status code (No Content).
        ValueError: For invalid status codes or invalid input types.
    """
    check_type(credentials, "credentials", InfuzuCredentials)
    response: APIResponse = clockwise_api_call(
        credentials=credentials, endpoint=constants.CLOCKWISE_RETRIEVE_ASSIGNMENT_ENDPOINT, method=HttpMethod.GET
    )
    if response.response_object.status_code == 204:
        raise NoContentError()
    if response.response_object.status_code == 200:
        return Assignment.from_api_response(response)
    else:
        raise ValueError(
            f"Status Code: {response.response_object.status_code}, Content: {response.response_object.json()}"
        )
