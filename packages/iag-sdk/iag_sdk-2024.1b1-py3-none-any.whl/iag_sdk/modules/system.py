from typing import Optional, Union

from iag_sdk.client_base import ClientBase
from iag_sdk.models import PathParam, QueryParams


class System(ClientBase):
    """
    Class that contains methods for the IAG System API routes.
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

    def get_audit_log(self, audit_id: str) -> dict:
        """
        Get execution history payload.

        :param audit_id: Audit id of execution.
        """
        path_params = PathParam(name=audit_id)
        return self._make_request(
            "/exec_history/{name}".format(**path_params.model_dump())
        )

    def get_audit_logs(
        self, offset: int = 0, limit: int = 50, order: str = "descending"
    ) -> dict:
        """
        Retrieve execution audit logs persisted in the database.

        :param offset: Optional. The number of items to skip before starting to collect the result set.
        :param limit: Optional. The number of items to return (default 50).
        :param order: Optional. Sort indication. Available values : 'ascending', 'descending' (default).
        """
        query_params = QueryParams(offset=offset, limit=limit, order=order)
        return self._make_request("/audit", params=query_params.model_dump())

    def get_health(self) -> dict:
        """
        Determine if AG server is up and running.
        """
        return self._make_request("/poll")

    def get_openapi_spec(self) -> dict:
        """
        Get the current OpenAPI spec from the running instance of IAG
        """
        return self._make_request("/openapi_spec")

    def get_status(self) -> dict:
        """
        Get the AG server status (version, ansible version, etc).
        """
        return self._make_request("/status")
