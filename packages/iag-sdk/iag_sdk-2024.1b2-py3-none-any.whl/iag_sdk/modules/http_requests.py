from typing import Optional, Union

from iag_sdk.client_base import ClientBase
from iag_sdk.models import HttpRequestsExecuteParameters, QueryParams


class HttpRequest(ClientBase):
    """
    Class that contains methods for the IAG HTTP Requests API routes.
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

    def execute_request(self, parameters: dict) -> dict:
        """
        Send an HTTP/1.1 request to an inventory device.

        :param parameters: Parameters required to send your request. See the Requests library for all other supported parameters: https://docs.python-requests.org/en/latest/api/
        """
        # TODO: replace parameters with arguments
        body = HttpRequestsExecuteParameters(**parameters)
        return self._make_request(
            "/http_requests/request/execute",
            method="post",
            jsonbody=body.model_dump(exclude_none=True),
        )

    def get_request_history(
        self, offset: int = 0, limit: int = 10, order: str = "descending"
    ) -> dict:
        """
        Get execution log events for an HTTP request.

        :param offset: Optional. The number of items to skip before starting to collect the result set.
        :param limit: Optional. The number of items to return (default 10).
        :param order: Optional. Sort indication. Available values : 'ascending', 'descending' (default).
        """
        query_params = QueryParams(offset=offset, limit=limit, order=order)
        return self._make_request(
            "/http_requests/request/history",
            params=query_params.model_dump(),
        )

    def get_request_schema(self) -> dict:
        """
        Get the json schema for http_requests' request endpoint.
        """
        return self._make_request("/http_requests/request/schema")
