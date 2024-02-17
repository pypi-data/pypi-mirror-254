from datetime import (timedelta, datetime, timezone)
from types import NoneType
from PythonAdvancedTyping import check_type
from ...utils.enums.api_calls import HttpMethod


class Rule:
    def __init__(
            self,
            name: str,
            url: str,
            rule_id: str | None = None,
            interval: timedelta = timedelta(days=1),
            start_datetime: datetime = datetime.utcnow().replace(tzinfo=timezone.utc),
            end_datetime: datetime | None = None,
            max_executions: int | None = None,
            http_method: HttpMethod = HttpMethod.GET,
            headers: dict | None = None,
            body: dict | None = None,
            max_retries: int = 0,
            timeout: int = 30,
            static: bool = False
    ) -> None:
        check_type(
            (name, "name", str),
            (url, "url", str),
            (rule_id, "rule_id", (str, NoneType)),
            (interval, "interval", timedelta),
            (start_datetime, "start_datetime", datetime),
            (end_datetime, "end_datetime", (datetime, NoneType)),
            (max_executions, "max_executions", (int, NoneType)),
            (http_method, "http_method", HttpMethod),
            (headers, "headers", (dict, NoneType)),
            (body, "body", (dict, NoneType)),
            (max_retries, "max_retries", int),
            (timeout, "timeout", int),
            (static, "static", bool)
        )
        self.name: str = name
        self.url: str = url
        self.rule_id: str | None = rule_id
        self.interval: timedelta = interval
        self.start_datetime: datetime = start_datetime
        self.end_datetime: datetime | None = end_datetime
        self.max_executions: int | None = max_executions
        self.http_method: HttpMethod = http_method
        self.headers: dict | None = headers
        self.body: dict | None = body
        self.max_retries: int = max_retries
        self.timeout: int = timeout
        self.static: bool = static

    def to_create_rule_dict(self) -> dict[str, any]:
        return {
            "rule_id": self.rule_id,
            "name": self.name,
            "interval": self.interval.total_seconds(),
            "start_datetime": self.start_datetime.isoformat(),
            "end_datetime": self.end_datetime.isoformat() if isinstance(self.end_datetime, datetime) else None,
            "max_executions": self.max_executions,
            "url": self.url,
            "http_method": self.http_method.name,
            "headers": self.headers,
            "body": self.body,
            "max_retries": self.max_retries,
            "timeout": self.timeout,
            "static": self.static
        }
