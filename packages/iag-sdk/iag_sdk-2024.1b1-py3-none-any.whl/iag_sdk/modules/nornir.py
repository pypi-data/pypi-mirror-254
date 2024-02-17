from typing import Any, Optional, Union

from iag_sdk.client_base import ClientBase
from iag_sdk.models import (
    NornirModuleExecuteParameters,
    PathParam,
    QueryParams,
    QueryParamsDetail,
    Schema,
)


class Nornir(ClientBase):
    """
    Class that contains methods for the IAG Nornir API routes.
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

    def delete_module_schema(self, name: str) -> dict:
        """
        Remove a Nornir module schema.

        :param name: Name of the nornir module.
        """
        path_params = PathParam(name=name)
        return self._make_request(
            "/nornir/{name}/schema".format(**path_params.model_dump()), method="delete"
        )

    def execute_module(
        self,
        name: str,
        args: dict[str, Any],
        env: Optional[dict[str, Any]] = None,
        groups: Optional[list[str]] = None,
        hosts: Optional[list[str]] = None,
        strict_args: Optional[bool] = None,
    ) -> dict:
        """
        Execute a Nornir module.
        Tip: Use get_module_schema() to get the format of the parameters object.

        :param name: Name of nornir module to execute.
        :param args: Module Execution Parameters.
        :param env: Optional. list of environment variables.
        :param groups: Optional. list of Ansible device groups.
        :param hosts: Optional. list of Ansible hosts.
        :param strict_args: Optional. Override global strict args setting.
        """
        path_params = PathParam(name=name)
        body = NornirModuleExecuteParameters(
            args=args, env=env, groups=groups, hosts=hosts, strict_args=strict_args
        )
        return self._make_request(
            "/nornir/{name}/execute".format(**path_params.model_dump()),
            method="post",
            jsonbody=body.model_dump(exclude_none=True),
        )

    def get_module(self, name: str) -> dict:
        """
        Get Nornir module information

        :param name: Name of nornir module to retrieve.
        """
        path_params = PathParam(name=name)
        return self._make_request("/nornir/{name}".format(**path_params.model_dump()))

    def get_module_history(
        self, name: str, offset: int = 0, limit: int = 10, order: str = "descending"
    ) -> dict:
        """
        Get execution log events for a Nornir module.
        Tip: Use get_audit_log() and the audit_id returned by this call, to get the details of the execution.

        :param name: Name of the nornir module.
        :param offset: Optional. The number of items to skip before starting to collect the result set (default 0).
        :param limit: Optional. The number of items to return (default 10).
        :param order: Optional. Sort indication. Available values : ascending, descending (default).
        """
        path_params = PathParam(name=name)
        query_params = QueryParams(offset=offset, limit=limit, order=order)
        return self._make_request(
            "/nornir/{name}/history".format(**path_params.model_dump()),
            params=query_params.model_dump(),
        )

    def get_module_schema(self, name: str) -> dict:
        """
        Get the schema for a Nornir module.

        :param name: Name of nornir module.
        """
        path_params = PathParam(name=name)
        return self._make_request(
            "/nornir/{name}/schema".format(**path_params.model_dump())
        )

    def get_modules(
        self,
        offset: int = 0,
        limit: int = 50,
        filter: str = None,
        order: str = "ascending",
        detail: str = "summary",
    ) -> dict:
        """
        Get a list of Nornir modules.

        :param offset: The number of items to skip before starting to collect the result set.
        :param limit: The number of items to return (default 50).
        :param filter: Response filter function with JSON name/value pair argument as string, i.e., 'equals({"name":"sample"})' Valid filter functions - contains, equals, startswith, endswith
        :param order: Optional. Sort indication. Available values : ascending (default), descending.
        :param detail: Select detail level between 'full' (a lot of data) or 'summary' for each item.
        """
        query_params = QueryParamsDetail(
            offset=offset, limit=limit, filter=filter, order=order, detail=detail
        )
        return self._make_request(
            "/nornir", params=query_params.model_dump(exclude_none=True)
        )

    def refresh(self) -> dict:
        """
        Perform Nornir module discovery and update internal cache.
        """
        return self._make_request("/nornir/refresh", method="post")

    def update_module_schema(self, name: str, schema_object: dict) -> dict:
        """
        Update/Insert a Nornir module schema document.
        Tip: Use get_module_schema() to get an idea of the format of the config_object.

        :param name: Name of nornir module.
        :param schema_object: Schema to apply to nornir module identified in path.
        """
        path_params = PathParam(name=name)
        body = Schema(**schema_object)
        return self._make_request(
            "/nornir/{name}/schema".format(**path_params.model_dump()),
            method="put",
            jsonbody=body.model_dump(exclude_none=True),
        )
