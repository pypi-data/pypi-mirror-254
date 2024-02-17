from ..authentication.requests import (AuthenticationKey, get_application_information, Application)
from ..authentication.shortcuts import get_key_pair_id_from_signature, verify_message_signature


def convert_message_signature_to_application_and_verify(message_signature: str, message: str) -> Application | None:
    pair_id: str = get_key_pair_id_from_signature(message_signature)
    if not pair_id:
        return None
    authentication_key: AuthenticationKey = get_application_information(pair_id)
    if not authentication_key.public_key_b64:
        return None
    sig_is_valid: bool = verify_message_signature(message, message_signature, authentication_key.public_key_b64)
    if not sig_is_valid:
        return None
    return authentication_key.application
