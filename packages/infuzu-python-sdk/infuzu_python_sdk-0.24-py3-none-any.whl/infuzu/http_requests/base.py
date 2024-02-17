import json
import requests
from ..authentication.shortcuts import (generate_message_signature, SIGNATURE_HEADER_NAME)


class SignatureSession(requests.Session):
    def request(self, method, url, **kwargs):
        request_body: any = kwargs.get("data") or kwargs.get("json", '')
        if not isinstance(request_body, str):
            request_body: str = json.dumps(request_body)
        signature: str = generate_message_signature(request_body)

        if 'headers' in kwargs:
            kwargs['headers'][SIGNATURE_HEADER_NAME] = signature
        else:
            kwargs['headers'] = {SIGNATURE_HEADER_NAME: signature}

        return super().request(method, url, **kwargs)


signed_requests: SignatureSession = SignatureSession()
