from typing import Any, Optional, Union

from iag_sdk.client_base import ClientBase
from iag_sdk.models import (
    GroupAddParameters,
    GroupChildren,
    GroupDevices,
    GroupUpdateParameters,
    PathParam,
    PathParams,
    QueryParamsFilter,
)


class Group(ClientBase):
    """
    Class that contains methods for the IAG Groups API routes.
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
        devices: list[str],
        child_groups: list[str] = None,
        variables: dict = None,
    ) -> dict:
        """
        Add a new Ansible device group.

        :param group_name: Name of device group.
        :param devices: List of devices that are part of this group.
        :param childGroups: Optional. Children of this device group.
        :param variables: Optional. Group variables.
        """
        body = GroupAddParameters(
            name=group_name,
            devices=devices,
            childGroups=child_groups,
            variables=variables,
        )
        return self._make_request(
            "/groups", method="post", jsonbody=body.model_dump(exclude_none=True)
        )

    def add_group_children(self, group_name: str, child_group_list: list[str]) -> dict:
        """
        Add new child groups to an Ansible device group.

        :param group_name: Name of group.
        :param child_group_list: Child Group List.
        """
        path_params = PathParam(name=group_name)
        body = GroupChildren(child_group_list)
        return self._make_request(
            "/groups/{name}/children".format(**path_params.model_dump()),
            method="post",
            jsonbody=body.model_dump(),
        )

    def add_group_devices(self, group_name: str, device_list: list[str]) -> dict:
        """
        Add new devices to an Ansible device group.

        :param group_name: Name of group.
        :param device_list: Device List.
        """
        path_params = PathParam(name=group_name)
        body = GroupDevices(device_list)
        return self._make_request(
            "/groups/{name}/devices".format(**path_params.model_dump()),
            method="post",
            jsonbody=body.model_dump(),
        )

    def delete_group(self, group_name: str) -> dict:
        """
        Delete an Ansible device group.

        :param group_name: Name of group.
        """
        path_params = PathParam(name=group_name)
        return self._make_request(
            "/groups/{name}".format(**path_params.model_dump()), method="delete"
        )

    def delete_group_child(self, group_name: str, child_group: str) -> dict:
        """
        Delete a child group from an Ansible device group.

        :param group_name: Name of group.
        :param child_group: Name of child group to delete.
        """
        path_params = PathParams(name=group_name, module=child_group)
        return self._make_request(
            "/groups/{name}/children/{module}".format(**path_params.model_dump()),
            method="delete",
        )

    def delete_group_device(self, group_name: str, device_name: str) -> dict:
        """
        Delete a device from an Ansible device group.

        :param group_name: Name of group.
        :param device_name: Name of device.
        """
        path_params = PathParams(name=group_name, module=device_name)
        return self._make_request(
            "/groups/{name}/devices/{module}".format(**path_params.model_dump()),
            method="delete",
        )

    def get_group(self, group_name: str) -> dict:
        """
        Get information for an Ansible device group.

        :param group_name: Name of group.
        """
        path_params = PathParam(name=group_name)
        return self._make_request("/groups/{name}".format(**path_params.model_dump()))

    def get_group_children(self, group_name: str) -> dict:
        """
        Get a list of child groups for an Ansible device group.

        :param group_name: Name of group.
        """
        path_params = PathParam(name=group_name)
        return self._make_request(
            "/groups/{name}/children".format(**path_params.model_dump())
        )

    def get_group_devices(self, group_name: str) -> dict:
        """
        Get the devices for an Ansible device group.

        :param group_name: Name of group.
        """
        path_params = PathParam(name=group_name)
        return self._make_request(
            "/groups/{name}/devices".format(**path_params.model_dump())
        )

    def get_group_variable(self, group_name: str, variable_name) -> dict:
        """
        Get the contents of a variable for an Ansible device group.

        :param group_name: Name of group.
        :param variable_name: Name of variable.
        """
        path_params = PathParams(name=group_name, module=variable_name)
        return self._make_request(
            "/groups/{name}/variables/{module}".format(**path_params.model_dump())
        )

    def get_group_variables(self, group_name: str) -> dict:
        """
        Get the variables for an Ansible device group.

        :param group_name: Name of group.
        """
        path_params = PathParam(name=group_name)
        return self._make_request(
            "/groups/{name}/variables".format(**path_params.model_dump())
        )

    def get_groups(
        self,
        offset: int = 0,
        limit: int = 50,
        filter: str = None,
        order: str = "ascending",
    ) -> dict:
        """
        Get a list of Ansible device groups.

        :param offset: Optional. The number of items to skip before starting to collect the result set.
        :param limit: Optional. The number of items to return (default 50).
        :param filter: Optional. Response filter function with JSON name/value pair argument as string, i.e., 'equals({"name":"asa"})' Valid filter functions - contains, equals, startswith, endswith
        :param order: Optional. Sort indication. Available values : 'ascending' (default), 'descending'.
        """
        query_params = QueryParamsFilter(
            offset=offset, limit=limit, filter=filter, order=order
        )
        return self._make_request(
            "/groups",
            params=query_params.model_dump(exclude_none=True),
        )

    def update_group(self, group_name: str, variables: dict[str, Any]) -> dict:
        """
        Update the variables in an Ansbile device group.

        :param group_name: Name of group
        :param variables: Group variables.
        """
        path_params = PathParam(name=group_name)
        body = GroupUpdateParameters(variables=variables)
        return self._make_request(
            "/groups/{name}".format(**path_params.model_dump()),
            method="put",
            jsonbody=body.variables,
        )
