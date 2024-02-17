"""
utils/api_calls/infuzu.py
This module provides utilities to interact with Infuzu's API.

Dependencies:
    - `PythonAdvancedTyping` for static type checking.
    - `constants` module for default values and constants.
    - `InfuzuCredentials` for generating authentication tokens.
    - `APIResponse` and `api_call` from the base module to handle API interactions.
    - `HttpMethod` from the enums module for HTTP method typing.
"""
from types import NoneType
from PythonAdvancedTyping import check_type
from ... import constants
from ...auth import InfuzuCredentials
from .base import (APIResponse, api_call)
from ..enums.api_calls import HttpMethod


def infuzu_api_call(
        credentials: InfuzuCredentials,
        base_url: str,
        endpoint: str,
        method: HttpMethod,
        timeout: int = constants.DEFAULT_REQUEST_TIMEOUT,
        headers: dict[str, any] = None,
        params: dict[str, any] = None,
        body: dict[str, any] = None
) -> APIResponse:
    """
    Makes an authenticated API call to Infuzu.

    Args:
        credentials (InfuzuCredentials): Infuzu authentication credentials object.
        base_url (str): The base URL for the Infuzu API.
        endpoint (str): The specific API endpoint (e.g., "/users").
        method (HttpMethod): The HTTP method for the API call.
        timeout (int, optional): The maximum duration (in seconds) to wait for a response. Defaults to `DEFAULT_REQUEST_TIMEOUT`.
        headers (dict[str, any], optional): Additional headers to send with the request.
        params (dict[str, any], optional): Query parameters to send with the request.
        body (dict[str, any], optional): The body of the request if applicable.

    Returns:
        APIResponse: An object containing the details of the API response.

    Raises:
        RequestException: If there's an issue with making the request.
        ValueError: For invalid input types.
    """
    if headers is None:
        headers: dict[str, any] = {}
    check_type(
        (credentials, "credentials", InfuzuCredentials),
        (base_url, "base_url", str),
        (endpoint, "endpoint", str),
        (headers, "headers", dict),
        (params, "params", (dict, NoneType)),
        (body, "body", (dict, NoneType)),
        (method, "method", HttpMethod),
        (timeout, "timeout", int)
    )
    url: str = base_url + endpoint
    headers[constants.INFUZU_AUTH_TOKEN_HEADER_NAME] = credentials.infuzu_auth_signature
    return api_call(url=url, method=method, headers=headers, timeout=timeout, body=body)
