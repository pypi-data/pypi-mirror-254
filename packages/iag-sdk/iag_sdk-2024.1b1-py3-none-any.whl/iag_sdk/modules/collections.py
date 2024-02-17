from typing import Any, Optional, Union

from iag_sdk.client_base import ClientBase
from iag_sdk.models import (
    CollectionInstallParameters,
    ModuleExecuteParameters,
    PathParam,
    PathParams,
    QueryParams,
    QueryParamsDetail,
    RoleExecuteParameters,
    Schema,
)


class Collection(ClientBase):
    """
    Class that contains methods for the IAG Collections API routes.
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

    def add_collection(self, config_object: dict) -> dict:
        """
        Install an Ansible collection from a Galaxy server or from a tarball.

        :param config_object: Parameters for collection name and Galaxy server authentication.
        """
        # TODO: replace config_object with arguments
        body = CollectionInstallParameters(**config_object)
        return self._make_request(
            "/collections/install",
            method="post",
            jsonbody=body.model_dump(exclude_none=True),
        )

    def delete_module_schema(self, collection_name: str, module_name: str) -> dict:
        """
        Remove a schema for a module in the Ansible collection.

        :param collection_name: Name of collection.
        :param module_name: Name of module.
        """
        path_params = PathParams(name=collection_name, module=module_name)
        return self._make_request(
            "/collections/{name}/modules/{module}/schema".format(
                **path_params.model_dump()
            ),
            method="delete",
        )

    def delete_role_schema(self, collection_name: str, role_name: str) -> dict:
        """
        Remove a schema for a role in the Ansible collection.

        :param collection_name: Name of collection.
        :param role_name: Name of role.
        """
        path_params = PathParams(name=collection_name, module=role_name)
        return self._make_request(
            "/collections/{name}/roles/{module}/schema".format(
                **path_params.model_dump()
            ),
            method="delete",
        )

    def get_collection(self, collection_name: str) -> dict:
        """
        Get details for an Ansible collection.

        :param collection_name: Name of collection to retrieve detail for.
        """
        path_params = PathParam(name=collection_name)
        return self._make_request(
            "/collections/{name}".format(**path_params.model_dump())
        )

    def get_module(self, collection_name: str, module_name: str) -> dict:
        """
        Get details for an Ansible collection.

        :param collection_name: Name of collection to retrieve detail for.
        :param module_name: Name of module to retrieve detail for.
        """
        path_params = PathParams(name=collection_name, module=module_name)
        return self._make_request(
            "/collections/{name}/modules/{module}".format(**path_params.model_dump())
        )

    def get_module_history(
        self,
        collection_name: str,
        module_name: str,
        offset: int = 0,
        limit: int = 10,
        order: str = "descending",
    ) -> dict:
        """
        Get execution log events for an Ansible collection module.
        Tip: Use get_audit_log() and the audit_id returned by this call, to get the details of the execution.

        :param collection_name: Name of collection.
        :param module_name: Name of module within collection.
        :param offset: Optional. The number of items to skip before starting to collect the result set.
        :param limit: Optional. The number of items to return.
        :param order: Optional. Sort indication. Available values : 'ascending', 'descending' (default).
        """
        path_params = PathParams(name=collection_name, module=module_name)
        query_params = QueryParams(offset=offset, limit=limit, order=order)
        return self._make_request(
            "/collections/{name}/modules/{module}/history".format(
                **path_params.model_dump()
            ),
            params=query_params.model_dump(),
        )

    def get_module_schema(self, collection_name: str, module_name: str) -> dict:
        """
        Get the schema for a module in the Ansible collection.

        :param collection_name: Name of collection.
        :param module_name: Name of module.
        """
        path_params = PathParams(name=collection_name, module=module_name)
        return self._make_request(
            "/collections/{name}/modules/{module}/schema".format(
                **path_params.model_dump()
            )
        )

    def get_modules(
        self,
        collection_name: str,
        offset: int = 0,
        limit: int = 50,
        filter: str = None,
        order: str = "ascending",
        detail: str = "summary",
    ) -> dict:
        """
        Get module list for an Ansible collection.

        :param collection_name: Name of collection to retrieve detail for.
        :param offset: Optional. The number of items to skip before starting to collect the result set.
        :param limit: Optional. The number of items to return (default 50).
        :param filter: Optional. Response filter function with JSON name/value pair argument as string, i.e., 'equals({"name":"cisco.asa"})' Valid filter functions - contains, equals, startswith, endswith
        :param order: Optional. Sort indication. Available values : 'ascending' (default), 'descending'.
        :param detail: Optional. Select detail level between 'full' (a lot of data) or 'summary' (default) for each item.
        """
        path_params = PathParam(name=collection_name)
        query_params = QueryParamsDetail(
            offset=offset, limit=limit, filter=filter, order=order, detail=detail
        )
        return self._make_request(
            "/collections/{name}/modules".format(**path_params.model_dump()),
            params=query_params.model_dump(exclude_none=True),
        )

    def get_role(self, collection_name: str, role_name: str) -> dict:
        """
        Get details for a role in the Ansible collection.

        :param collection_name: Name of collection to retrieve detail for.
        :param role_name: Name of role to retrieve detail for.
        """
        path_params = PathParams(name=collection_name, module=role_name)
        return self._make_request(
            "/collections/{name}/roles/{module}".format(**path_params.model_dump())
        )

    def get_role_history(
        self,
        collection_name: str,
        role_name: str,
        offset: int = 0,
        limit: int = 10,
        order: str = "descending",
    ) -> dict:
        """
        Get execution log events for an Ansible collection role.
        Tip: Use get_audit_log() and the audit_id returned by this call, to get the details of the execution.

        :param collection_name: Name of collection.
        :param role_name: Name of role within collection.
        :param offset: Optional. The number of items to skip before starting to collect the result set.
        :param limit: Optional. The number of items to return.
        :param order: Optional. Sort indication. Available values : 'ascending', 'descending' (default).
        """
        path_params = PathParams(name=collection_name, module=role_name)
        query_params = QueryParams(offset=offset, limit=limit, order=order)
        return self._make_request(
            "/collections/{name}/roles/{module}/history".format(
                **path_params.model_dump()
            ),
            params=query_params.model_dump(),
        )

    def get_role_schema(self, collection_name: str, role_name: str) -> dict:
        """
        Get the schema for a role in the Ansible collection.

        :param collection_name: Name of collection.
        :param role_name: Name of role.
        """
        path_params = PathParams(name=collection_name, module=role_name)
        return self._make_request(
            "/collections/{name}/roles/{module}/schema".format(
                **path_params.model_dump()
            )
        )

    def get_roles(
        self,
        collection_name: str,
        offset: int = 0,
        limit: int = 50,
        filter: str = None,
        order: str = "ascending",
        detail: str = "summary",
    ) -> dict:
        """
        Get role list for an Ansible collection.

        :param collection_name: Name of collection to retrieve detail for.
        :param offset: Optional. The number of items to skip before starting to collect the result set.
        :param limit: Optional. The number of items to return (default 50).
        :param filter: Optional. Response filter function with JSON name/value pair argument as string, i.e., 'equals({"name":"cisco.asa"})' Valid filter functions - contains, equals, startswith, endswith
        :param order: Optional. Sort indication. Available values : 'ascending' (default), 'descending'.
        :param detail: Optional. Select detail level between 'full' (a lot of data) or 'summary' (default) for each item.
        """
        path_params = PathParam(name=collection_name)
        query_params = QueryParamsDetail(
            offset=offset, limit=limit, filter=filter, order=order, detail=detail
        )
        return self._make_request(
            "/collections/{name}/roles".format(**path_params.model_dump()),
            params=query_params.model_dump(exclude_none=True),
        )

    def get_collections(
        self,
        offset: int = 0,
        limit: int = 50,
        filter: str = None,
        order: str = "ascending",
        detail: str = "summary",
    ) -> dict:
        """
        Get list of installed Ansible collections.

        :param offset: Optional. The number of items to skip before starting to collect the result set.
        :param limit: Optional. The number of items to return (default 50).
        :param filter: Optional. Response filter function with JSON name/value pair argument as string, i.e., 'equals({"name":"cisco.asa"})' Valid filter functions - contains, equals, startswith, endswith
        :param order: Optional. Sort indication. Available values : 'ascending' (default), 'descending'.
        :param detail: Optional. Select detail level between 'full' (a lot! of data) or 'summary' (default) for each item.
        """
        query_params = QueryParamsDetail(
            offset=offset, limit=limit, filter=filter, order=order, detail=detail
        )
        return self._make_request(
            "/collections", params=query_params.model_dump(exclude_none=True)
        )

    def refresh(self) -> dict:
        """
        Perform Ansible collection discovery and update internal cache.
        """
        return self._make_request("/collections/refresh", method="post")

    def execute_module(
        self,
        collection_name: str,
        module_name: str,
        args: dict[str, Any],
        groups: Optional[list[str]] = None,
        hosts: Optional[list[str]] = None,
        provider_required: Optional[bool] = None,
        strict_args: Optional[bool] = None,
        template: Optional[str] = None,
    ) -> dict:
        """
        Execute a module contained within the Ansible collection.

        :param collection_name: Name of collection.
        :param module_name: Name of module within collection.
        :param args: Module Execution Parameters.
        :param groups: Optional. Ansible device groups.
        :param hosts: Optional. Ansible hosts.
        :param provider_required: Optional. Enable/disable automation of provider object.
        :param strict_args: Optional. Override global strict args setting.
        :param template: Optional. TextFSM template.
        """
        path_params = PathParams(name=collection_name, module=module_name)
        body = ModuleExecuteParameters(
            args=args,
            groups=groups,
            hosts=hosts,
            provider_required=provider_required,
            strict_args=strict_args,
            template=template,
        )
        return self._make_request(
            "/collections/{name}/modules/{module}/execute".format(
                **path_params.model_dump()
            ),
            method="post",
            jsonbody=body.model_dump(exclude_none=True),
        )

    def execute_role(
        self,
        collection_name: str,
        role_name: str,
        args: dict[str, Any],
        groups: Optional[list[str]] = None,
        hosts: Optional[list[str]] = None,
        strict_args: Optional[bool] = None,
        template: Optional[str] = None,
    ) -> dict:
        """
        Execute a module contained within the Ansible collection.

        :param collection_name: Name of collection.
        :param role_name: Name of role within collection.
        :param args: Module Execution Parameters.
        :param groups: Optional. Ansible device groups.
        :param hosts: Optional. Ansible hosts.
        :param strict_args: Optional. Override global strict args setting.
        :param template: Optional. TextFSM template.
        """
        path_params = PathParams(name=collection_name, module=role_name)
        body = RoleExecuteParameters(
            args=args,
            groups=groups,
            hosts=hosts,
            strict_args=strict_args,
            template=template,
        )
        return self._make_request(
            "/collections/{name}/roles/{module}/execute".format(
                **path_params.model_dump()
            ),
            method="post",
            jsonbody=body.model_dump(exclude_none=True),
        )

    def update_module_schema(
        self, collection_name: str, module_name: str, schema_object: dict
    ) -> dict:
        """
        Update/Insert a schema document for module in the Ansible collection.
        Tip: Use get_collection_module_schema() to get an idea of the format of the schema_object.

        :param collection_name: Name of collection.
        :param module_name: Name of module.
        :param schema_object: Schema to apply to module identified in path.
        """
        path_params = PathParams(name=collection_name, module=module_name)
        body = Schema(**schema_object)
        return self._make_request(
            "/collections/{name}/modules/{module}/schema".format(
                **path_params.model_dump()
            ),
            method="put",
            jsonbody=body.model_dump(exclude_none=True),
        )

    def update_role_schema(
        self, collection_name: str, role_name: str, schema_object: dict
    ) -> dict:
        """
        Update/Insert a schema document for role in the Ansible collection.
        Tip: Use get_collection_role_schema() to get an idea of the format of the config_object.

        :param collection_name: Name of collection.
        :param role_name: Name of role.
        :param schema_object: Schema to apply to role identified in path.
        """
        path_params = PathParams(name=collection_name, module=role_name)
        body = Schema(**schema_object)
        return self._make_request(
            "/collections/{name}/roles/{module}/schema".format(
                **path_params.model_dump()
            ),
            method="put",
            jsonbody=body.model_dump(exclude_none=True),
        )
