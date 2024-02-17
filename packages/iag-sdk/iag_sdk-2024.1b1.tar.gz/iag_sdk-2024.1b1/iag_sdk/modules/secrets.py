from typing import Optional, Union

from iag_sdk.client_base import ClientBase
from iag_sdk.models import SecretAddParameters


class Secret(ClientBase):
    """
    Class that contains methods for the IAG Secrets API routes.
    """

    def __init__(
        self,
        host: str,
        username: str,
        password: str,
        base_url: Optional[str] = "/api/v2.0",
        protocol: Optional[str] = "http",
        port: Optional[Union[int, str]] = 8083,
        verify: Optional[bool] = True,
        session=None,
        token: Optional[str] = None,
    ) -> None:
        super().__init__(
            host, username, password, base_url, protocol, port, verify, session, token
        )

    def add_secret(self, path: str, secret: dict) -> dict:
        """
        Add a new Hashicorp Vault secret.

        :param path: Name of secret path.
        :param secret: Secret definition {"path": path, "secret_data": {}}
        """
        body = SecretAddParameters(**secret)
        return self._make_request(
            "/secrets", method="post", params={"path": path}, jsonbody=body.model_dump()
        )

    def delete_secret(self, path: str) -> dict:
        """
        Delete a Hashicorp Vault secret.

        :param path: Name of secret path.
        """
        return self._make_request("/secrets", method="delete", params={"path": path})

    def get_secret(self, path: str) -> dict:
        """
        Get a list of Hashicorp Vault secrets.

        :param path: Name of secret path.
        """
        return self._make_request("/secrets", params={"path": path})

    def update_secret(self, path: str, config_object: dict) -> dict:
        """
        Updata a Hashicorpy Vault secret.

        :param path: Name of secret path.
        :param config_object: Secret data key/value pairs
        """
        return self._make_request(
            "/secrets", method="put", params={"path": path}, jsonbody=config_object
        )
