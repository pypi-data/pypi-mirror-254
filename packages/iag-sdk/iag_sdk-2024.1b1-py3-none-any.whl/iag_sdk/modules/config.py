from typing import Optional, Union

from iag_sdk.client_base import ClientBase
from iag_sdk.models import ConfigParameters


class Config(ClientBase):
    """
    Class that contains methods for the IAG Config API routes.
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

    def get_config(self) -> dict:
        """
        Fetch config value from IAG server database.
        """
        return self._make_request("/config")

    def update_config(self, config_object: dict) -> dict:
        """
        Update config to AG server database.
        Tip: Use get_config() to get the format of the config_object.
        Note: Not all of the settings can be udpated through the API. Check the ConfigParameters class in iag_sdk.models for available fields.

        :param config_object: Updated config object.
        """
        # TODO: replace config_object with arguments
        body = ConfigParameters(**config_object)
        return self._make_request(
            "/config", method="put", jsonbody=body.model_dump(exclude_none=True)
        )
