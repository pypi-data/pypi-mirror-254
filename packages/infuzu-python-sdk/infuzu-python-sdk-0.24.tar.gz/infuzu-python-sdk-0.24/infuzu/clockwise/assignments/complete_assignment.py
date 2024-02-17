"""
clockwise/complete_assignment.py
This module provides utilities to mark an assignment as complete in Clockwise using the Infuzu authentication.

Dependencies:
    - `datetime` from Python standard library for date and time management.
    - `PythonAdvancedTyping` for static type checking.
    - `constants` module for default values and constants, including CLOCKWISE_ASSIGNMENT_COMPLETE_ENDPOINT.
    - `HttpMethod` from the enums module for HTTP method typing.
    - `InfuzuCredentials` for Clockwise authentication.
    - `clockwise_api_call` for interacting with the Clockwise API.
    - `APIResponse` for handling API responses.
    - `Assignment` from the `retrieve_assignment` module for assignment representation.
"""

from datetime import (datetime, timezone)
from PythonAdvancedTyping import check_type
from ... import constants
from ...utils.enums.api_calls import HttpMethod
from ...auth import InfuzuCredentials
from ...utils.api_calls.clockwise import clockwise_api_call
from ...utils.api_calls.base import APIResponse
from .retrieve_assignment import Assignment


class CompleteAssignment:
    """
    Represents a completed assignment in Clockwise.

    Attributes:
        assignment (Assignment): The fetched assignment from Clockwise.
        start_datetime (datetime): The start time of the assignment execution.
        end_datetime (datetime): The end time of the assignment execution.
        response (APIResponse): The response from executing the assignment.
    """
    def __init__(
            self, assignment: Assignment, start_datetime: datetime, end_datetime: datetime, response: APIResponse
    ) -> None:
        check_type(
            (assignment, "assignment", Assignment),
            (start_datetime, "start_datetime", datetime),
            (end_datetime, "end_datetime", datetime),
            (response, "response", APIResponse)
        )
        self.assignment: Assignment = assignment
        self.start_datetime: datetime = start_datetime
        self.end_datetime: datetime = end_datetime
        self.response: APIResponse = response

    def to_assignment_completion_dict(self) -> dict[str, any]:
        """
        Convert the complete assignment to a dictionary format.

        Returns:
            dict[str, any]: Dictionary representation of the complete assignment.
        """
        return {
            "rule_id": self.assignment.rule_id,
            "start_datetime": self.start_datetime.isoformat(),
            "end_datetime": datetime.utcnow().replace(tzinfo=timezone.utc).isoformat(),
            "request_details": self.assignment.to_dict(),
            "response_details": self.response.response_dict,
            "execution_details": self.response.execution_dict
        }


def assignment_complete(credentials: InfuzuCredentials, complete_assignment: CompleteAssignment) -> None:
    """
    Marks an assignment as complete in Clockwise using the given credentials and assignment details.

    Args:
        credentials (InfuzuCredentials): Clockwise authentication credentials object.
        complete_assignment (CompleteAssignment): Object representing the completed assignment.

    Note:
        This function doesn't return anything. If the API call is successful, the assignment is marked as complete.
        Otherwise, the caller should handle exceptions raised by the `clockwise_api_call`.
    """
    check_type(
        (credentials, "credentials", InfuzuCredentials),
        (complete_assignment, "complete_assignment", CompleteAssignment)
    )

    headers: dict[str, str] = {"Content-Type": "application/json"}

    clockwise_api_call(
        credentials=credentials,
        endpoint=constants.CLOCKWISE_ASSIGNMENT_COMPLETE_ENDPOINT,
        headers=headers,
        method=HttpMethod.POST,
        body=complete_assignment.to_assignment_completion_dict()
    )
