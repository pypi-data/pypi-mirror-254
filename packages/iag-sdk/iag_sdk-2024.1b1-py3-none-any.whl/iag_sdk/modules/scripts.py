from typing import Any, Optional, Union

from iag_sdk.client_base import ClientBase
from iag_sdk.models import (
    PathParam,
    QueryParams,
    QueryParamsDetail,
    Schema,
    ScriptExecuteParameters,
)


class Script(ClientBase):
    """
    Class that contains methods for the IAG Scripts API routes.
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

    def delete_script_schema(self, name: str) -> dict:
        """
        Remove a script schema.

        :param name: Name of script.
        """
        path_params = PathParam(name=name)
        return self._make_request(
            "/scripts/{name}/schema".format(**path_params.model_dump()), method="delete"
        )

    def execute_script(
        self,
        name: str,
        args: dict[str, Any],
        env: Optional[dict[str, Any]] = None,
        hosts: Optional[list[str]] = None,
        strict_args: Optional[bool] = None,
        template: Optional[str] = None,
    ) -> dict:
        """
        Execute a script.
        Tip: Use get_script_schema() to get the format of the parameters object.

        :param name: Name of script to be executed.
        :param args: Module Execution Parameters.
        :param env: Optional. Environment variables.
        :param hosts: Optional. list of Ansible hosts.
        :param strict_args: Optional. Override global strict args setting.
        :param template: Optional. TextFSM template.
        """
        path_params = PathParam(name=name)
        body = ScriptExecuteParameters(
            args=args, env=env, hosts=hosts, strict_args=strict_args, template=template
        )
        return self._make_request(
            "/scripts/{name}/execute".format(**path_params.model_dump()),
            method="post",
            jsonbody=body.model_dump(exclude_none=True),
        )

    def get_script(self, name: str) -> dict:
        """
        Get script information.

        :param name: Name of script to retrieve.
        """
        path_params = PathParam(name=name)
        return self._make_request("/scripts/{name}".format(**path_params.model_dump()))

    def get_script_history(
        self, name: str, offset: int = 0, limit: int = 10, order: str = "descending"
    ) -> dict:
        """
        Get execution log events for a script.
        Tip: Use get_audit_log() and the audit_id returned by this call, to get the details of the execution.

        :param name: Name of script to retrieve.
        :param offset: Optional. The number of items to skip before starting to collect the result set.
        :param limit: Optional. The number of items to return.
        :param order: Optional. Sort indication. Available values : ascending, descending (default).
        """
        path_params = PathParam(name=name)
        query_params = QueryParams(offset=offset, limit=limit, order=order)
        return self._make_request(
            "/scripts/{name}/history".format(**path_params.model_dump()),
            params=query_params.model_dump(),
        )

    def get_script_schema(self, name: str) -> dict:
        """
        Get the schema for a script.

        :param name: Name of script to retrieve.
        """
        path_params = PathParam(name=name)
        return self._make_request(
            "/scripts/{name}/schema".format(**path_params.model_dump())
        )

    def get_scripts(
        self,
        offset: int = 0,
        limit: int = 50,
        filter: str = None,
        order: str = "ascending",
        detail: str = "summary",
    ) -> dict:
        """
        Get a list of scripts.

        :param offset: Optional. The number of items to skip before starting to collect the result set.
        :param limit: Optional. The number of items to return (default 50).
        :param filter: Optional. Response filter function with JSON name/value pair argument as string, i.e., 'equals({"name":"sample"})' Valid filter functions - contains, equals, startswith, endswith
        :param order: Optional. Sort indication. Available values : ascending (default), descending.
        :param detail: Optional. Select detail level between 'full' (a lot of data) or 'summary' for each item.
        """
        query_params = QueryParamsDetail(
            offset=offset, limit=limit, filter=filter, order=order, detail=detail
        )
        return self._make_request(
            "/scripts", params=query_params.model_dump(exclude_none=True)
        )

    def refresh(self) -> dict:
        """
        Perform script discovery and update internal cache.
        """
        return self._make_request("/scripts/refresh", method="post")

    def update_script_schema(self, name: str, schema_object: dict) -> dict:
        """
        Update/Insert a script schema document.
        Tip: Use get_script_schema() to get an idea of the format of the config_object.

        :param name: Name of script.
        :param schema_object: Schema to apply to module identified in path.
        """
        path_params = PathParam(name=name)
        body = Schema(**schema_object)
        return self._make_request(
            "/scripts/{name}/schema".format(**path_params.model_dump()),
            method="put",
            jsonbody=body.model_dump(exclude_none=True),
        )
