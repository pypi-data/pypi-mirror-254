from typing import Any, Optional, Union

from iag_sdk.client_base import ClientBase
from iag_sdk.models import (
    InventoryHttpAddParameters,
    InventoryHttpUpdateParameters,
    InventoryNetconfAddParameters,
    InventoryNetconfUpdateParameters,
    InventoryNetmikoAddVariables,
    InventoryNetmikoUpdateParameters,
    PathParams,
    QueryParamsFilter,
)


class Inventory(ClientBase):
    """
    Class that contains methods for the IAG Inventory API routes.
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

    def add_http_requests_device(
        self, name: str, variables: dict[str, Any], inventory_name: str = "default"
    ) -> dict:
        """
        Create a device in the http_requests inventory.

        :param name: Name of the device.
        :param variables: dictionary containing the device definition.
        :param inventory_name: Optional. Name of inventory (default = "default").
        """
        body = InventoryHttpAddParameters(name=name, variables=variables)
        return self._make_request(
            f"/inventories/http_requests/{inventory_name}/devices",
            method="post",
            jsonbody=body.model_dump(exclude_none=True),
        )

    def add_netconf_device(
        self, name: str, variables: dict[str, Any], inventory_name: str = "default"
    ) -> dict:
        """
        Create a device in the netconf inventory.

        :param name: Name of the device.
        :param variables: dictionary containing the device definition.
        :param inventory_name: Optional. Name of inventory (default = "default").
        """
        body = InventoryNetconfAddParameters(name=name, variables=variables)
        return self._make_request(
            f"/inventories/netconf/{inventory_name}/devices",
            method="post",
            jsonbody=body.model_dump(exclude_none=True),
        )

    def add_netmiko_device(
        self, variables: dict, inventory_name: str = "default"
    ) -> dict:
        """
        Create a device in the default netmiko inventory.
        Use get_netmiko_device() to get an idea of the format of the variables dict.

        :param variables: dictionary containing the device definition
        :param inventory_name: Optional. Name of inventory (default = "default").
        """
        body = InventoryNetmikoAddVariables(**variables)
        return self._make_request(
            f"/inventories/netmiko/{inventory_name}/devices",
            method="post",
            jsonbody=body.model_dump(exclude_none=True),
        )

    def delete_http_requests_device(
        self, name: str, inventory_name: str = "default"
    ) -> dict:
        """
        Delete a device from the HTTP requests inventory.

        :param name: Name of the HTTP requests device.
        :param inventory_name: Optional. Name of inventory (default = "default").
        """
        path_params = PathParams(name=name, module=inventory_name)
        return self._make_request(
            "/inventories/http_requests/{module}/devices/{name}".format(
                **path_params.model_dump()
            ),
            method="delete",
        )

    def delete_netconf_device(self, name: str, inventory_name: str = "default") -> dict:
        """
        Delete a device from the netconf inventory.

        :param name: Name of the netconf device.
        :param inventory_name: Optional. Name of inventory (default = "default").
        """
        path_params = PathParams(name=name, module=inventory_name)
        return self._make_request(
            "/inventories/netconf/{module}/devices/{name}".format(
                **path_params.model_dump()
            ),
            method="delete",
        )

    def delete_netmiko_device(self, name: str, inventory_name: str = "default") -> dict:
        """
        Delete a device from the default Netmiko inventory.

        :param name: Name of the Netmiko device.
        :param inventory_name: Optional. Name of inventory (default = "default").
        """
        path_params = PathParams(name=name, module=inventory_name)
        return self._make_request(
            "/inventories/netmiko/{module}/devices/{name}".format(
                **path_params.model_dump()
            ),
            method="delete",
        )

    def get_http_requests_device(
        self, name: str, inventory_name: str = "default"
    ) -> dict:
        """
        Get information for a device in the HTTP requests inventory.

        :param name: Name of the device.
        :param inventory_name: Optional. Name of inventory (default = "default").
        """
        path_params = PathParams(name=name, module=inventory_name)
        return self._make_request(
            "/inventories/http_requests/{module}/devices/{name}".format(
                **path_params.model_dump()
            )
        )

    def get_http_requests_device_group(
        self, group_name: str, inventory_name: str = "default"
    ) -> dict:
        """
        Get information for a HTTP requests device group in the specified inventory.

        :param group_name: Name of group.
        :param inventory_name: Optional. Name of inventory (default = "default").
        """
        path_params = PathParams(name=group_name, module=inventory_name)
        return self._make_request(
            "/inventories/http_requests/{module}/groups/{name}".format(
                **path_params.model_dump()
            )
        )

    def get_http_requests_device_group_children(
        self, group_name: str, inventory_name: str = "default"
    ) -> dict:
        """
        Get a list of child groups in the HTTP requests inventory device group.

        :param group_name: Name of group.
        :param inventory_name: Optional. Name of inventory (default = "default").
        """
        path_params = PathParams(name=group_name, module=inventory_name)
        return self._make_request(
            "/inventories/http_requests/{module}/groups/{name}/children".format(
                **path_params.model_dump()
            )
        )

    def get_http_requests_device_group_devices(
        self, group_name: str, inventory_name: str = "default"
    ) -> dict:
        """
        Get a list of devices in the HTTP requests inventory device group.

        :param group_name: Name of group.
        :param inventory_name: Optional. Name of inventory (default = "default").
        """
        path_params = PathParams(name=group_name, module=inventory_name)
        return self._make_request(
            "/inventories/http_requests/{module}/groups/{name}/devices".format(
                **path_params.model_dump()
            )
        )

    def get_http_requests_device_groups(
        self,
        inventory_name: str = "default",
        offset: int = 0,
        limit: int = 50,
        filter: str = None,
        order: str = "ascending",
    ) -> dict:
        """
        Get a list of HTTP requests device groups in specified inventory.

        :param inventory_name: Optional. Name of inventory (default = "default").
        :param offset: Optional.The number of items to skip before starting to collect the result set.
        :param limit: Optional.The number of items to return (default 50).
        :param filter: Optional.Response filter function with JSON name/value pair argument as string, i.e., 'contains({"name":"SW"})' Valid filter functions - contains, equals, startswith, endswith
        :param order: Optional. Sort indication. Available values : 'ascending' (default), 'descending'.
        """
        query_params = QueryParamsFilter(
            offset=offset, limit=limit, filter=filter, order=order
        )
        return self._make_request(
            f"/inventories/http_requests/{inventory_name}/groups",
            params=query_params.model_dump(exclude_none=True),
        )

    def get_http_requests_devices(
        self,
        inventory_name: str = "default",
        offset: int = 0,
        limit: int = 100,
        filter: str = None,
        order: str = "ascending",
    ) -> dict:
        """
        Get a list of devices in the HTTP requests inventory.

        :param inventory_name: Optional. Name of inventory (default = "default").
        :param offset: Optional.The number of items to skip before starting to collect the result set.
        :param limit: Optional.The number of items to return (default 100).
        :param filter: Optional.Response filter function with JSON name/value pair argument as string, i.e., 'contains({"name":"SW"})' Valid filter functions - contains, equals, startswith, endswith
        :param order: Optional. Sort indication. Available values : 'ascending' (default), 'descending'.
        """
        query_params = QueryParamsFilter(
            offset=offset, limit=limit, filter=filter, order=order
        )
        return self._make_request(
            f"/inventories/http_requests/{inventory_name}/devices",
            params=query_params.model_dump(exclude_none=True),
        )

    def get_netconf_device(self, name: str, inventory_name: str = "default") -> dict:
        """
        Get information for a device in the netconf inventory.

        :param name: Name of the device.
        :param inventory_name: Optional. Name of inventory (default = "default").
        """
        path_params = PathParams(name=name, module=inventory_name)
        return self._make_request(
            "/inventories/netconf/{module}/devices/{name}".format(
                **path_params.model_dump()
            )
        )

    def get_netconf_device_group(
        self, group_name: str, inventory_name: str = "default"
    ) -> dict:
        """
        Get information for a netconf device group in the specified inventory.

        :param group_name: Name of group.
        :param inventory_name: Optional. Name of inventory (default = "default").
        """
        path_params = PathParams(name=group_name, module=inventory_name)
        return self._make_request(
            "/inventories/netconf/{module}/groups/{name}".format(
                **path_params.model_dump()
            )
        )

    def get_netconf_device_group_children(
        self, group_name: str, inventory_name: str = "default"
    ) -> dict:
        """
        Get a list of child groups in the netconf inventory device group.

        :param group_name: Name of group.
        :param inventory_name: Optional. Name of inventory (default = "default").
        """
        path_params = PathParams(name=group_name, module=inventory_name)
        return self._make_request(
            "/inventories/netconf/{module}/groups/{name}/children".format(
                **path_params.model_dump()
            )
        )

    def get_netconf_device_group_devices(
        self, group_name: str, inventory_name: str = "default"
    ) -> dict:
        """
        Get a list of devices in the netconf inventory device group.

        :param group_name: Name of group.
        :param inventory_name: Optional. Name of inventory (default = "default").
        """
        path_params = PathParams(name=group_name, module=inventory_name)
        return self._make_request(
            "/inventories/netconf/{module}/groups/{name}/devices".format(
                **path_params.model_dump()
            )
        )

    def get_netconf_device_groups(
        self,
        inventory_name: str = "default",
        offset: int = 0,
        limit: int = 50,
        filter: str = None,
        order: str = "ascending",
    ) -> dict:
        """
        Get a list of netconf device groups in specified inventory.

        :param inventory_name: Optional. Name of inventory (default = "default").
        :param offset: Optional.The number of items to skip before starting to collect the result set.
        :param limit: Optional.The number of items to return (default 50).
        :param filter: Optional.Response filter function with JSON name/value pair argument as string, i.e., 'contains({"name":"SW"})' Valid filter functions - contains, equals, startswith, endswith
        :param order: Optional. Sort indication. Available values : 'ascending' (default), 'descending'.
        """
        query_params = QueryParamsFilter(
            offset=offset, limit=limit, filter=filter, order=order
        )
        return self._make_request(
            f"/inventories/netconf/{inventory_name}/groups",
            params=query_params.model_dump(exclude_none=True),
        )

    def get_netconf_devices(
        self,
        inventory_name: str = "default",
        offset: int = 0,
        limit: int = 100,
        filter: str = None,
        order: str = "ascending",
    ) -> dict:
        """
        Get a list of devices in the netconf inventory.

        :param inventory_name: Optional. Name of inventory (default = "default").
        :param offset: Optional.The number of items to skip before starting to collect the result set.
        :param limit: Optional.The number of items to return (default 100).
        :param filter: Optional.Response filter function with JSON name/value pair argument as string, i.e., 'contains({"name":"SW"})' Valid filter functions - contains, equals, startswith, endswith
        :param order: Optional. Sort indication. Available values : 'ascending' (default), 'descending'.
        """
        query_params = QueryParamsFilter(
            offset=offset, limit=limit, filter=filter, order=order
        )
        return self._make_request(
            f"/inventories/netconf/{inventory_name}/devices",
            params=query_params.model_dump(exclude_none=True),
        )

    def get_netmiko_device(self, name: str, inventory_name: str = "default") -> dict:
        """
        Get information for a Netmiko device in the specified inventory.

        :param name: Name of the device.
        :param inventory_name: Optional. Name of inventory (default = "default").
        """
        path_params = PathParams(name=name, module=inventory_name)
        return self._make_request(
            "/inventories/netmiko/{module}/devices/{name}".format(
                **path_params.model_dump()
            )
        )

    def get_netmiko_device_group(
        self, group_name: str, inventory_name: str = "default"
    ) -> dict:
        """
        Get information for a Netmiko device group in the specified inventory.

        :param group_name: Name of group.
        :param inventory_name: Optional. Name of inventory (default = "default").
        """
        path_params = PathParams(name=group_name, module=inventory_name)
        return self._make_request(
            "/inventories/netmiko/{module}/groups/{name}".format(
                **path_params.model_dump()
            )
        )

    def get_netmiko_device_group_children(
        self, group_name: str, inventory_name: str = "default"
    ) -> dict:
        """
        Get a list of child groups in the Netmiko inventory device group.

        :param group_name: Name of group.
        :param inventory_name: Optional. Name of inventory (default = "default").
        """
        path_params = PathParams(name=group_name, module=inventory_name)
        return self._make_request(
            "/inventories/netmiko/{module}/groups/{name}/children".format(
                **path_params.model_dump()
            )
        )

    def get_netmiko_device_group_devices(
        self, group_name: str, inventory_name: str = "default"
    ) -> dict:
        """
        Get a list of devices in the Netmiko inventory device group.

        :param group_name: Name of group.
        :param inventory_name: Optional. Name of inventory (default = "default").
        """
        path_params = PathParams(name=group_name, module=inventory_name)
        return self._make_request(
            "/inventories/netmiko/{module}/groups/{name}/devices".format(
                **path_params.model_dump()
            )
        )

    def get_netmiko_device_groups(
        self,
        inventory_name: str = "default",
        offset: int = 0,
        limit: int = 50,
        filter: str = None,
        order: str = "ascending",
    ) -> dict:
        """
        Get a list of Netmiko device groups in specified inventory.

        :param inventory_name: Optional. Name of inventory (default = "default").
        :param offset: Optional.The number of items to skip before starting to collect the result set.
        :param limit: Optional.The number of items to return (default 50).
        :param filter: Optional.Response filter function with JSON name/value pair argument as string, i.e., 'contains({"name":"SW"})' Valid filter functions - contains, equals, startswith, endswith
        :param order: Optional. Sort indication. Available values : 'ascending' (default), 'descending'.
        """
        query_params = QueryParamsFilter(
            offset=offset, limit=limit, filter=filter, order=order
        )
        return self._make_request(
            f"/inventories/netmiko/{inventory_name}/groups",
            params=query_params.model_dump(exclude_none=True),
        )

    def get_netmiko_devices(
        self,
        inventory_name: str = "default",
        offset: int = 0,
        limit: int = 100,
        filter: str = None,
        order: str = "ascending",
    ) -> dict:
        """
        Get a list of devices in the Netmiko inventory.

        :param inventory_name: Optional. Name of inventory (default = "default").
        :param offset: Optional.The number of items to skip before starting to collect the result set.
        :param limit: Optional.The number of items to return (default 100).
        :param filter: Optional.Response filter function with JSON name/value pair argument as string, i.e., 'contains({"name":"SW"})' Valid filter functions - contains, equals, startswith, endswith
        :param order: Optional. Sort indication. Available values : 'ascending' (default), 'descending'.
        """
        query_params = QueryParamsFilter(
            offset=offset, limit=limit, filter=filter, order=order
        )
        return self._make_request(
            f"/inventories/netmiko/{inventory_name}/devices",
            params=query_params.model_dump(exclude_none=True),
        )

    def update_http_requests_device(
        self,
        name: str,
        variables: dict[str, Any],
        inventory_name: str = "default",
        method: str = "put",
    ) -> dict:
        """
        Update a device in the http_requests inventory.
        Tip: Use get_http_requests_device() to get an idea of the format of the config_object.

        :param name: Name of the HTTP requests device.
        :param variables: dictionary containing the device definition.
        :param inventory_name: Optional. Name of inventory (default = "default").
        :param method: Optional. Choose between 'put' (default) and 'patch'.
        """
        body = InventoryHttpUpdateParameters(name=name, variables=variables)
        return self._make_request(
            f"/inventories/http_requests/{inventory_name}/devices/{name}",
            method=method,
            jsonbody=body.model_dump(exclude_none=True),
        )

    def update_netconf_device(
        self,
        name: str,
        variables: dict[str, Any],
        inventory_name: str = "default",
        method: str = "put",
    ) -> dict:
        """
        Update a device in the netconf inventory.
        Tip: Use get_netconf_device() to get an idea of the format of the config_object.

        :param name: Name of the netconf device.
        :param variables: dictionary containing the device definition.
        :param inventory_name: Optional. Name of inventory (default = "default").
        :param method: Optional. Choose between 'put' (default) and 'patch'.
        """
        body = InventoryNetconfUpdateParameters(name=name, variables=variables)
        return self._make_request(
            f"/inventories/netconf/{inventory_name}/devices/{name}",
            method=method,
            jsonbody=body.model_dump(exclude_none=True),
        )

    def update_netmiko_device(
        self,
        name: str,
        variables: dict[str, Any],
        inventory_name: str = "default",
        method: str = "put",
    ) -> dict:
        """
        Update a device in the default netmiko inventory.
        Tip: Use get_netmiko_device() to get an idea of the format of the config_object.

        :param name: Name of the Netmiko device.
        :param variables: dictionary containing the device definition.
        :param inventory_name: Optional. Name of inventory (default = "default").
        :param method: Choose between 'put' (default) and 'patch'.
        """
        body = InventoryNetmikoUpdateParameters(name=name, variables=variables)
        return self._make_request(
            f"/inventories/netmiko/{inventory_name}/devices/{name}",
            method=method,
            jsonbody=body.model_dump(exclude_none=True),
        )

    def refresh(self) -> dict:
        """
        Perform external inventory discovery and update internal cache.
        """
        return self._make_request("/inventory/refresh", method="post")
