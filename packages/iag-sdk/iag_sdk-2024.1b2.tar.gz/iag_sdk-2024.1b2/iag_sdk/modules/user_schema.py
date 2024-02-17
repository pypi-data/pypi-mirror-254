from typing import Optional, Union

from iag_sdk.client_base import ClientBase
from iag_sdk.models import PathParams


class UserSchema(ClientBase):
    """
    Class that contains methods for the IAG User Schema API routes.
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

    def delete_schema(self, schema_type: str, schema_name: str) -> dict:
        """
        Remove a user schema.

        :param schema_type: Type of schema.
        :param schema_name: Name of schema.
        """
        path_params = PathParams(name=schema_type, module=schema_name)
        return self._make_request(
            "/user-schema/{schema_type}/{schema_name}".format(
                **path_params.model_dump()
            ),
            method="delete",
        )

    def update_schema(
        self, schema_type: str, schema_name: str, schema_object: dict
    ) -> dict:
        """
        Update/Insert a user schema document.

        :param schema_type: Type of schema.
        :param schema_name: Name of schema.
        :param schema_object: Schema to apply to entity in identified in path.
        """
        path_params = PathParams(name=schema_type, module=schema_name)
        return self._make_request(
            "/user-schema/{schema_type}/{schema_name}".format(
                **path_params.model_dump()
            ),
            method="put",
            jsonbody=schema_object,
        )
