from typing import Any, Optional, Union

from iag_sdk.client_base import ClientBase
from iag_sdk.models import (
    PathParam,
    PlaybookExecuteParameters,
    QueryParams,
    QueryParamsDetail,
    Schema,
)


class Playbook(ClientBase):
    """
    Class that contains methods for the IAG Playbooks API routes.
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

    def delete_playbook_schema(self, name: str) -> dict:
        """
        Remove an Ansible playbook schema.

        :param name: Name of playbook.
        """
        path_params = PathParam(name=name)
        return self._make_request(
            "/playbooks/{name}/schema".format(**path_params.model_dump()),
            method="delete",
        )

    def execute_playbook(
        self,
        name: str,
        args: dict[str, Any],
        groups: Optional[list[str]] = None,
        hosts: Optional[list[str]] = None,
        strict_args: Optional[bool] = None,
        syntax_check: Optional[bool] = None,
        template: Optional[str] = None,
        verbosity: Optional[int] = None,
        dry_run: bool = False,
    ) -> dict:
        """
        Execute an Ansible playbook.
        Tip: Use get_playbook_schema() to get the format of the parameters object.

        :param name: Name of playbook to be executed.
        :param args: Playbook Execution Parameters.
        :param groups: Optional. list of Ansible device groups.
        :param hosts: Optional. list of Ansible hosts.
        :param strict_args: Optional. Override global strict args setting
        :param syntax_check: Optional. Perform a syntax check on the playbook, but do not execute it
        :param template: Optional. TextFSM template.
        :param verbosity: Optional. Control how verbose the output of ansible-playbook is. Min=1, Max=4.
        :param dry_run: Optional. Set to True to run playbook in check mode (dry run).
        """
        path_params = PathParam(name=name)
        body = PlaybookExecuteParameters(
            args=args,
            groups=groups,
            hosts=hosts,
            strict_args=strict_args,
            syntax_check=syntax_check,
            template=template,
            verbosity=verbosity,
        )
        if dry_run:
            return self._make_request(
                "/playbooks/{name}/dry_run".format(**path_params.model_dump()),
                method="post",
                jsonbody=body.model_dump(exclude_none=True),
            )
        else:
            return self._make_request(
                "/playbooks/{name}/execute".format(**path_params.model_dump()),
                method="post",
                jsonbody=body.model_dump(exclude_none=True),
            )

    def get_playbook(self, name: str) -> dict:
        """
        Get information for an Ansible playbook.

        :param name: Name of playbook to retrieve.
        """
        path_params = PathParam(name=name)
        return self._make_request(
            "/playbooks/{name}".format(**path_params.model_dump())
        )

    def get_playook_history(
        self, name: str, offset: int = 0, limit: int = 10, order: str = "descending"
    ) -> dict:
        """
        Get execution log events for an Ansible playbook.
        Tip: Use get_audit_log() and the audit_id returned by this call, to get the details of the execution.

        :param name: Name of playbook to retrieve.
        :param offset: Optional. The number of items to skip before starting to collect the result set (default 0).
        :param limit: Optional. The number of items to return (default 10).
        :param order: Optional. Sort indication. Available values : ascending, descending (default).
        """
        path_params = PathParam(name=name)
        query_params = QueryParams(offset=offset, limit=limit, order=order)
        return self._make_request(
            "/playbooks/{name}/history".format(**path_params.model_dump()),
            params=query_params.model_dump(),
        )

    def get_playbook_schema(self, name: str) -> dict:
        """
        Get the schema for an Ansible playbook.

        :param name: Name of playbook to retrieve.
        """
        path_params = PathParam(name=name)
        return self._make_request(
            "/playbooks/{name}/schema".format(**path_params.model_dump())
        )

    def get_playbooks(
        self,
        offset: int = 0,
        limit: int = 50,
        filter: str = None,
        order: str = "ascending",
        detail: str = "summary",
    ) -> dict:
        """
        Get a list of Ansible playbooks.

        :param offset: Optional. The number of items to skip before starting to collect the result set (default 0).
        :param limit: Optional. The number of items to return (default 50).
        :param filter: Optional. Response filter function with JSON name/value pair argument as string, i.e., 'equals({"name":"sample"})' Valid filter functions - contains, equals, startswith, endswith
        :param order: Optional. Sort indication. Available values : ascending (default), descending.
        :param detail: Optional. Select detail level between 'full' (a lot of data) or 'summary' for each item.
        """
        query_params = QueryParamsDetail(
            offset=offset, limit=limit, filter=filter, order=order, detail=detail
        )
        return self._make_request(
            "/playbooks", params=query_params.model_dump(exclude_none=True)
        )

    def refresh(self) -> dict:
        """
        Perform Ansible playbook discovery and update internal cache.
        """
        return self._make_request("/playbooks/refresh", method="post")

    def update_playbook_schema(self, name: str, schema_object: dict) -> dict:
        """
        Update/Insert an Ansible playbook schema document.
        Tip: Use get_playbook_schema() to get an idea of the format of the config_object.

        :param name: Name of playbook.
        :param schema_object: Schema to apply to playbook identified in path.
        """
        path_params = PathParam(name=name)
        body = Schema(**schema_object)
        return self._make_request(
            "/playbooks/{name}/schema".format(**path_params.model_dump()),
            method="put",
            jsonbody=body.model_dump(exclude_none=True),
        )
