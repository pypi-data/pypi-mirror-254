from typing import Any, Optional, Union

from iag_sdk.client_base import ClientBase
from iag_sdk.models import (
    DeviceAddParameters,
    DeviceUpdateParameters,
    PathParam,
    PathParams,
    QueryParamsFilter,
    UpdateMethod,
)


class Device(ClientBase):
    """
    Class that contains methods for the IAG Devices API routes.
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

    def add_device(self, name: str, variables: dict[str, Any]) -> dict:
        """
        Add a new device to Ansible inventory.
        Tip: Use get_device() to get an idea of the format of the variables dict.

        :param name: Name of the device.
        :param variables: Dictionary containing the device definition.
        """
        body = DeviceAddParameters(name=name, variables=variables)
        return self._make_request(
            "/devices", method="post", jsonbody=body.model_dump(exclude_none=True)
        )

    def delete_device(self, name: str) -> dict:
        """
        Delete a device from Ansible inventory.

        :param name: Name of the device.
        """
        path_params = PathParam(name=name)
        return self._make_request(
            "/devices/{name}".format(**path_params.model_dump()), method="delete"
        )

    def get_device(self, name: str) -> dict:
        """
        Get information for an Ansible device.

        :param name: Name of device.
        """
        path_params = PathParam(name=name)
        return self._make_request("/devices/{name}".format(**path_params.model_dump()))

    def get_device_state(self, name: str) -> dict:
        """
        Get the connectivity state for an Ansible device.

        :param name: Name of device.
        """
        path_params = PathParam(name=name)
        return self._make_request(
            "/devices/{name}/state".format(**path_params.model_dump())
        )

    def get_device_variable(self, name: str, variable_name: str) -> dict:
        """
        Get the value of a connection variable for an Ansible device.

        :param name: Name of device.
        :param variable_name: Name of variable.
        """
        path_params = PathParams(name=name, module=variable_name)
        return self._make_request(
            "/devices/{name}/variables/{module}".format(**path_params.model_dump())
        )

    def get_device_variables(self, name: str) -> dict:
        """
        Get the connection variables for an Ansible device.

        :param name: Name of device.
        """
        path_params = PathParam(name=name)
        return self._make_request(
            "/devices/{name}/variables".format(**path_params.model_dump())
        )

    def get_devices(
        self,
        offset: int = 0,
        limit: int = 100,
        filter: str = None,
        order: str = "ascending",
    ) -> dict:
        """
        Get a list of Ansible devices.

        :param offset: Optional. The number of items to skip before starting to collect the result set.
        :param limit: Optional. The number of items to return (default 100).
        :param filter: Optional. Response filter function with JSON name/value pair argument as string, i.e., 'contains({"name":"SW"})' Valid filter functions - contains, equals, startswith, endswith
        :param order: Optional. Sort indication. Available values : 'ascending' (default), 'descending'.

        """
        query_params = QueryParamsFilter(
            offset=offset, limit=limit, filter=filter, order=order
        )
        return self._make_request(
            "/devices", params=query_params.model_dump(exclude_none=True)
        )

    def update_device(
        self, name: str, variables: dict[str, Any], method: str = "put"
    ) -> dict:
        """
        Replace the variables for a device in the Ansible inventory.
        Use get_device() to get an idea of the format of the variables dict.

        :param name: Name of the device.
        :param variables: Dictionary containing the variables to be updated.
        :param method: Optional. Choose between 'put' (default) and 'patch'.
        """
        path_params = PathParam(name=name)
        rest_method = UpdateMethod(method=method.lower())
        body = DeviceUpdateParameters(variables=variables)
        return self._make_request(
            "/devices/{name}".format(**path_params.model_dump()),
            method=rest_method.method,
            jsonbody=body.variables,
        )
