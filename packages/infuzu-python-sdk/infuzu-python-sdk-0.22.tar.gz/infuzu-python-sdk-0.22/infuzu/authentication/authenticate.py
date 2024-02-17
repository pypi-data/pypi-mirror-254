from .requests import Application


def application_is_valid(application: any) -> bool:
    if not isinstance(application, Application):
        return False
    return True


def application_is_internal(application: any) -> bool:
    if not application_is_valid(application):
        return False
    if not application.is_internal:
        return False
    return True


def application_is_in_list(application: any, app_ids: list[str]) -> bool:
    if not application_is_valid(application):
        return False
    if application.id not in app_ids:
        return False
    return True
