import json
import time
from types import NoneType
import requests
from PythonAdvancedTyping import check_type
from .serialize import class_str_serializer
from ..enums.api_calls import HttpMethod


class APIResponse:
    """
    Wrapper class around the response object returned by the requests library.

    Attributes:
        response_object (requests.Response): The raw response object from the requests library.
        attempts_count (int): The number of attempts made to get the response.

    Methods:
        success: Property indicating if the response was successful (HTTP 200).
        response_dict: Property returning the response details as a dictionary.
        execution_dict: Property returning details about the execution (e.g., attempts).
    """

    def __init__(self, response_object: requests.Response, attempts_count: int) -> None:
        """
        Initialize an APIResponse instance.

        Args:
            response_object (requests.Response): The raw response object.
            attempts_count (int): The number of attempts made to get the response.
        """
        check_type((response_object, "response_object", requests.Response), (attempts_count, "attempts_count", int))
        self.response_object: requests.Response = response_object
        self.attempts_count: int = attempts_count

    @property
    def success(self) -> bool:
        return self.response_object.status_code == 200

    @property
    def response_dict(self) -> dict[str, any]:
        return {
            "status_code": self.response_object.status_code,
            "headers": self._headers_dict,
            "content": self._content,
            "url": self.response_object.url,
            "history": [{"url": resp.url, "status": resp.status_code} for resp in self.response_object.history],
            "encoding": self.response_object.encoding,
            "elapsed": str(self.response_object.elapsed),
            "cookies": self._cookies_dict,
        }

    @property
    def execution_dict(self) -> dict[str, any]:
        return {
            "attempts": self.attempts_count
        }

    @property
    def _headers_dict(self) -> dict[str, any]:
        return dict(self.response_object.headers)

    @property
    def _cookies_dict(self) -> dict[str, any]:
        cookies_dict: dict[str, any] = {}
        for cookie in self.response_object.cookies:
            cookies_dict[cookie.name] = cookie.value
        return cookies_dict

    @property
    def _content(self) -> str:
        try:
            if 'json' in self._headers_dict.get('content-type', ''):
                content: str = self.response_object.json()
            else:
                content: str = self.response_object.text
        except (json.JSONDecodeError, UnicodeDecodeError):
            content: str = "Error decoding content"
        return content

    @property
    def response_content(self) -> any:
        try:
            if 'json' in self._headers_dict.get('Content-Type', ''):
                return self.response_object.json()
            else:
                return self.response_object.text
        except (json.JSONDecodeError, UnicodeDecodeError):
            return "Error decoding content"


def api_call(
        url: str,
        headers: dict | None,
        params: dict | None = None,
        body: dict | None = None,
        method: HttpMethod = HttpMethod.GET,
        tries: int = 1,
        retry_wait: int = 0,
        timeout: int = 10
) -> APIResponse:
    """
    Make an API call with the provided details and retry mechanism.

    Args:
        url (str): The API endpoint to call.
        headers (dict | None): Dictionary containing headers for the API request.
        params (dict | None, optional): Dictionary containing query parameters for the API request. Defaults to None.
        body (dict | None, optional): Dictionary containing request body (used for POST, PUT, etc.). Defaults to None.
        method (HttpMethod, optional): The HTTP method to use. Defaults to HttpMethod.GET.
        tries (int, optional): The number of tries to attempt the call. Defaults to 1.
        retry_wait (int, optional): The number of seconds to wait between retries. Defaults to 0.
        timeout (int, optional): The timeout for the API call in seconds. Defaults to 10.

    Returns:
        APIResponse: A wrapper around the response object with additional metadata.
    """
    check_type(
        (url, "url", str),
        (headers, "headers", (dict, NoneType)),
        (params, "params", (dict, NoneType)),
        (body, "body", (dict, NoneType)),
        (method, "method", HttpMethod),
        (tries, "tries", int),
        (retry_wait, "retry_wait", int),
        (timeout, "timeout", int)
    )
    attempts_made: int = 0
    while attempts_made < tries:
        attempts_made += 1
        try:
            if body is None:
                json_body: None = None
            else:
                json_body: str = json.dumps(body, default=class_str_serializer)
            response: requests.Response = requests.request(
                method.name, url, headers=headers, params=params, data=json_body, timeout=timeout
            )
            if attempts_made < tries:
                response.raise_for_status()
            return APIResponse(response, attempts_made)
        except requests.ConnectionError:
            print("Failed to connect to the URL.")
            if attempts_made < tries:
                print(f"Attempt {attempts_made} failed due to connection error. Retrying in {retry_wait} seconds...")
                time.sleep(retry_wait)
            else:
                custom_response_data: dict[str, any] = {
                    "status_code": 503, "content": "Failed to connect after all attempts.",
                }
                custom_response: requests.Response = requests.Response()
                for key, value in custom_response_data.items():
                    setattr(custom_response, key, value)
                return APIResponse(custom_response, attempts_made)
        except requests.TooManyRedirects:
            print("Too many redirects.")
            if attempts_made < tries:
                print(f"Attempt {attempts_made} failed due to too many redirects. Retrying in {retry_wait} seconds...")
                time.sleep(retry_wait)
            else:
                custom_response_data: dict[str, any] = {
                    "status_code": 508, "content": "Too many redirects after all attempts.",
                }
                custom_response: requests.Response = requests.Response()
                for key, value in custom_response_data.items():
                    setattr(custom_response, key, value)
                return APIResponse(custom_response, attempts_made)
        except requests.RequestException:
            if attempts_made < tries:
                print(f"Attempt {attempts_made} failed. Retrying in {retry_wait} seconds...")
                time.sleep(retry_wait)
            else:
                try:
                    # noinspection PyUnboundLocalVariable
                    return APIResponse(response, attempts_made)
                except NameError:
                    print("An unexpected error occurred. Unable to get a response.")
                    custom_response_data: dict[str, any] = {
                        "status_code": 500, "content": "An unexpected error occurred after all attempts.",
                    }
                    custom_response: requests.Response = requests.Response()
                    for key, value in custom_response_data.items():
                        setattr(custom_response, key, value)
                    return APIResponse(custom_response, attempts_made)

    custom_response_data: dict[str, any] = {"status_code": 400, "content": "Unexpected failure"}
    custom_response: requests.Response = requests.Response()
    for key, value in custom_response_data.items():
        setattr(custom_response, key, value)
    return APIResponse(custom_response, attempts_made)
