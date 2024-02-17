from typing import Any, Optional, Union

from iag_sdk.client_base import ClientBase


class Ldap(ClientBase):
    """
    Class that contains methods for the IAG LDAP API routes.
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

    def test_bind(self) -> Any:
        """
        test LDAP connection
        """
        return self._make_request("/ldap/test_bind", method="post")
