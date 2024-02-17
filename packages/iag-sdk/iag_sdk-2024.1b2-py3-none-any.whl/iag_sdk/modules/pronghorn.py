from typing import Optional, Union

from iag_sdk.client_base import ClientBase


class Pronghorn(ClientBase):
    """
    Class that contains methods for the IAG Pronghorn API routes.
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

    def get_pronghorn(self) -> dict:
        """
        Get pronghorn.json for the IAG server.
        """
        return self._make_request("/pronghorn")
