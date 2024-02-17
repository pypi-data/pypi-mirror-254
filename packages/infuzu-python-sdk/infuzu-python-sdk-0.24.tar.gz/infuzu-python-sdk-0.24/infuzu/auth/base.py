"""
auth/base.py
This module contains classes for managing and generating authentication credentials for Infuzu.

Dependencies:
    - Encryption utilities from `..utils.encryption`.
    - Random utilities from `..utils.random`.
"""

import json
from datetime import (datetime, timezone)
from PythonAdvancedTyping import check_type
from ..utils.encryption import compute_sha256
from ..utils.random import create_uuid_without_dash


class InfuzuCredentials:
    """
    Represents authentication credentials for Infuzu with methods for signature generation.

    Attributes:
        secret_id (str): The secret ID provided by Infuzu.

    Properties:
        infuzu_auth_signature: Generates the Infuzu authentication signature.

    Methods:
        from_file: Class method to create an InfuzuCredentials instance from a JSON file.
        from_dict: Class method to create an InfuzuCredentials instance from a dictionary.
    """

    def __init__(self, secret_id: str, secret_key: str) -> None:
        """
        Initialize the InfuzuCredentials instance.

        Args:
            secret_id (str): The secret ID provided by Infuzu.
            secret_key (str): The secret key provided by Infuzu.
        """
        check_type((secret_id, "secret_id", str), (secret_key, "secret_key", str))
        self.secret_id: str = secret_id
        self._secret_key: str = secret_key

    def __str__(self) -> str:
        return f"Infuzu Credentials Instance: secret_id: {self.secret_id}"

    @property
    def infuzu_auth_signature(self) -> str:
        self._refresh_i_auth_token_part_one()
        return f"{self._i_auth_token_part_one}, Hashed Secret: {self._hashed_secret}"

    @property
    def _i_code(self) -> str:
        return create_uuid_without_dash()

    @property
    def _timestamp_str(self) -> str:
        return datetime.utcnow().replace(tzinfo=timezone.utc).isoformat()

    @property
    def _hashed_secret(self) -> str:
        prehashed_str: str = f"{self._i_auth_token_part_one}, Secret Key {self._secret_key}"
        return compute_sha256(prehashed_str)

    def _refresh_i_auth_token_part_one(self):
        self._i_auth_token_part_one: str = \
            f"Secret ID: {self.secret_id}, TimeStamp: {self._timestamp_str}, I Code: {self._i_code}"

    @classmethod
    def from_file(cls, filepath: str) -> 'InfuzuCredentials':
        """
        Create an InfuzuCredentials instance from a JSON file.

        Args:
            filepath (str): The path to the JSON file containing secret_id and secret_key.

        Returns:
            InfuzuCredentials: A new InfuzuCredentials instance.

        Raises:
            ValueError: If the file does not contain both 'secret_id' and 'secret_key'.
        """
        check_type(filepath, "filepath", str)
        with open(filepath, 'r') as f:
            data: dict[str, any] = json.load(f)
        secret_id: str | None = data.get("secret_id")
        secret_key: str | None = data.get("secret_key")
        if not secret_id or not secret_key:
            raise ValueError("File must contain both 'secret_id' and 'secret_key'.")
        return cls(secret_id, secret_key)

    @classmethod
    def from_dict(cls, data: dict[str, str]) -> 'InfuzuCredentials':
        """
        Create an InfuzuCredentials instance from a dictionary.

        Args:
            data (dict[str, str]): A dictionary containing secret_id and secret_key.

        Returns:
            InfuzuCredentials: A new InfuzuCredentials instance.

        Raises:
            ValueError: If the dictionary does not contain both 'secret_id' and 'secret_key'.
        """
        check_type(data, "data", dict)
        secret_id: str | None = data.get("secret_id")
        secret_key: str | None = data.get("secret_key")
        if not secret_id or not secret_key:
            raise ValueError("Dictionary must contain both 'secret_id' and 'secret_key'.")
        return cls(secret_id, secret_key)
