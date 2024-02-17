from datetime import datetime
from PythonAdvancedTyping import check_type


class Execution:
    def __init__(
            self,
            task_id: str,
            rule_id: str,
            start_datetime: datetime,
            end_datetime: datetime,
            request_details: dict[str, any],
            response_details: dict[str, any],
            execution_details: dict[str, any]
    ) -> None:
        check_type(
            (task_id, "task_id", str),
            (rule_id, "rule_id", str),
            (start_datetime, "start_datetime", datetime),
            (end_datetime, "end_datetime", datetime),
            (request_details, "request_details", dict),
            (response_details, "response_details", dict),
            (execution_details, "execution_details", dict),
        )
        self.task_id: str = task_id
        self.rule_id: str = rule_id
        self.start_datetime: datetime = start_datetime
        self.end_datetime: datetime = end_datetime
        self.request_details: dict[str, any] = request_details
        self.response_details: dict[str, any] = response_details
        self.execution_details: dict[str, any] = execution_details

    @classmethod
    def from_logs_api_call(cls, execution_log_list: list[dict[str, any]]) -> list['Execution']:
        check_type(execution_log_list, "execution_log_list", list)
        executions_list: list['Execution'] = []
        for execution_log in execution_log_list:
            check_type(execution_log, "execution_log", dict)
            executions_list.append(
                cls(
                    task_id=execution_log["task_id"],
                    rule_id=execution_log["rule_id"],
                    start_datetime=datetime.fromisoformat(execution_log["start_datetime"]),
                    end_datetime=datetime.fromisoformat(execution_log["end_datetime"]),
                    request_details=execution_log["request_details"],
                    response_details=execution_log["response_details"],
                    execution_details=execution_log["execution_details"]
                )
            )
        return executions_list
