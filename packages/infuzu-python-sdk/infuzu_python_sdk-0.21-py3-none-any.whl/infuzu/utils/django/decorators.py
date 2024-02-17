from typing import Callable
from ...authentication.requests import Application


def ensure_there_is_valid_application(func: Callable) -> Callable:
    def wrapper(request, *args, **kwargs) -> any:
        application: Application | None = getattr(request, 'application', None)
        if application is None:
            from django.http import HttpResponseForbidden
            return HttpResponseForbidden("Access Denied - Signature is invalid")
        return func(request, *args, **kwargs)
    return wrapper


def ensure_application_is_internal(func: Callable) -> Callable:
    def wrapper(request, *args, **kwargs) -> any:
        if not request.application.is_internal:
            from django.http import HttpResponseForbidden
            return HttpResponseForbidden("Access Denied - Signature is invalid")
        return func(request, *args, **kwargs)
    return wrapper


def ensure_valid_application_ids(allowed_app_ids: list[str]) -> Callable:
    def decorator(func: Callable) -> Callable:
        def wrapper(request, *args, **kwargs) -> any:
            application = getattr(request, 'application', None)
            if application is None or application.id not in allowed_app_ids:
                from django.http import HttpResponseForbidden
                return HttpResponseForbidden("Access Denied - Application ID is not allowed")
            return func(request, *args, **kwargs)
        return wrapper
    return decorator
