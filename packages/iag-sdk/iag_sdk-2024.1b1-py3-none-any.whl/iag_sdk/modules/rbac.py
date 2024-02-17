from typing import Optional, Union

from iag_sdk.client_base import ClientBase
from iag_sdk.models import (
    PathParam,
    PathParams,
    QueryParamsFilter,
    RbacAddGroupParameters,
    RbacAddGroupRolesParameters,
    RbacAddGroupUsersParameters,
    RbacUpdateGroupParameters,
)


class Rbac(ClientBase):
    """
    Class that contains methods for the IAG RBAC API routes.
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

    def add_group(
        self,
        group_name: str,
        roles: list[str],
        users: list[str] = None,
        description: str = None,
    ) -> dict:
        """
        Add a new RBAC group

        :param group_name: RBAC group name.
        :param roles: list of roles to assign to group.
        :param users: Optional. list of users to assign to group.
        :param description: Optional. Group description.
        """
        body = RbacAddGroupParameters(
            name=group_name, description=description, roles=roles, users=users
        )
        return self._make_request(
            "/rbac/groups", method="post", jsonbody=body.model_dump(exclude_none=True)
        )

    def add_group_roles(self, group_name: str, roles: list[str]) -> dict:
        """
        Add new roles to the RBAC group.

        :param group_name: RBAC group name.
        :param roles: list of roles to assign to group.
        """
        path_params = PathParam(name=group_name)
        body = RbacAddGroupRolesParameters(roles=roles)
        return self._make_request(
            "/rbac/groups/{name}/roles".format(**path_params.model_dump()),
            method="post",
            jsonbody=body.model_dump(),
        )

    def add_group_users(self, group_name: str, users: list[str]) -> dict:
        """
        Add new users to the RBAC group.

        :param group_name: RBAC group name.
        :param users: list of users to assign to group.
        """
        path_params = PathParam(name=group_name)
        body = RbacAddGroupUsersParameters(users=users)
        return self._make_request(
            "/rbac/groups/{name}/users".format(**path_params.model_dump()),
            method="post",
            jsonbody=body.model_dump(),
        )

    def delete_group(self, group_name: str) -> dict:
        """
        Delete an RBAC group.

        :param group_name: RBAC group name.
        """
        path_params = PathParam(name=group_name)
        return self._make_request(
            "/rbac/groups/{name}".format(**path_params.model_dump()), method="delete"
        )

    def delete_group_role(self, group_name: str, role_name: str) -> dict:
        """
        Delete a role from the RBAC group.

        :param group_name: RBAC group name.
        :param role_name: Name of role.
        """
        path_params = PathParams(name=group_name, module=role_name)
        return self._make_request(
            "/rbac/groups/{name}/roles/{module}".format(**path_params.model_dump()),
            method="delete",
        )

    def delete_group_user(self, group_name: str, username: str) -> dict:
        """
        Delete a user from the RBAC group.

        :param group_name: RBAC group name.
        :param username: Name of user.
        """
        path_params = PathParams(name=group_name, module=username)
        return self._make_request(
            "/rbac/groups/{name}/roles/{module}".format(**path_params.model_dump()),
            method="delete",
        )

    def get_group(self, group_name: str) -> dict:
        """
        Get information for an RBAC group.

        :param group_name: RBAC group name.
        """
        path_params = PathParam(name=group_name)
        return self._make_request(
            "/rbac/groups/{name}".format(**path_params.model_dump())
        )

    def get_group_roles(self, group_name: str) -> dict:
        """
        Get roles for an RBAC group.

        :param group_name: RBAC group name.
        """
        path_params = PathParam(name=group_name)
        return self._make_request(
            "/rbac/groups/{name}/roles".format(**path_params.model_dump())
        )

    def get_group_users(self, group_name: str) -> dict:
        """
        Get users for an RBAC group.

        :param group_name: RBAC group name.
        """
        path_params = PathParam(name=group_name)
        return self._make_request(
            "/rbac/groups/{name}/users".format(**path_params.model_dump())
        )

    def get_groups(
        self,
        offset: int = 0,
        limit: int = 50,
        filter: str = None,
        order: str = "ascending",
    ) -> dict:
        """
        Get a list of RBAC groups.

        :param offset: Optional. The number of items to skip before starting to collect the result set.
        :param limit: Optional. The number of items to return (default 50).
        :param filter: Optional. Response filter function with JSON name/value pair argument as string, i.e., 'contains({"name":"admin"})' Valid filter functions - contains, equals, startswith, endswith
        :param order: Optional. Sort indication. Available values : 'ascending' (default), 'descending'.
        """
        query_params = QueryParamsFilter(
            offset=offset, limit=limit, order=order, filter=filter
        )
        return self._make_request(
            "/rbac/groups",
            params=query_params.model_dump(exclude_none=True),
        )

    def get_role(self, role_name: str) -> dict:
        """
        Get information for an RBAC role.

        :param role_name: Name of RBAC role.
        """
        path_params = PathParam(name=role_name)
        return self._make_request(
            "/rbac/roles/{name}".format(**path_params.model_dump())
        )

    def get_roles(
        self,
        offset: int = 0,
        limit: int = 50,
        filter: str = None,
        order: str = "ascending",
    ) -> dict:
        """
        Get a list of RBAC roles.

        :param offset: Optional. The number of items to skip before starting to collect the result set.
        :param limit: Optional. The number of items to return (default 50).
        :param filter: Optional. Response filter function with JSON name/value pair argument as string, i.e., 'contains({"name":"admin"})' Valid filter functions - contains, equals, startswith, endswith
        :param order: Optional. Sort indication. Available values : 'ascending' (default), 'descending'.
        """
        query_params = QueryParamsFilter(
            offset=offset, limit=limit, order=order, filter=filter
        )
        return self._make_request(
            "/rbac/roles", params=query_params.model_dump(exclude_none=True)
        )

    def get_user_groups(
        self,
        username: str,
        offset: int = 0,
        limit: int = 50,
        filter: str = None,
        order: str = "ascending",
    ) -> dict:
        """
        Get RBAC group information for a user.

        :param username: Name of user.
        :param offset: Optional. The number of items to skip before starting to collect the result set.
        :param limit: Optional. The number of items to return (default 50).
        :param filter: Optional. Response filter function with JSON name/value pair argument as string, i.e., 'contains({"name":"admin"})' Valid filter functions - contains, equals, startswith, endswith
        :param order: Optional. Sort indication. Available values : 'ascending' (default), 'descending'.
        """
        query_params = QueryParamsFilter(
            offset=offset, limit=limit, order=order, filter=filter
        )
        return self._make_request(
            f"/rbac/users/{username}/groups",
            params=query_params.model_dump(exclude_none=True),
        )

    def get_user_roles(
        self,
        username: str,
        offset: int = 0,
        limit: int = 50,
        filter: str = None,
        order: str = "ascending",
    ) -> dict:
        """
        Get RBAC role information for a user.

        :param username: Name of user.
        :param offset: Optional. The number of items to skip before starting to collect the result set.
        :param limit: Optional. The number of items to return (default 50).
        :param filter: Optional. Response filter function with JSON name/value pair argument as string, i.e., 'contains({"name":"admin"})' Valid filter functions - contains, equals, startswith, endswith
        :param order: Optional. Sort indication. Available values : 'ascending' (default), 'descending'.
        """
        query_params = QueryParamsFilter(
            offset=offset, limit=limit, order=order, filter=filter
        )
        return self._make_request(
            f"/rbac/users/{username}/roles",
            params=query_params.model_dump(exclude_none=True),
        )

    def update_group(
        self,
        group_name: str,
        roles: list[str] = None,
        users: list[str] = None,
        description: str = None,
    ) -> dict:
        """
        Update an RBAC group

        :param group_name: RBAC group name.
        :param roles: Optional. list of roles to assign to group.
        :param users: Optional. list of users to assign to group.
        :param description: Optional. Group description.
        """
        path_params = PathParam(name=group_name)
        body = RbacUpdateGroupParameters(
            description=description, roles=roles, users=users
        )
        return self._make_request(
            "/rbac/groups/{name}".format(**path_params.model_dump()),
            method="put",
            jsonbody=body.model_dump(exclude_none=True),
        )
