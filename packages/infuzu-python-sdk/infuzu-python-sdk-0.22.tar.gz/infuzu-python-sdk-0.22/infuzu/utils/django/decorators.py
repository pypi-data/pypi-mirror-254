from typing import Callable
from ...authentication.authenticate import (application_is_valid, application_is_internal, application_is_in_list)
from ...authentication.requests import Application


def ensure_there_is_valid_application(func: Callable) -> Callable:
    def wrapper(request, *args, **kwargs) -> any:
        application: Application | None = getattr(request, 'application', None)
        if not application_is_valid(application):
            from django.http import HttpResponseForbidden
            return HttpResponseForbidden("Access Denied - Signature is invalid")
        return func(request, *args, **kwargs)
    return wrapper


def ensure_application_is_internal(func: Callable) -> Callable:
    def wrapper(request, *args, **kwargs) -> any:
        application: Application | None = getattr(request, 'application', None)
        if not application_is_internal(application):
            from django.http import HttpResponseForbidden
            return HttpResponseForbidden("Access Denied - Signature is invalid")
        return func(request, *args, **kwargs)
    return wrapper


def ensure_valid_application_ids(allowed_app_ids: list[str]) -> Callable:
    def decorator(func: Callable) -> Callable:
        def wrapper(request, *args, **kwargs) -> any:
            application: Application | None = getattr(request, 'application', None)
            if not application_is_in_list(application, allowed_app_ids):
                from django.http import HttpResponseForbidden
                return HttpResponseForbidden("Access Denied - Application ID is not allowed")
            return func(request, *args, **kwargs)
        return wrapper
    return decorator
