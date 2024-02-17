from typing import Optional, Union

from iag_sdk.client_base import ClientBase
from iag_sdk.models import (
    PathParam,
    QueryParams,
    QueryParamsDetail,
    Schema,
    TerraformParameters,
)


class Terraform(ClientBase):
    """
    Class that contains methods for the IAG Terraforms API routes.
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
        Remove a Terraform module schema.

        :param name: Name of the terraform module.
        """
        path_params = PathParam(name=name)
        return self._make_request(
            "/terraforms/{name}/schema".format(**path_params.model_dump()),
            method="delete",
        )

    def execute_terraform_apply(
        self, name: str, args: dict, strict_args: bool = None
    ) -> dict:
        """
        Apply the configuration of a Terraform module.

        :param name: Name of terraform module to apply.
        :param args: Terraform Parameters.
        :param strict_args: Optional. Override global strict args setting
        """
        path_params = PathParam(name=name)
        body = TerraformParameters(args=args, strict_args=strict_args)
        return self._make_request(
            "/terraforms/{name}/terraform_apply".format(**path_params.model_dump()),
            method="post",
            jsonbody=body.model_dump(exclude_none=True),
        )

    def execute_terraform_destroy(
        self, name: str, args: dict, strict_args: bool = None
    ) -> dict:
        """
        Destroy the resources of a Terraform module.

        :param name: Name of terraform module to destroy.
        :param args: Terraform Parameters.
        :param strict_args: Optional. Override global strict args setting
        """
        path_params = PathParam(name=name)
        body = TerraformParameters(args=args, strict_args=strict_args)
        return self._make_request(
            "/terraforms/{name}/terraform_destroy".format(**path_params.model_dump()),
            method="post",
            jsonbody=body.model_dump(exclude_none=True),
        )

    def execute_terraform_init(
        self, name: str, args: dict, strict_args: bool = None
    ) -> dict:
        """
        Initialize the providers of a Terraform module.

        :param name: Name of terraform module to init.
        :param args: Terraform Parameters.
        :param strict_args: Optional. Override global strict args setting
        """
        path_params = PathParam(name=name)
        body = TerraformParameters(args=args, strict_args=strict_args)
        return self._make_request(
            "/terraforms/{name}/terraform_init".format(**path_params.model_dump()),
            method="post",
            jsonbody=body.model_dump(exclude_none=True),
        )

    def execute_terraform_plan(
        self, name: str, args: dict, strict_args: bool = None
    ) -> dict:
        """
        Plan the execution of a Terraform module.

        :param name: Name of terraform module to plan.
        :param args: Terraform Parameters.
        :param strict_args: Optional. Override global strict args setting
        """
        path_params = PathParam(name=name)
        body = TerraformParameters(args=args, strict_args=strict_args)
        return self._make_request(
            "/terraforms/{name}/terraform_plan".format(**path_params.model_dump()),
            method="post",
            jsonbody=body.model_dump(exclude_none=True),
        )

    def execute_terraform_validate(
        self, name: str, args: dict, strict_args: bool = None
    ) -> dict:
        """
        Validate the configuration of a Terraform module.

        :param name: Name of terraform module to validate.
        :param args: Terraform Parameters.
        :param strict_args: Optional. Override global strict args setting
        """
        path_params = PathParam(name=name)
        body = TerraformParameters(args=args, strict_args=strict_args)
        return self._make_request(
            "/terraforms/{name}/terraform_validate".format(**path_params.model_dump()),
            method="post",
            jsonbody=body.model_dump(exclude_none=True),
        )

    def get_module(self, name) -> dict:
        """
        Get information on a Terraform module.

        :param name: Name of the terraform module.
        """
        path_params = PathParam(name=name)
        return self._make_request(
            "/terraforms/{name}".format(**path_params.model_dump())
        )

    def get_module_history(
        self, name: str, offset: int = 0, limit: int = 10, order: str = "descending"
    ) -> dict:
        """
        Get execution log events for a Terraform module.
        Tip: Use get_audit_log() and the audit_id returned by this call, to get the details of the execution.

        :param name: Name of the terraform module.
        :param offset: Optional. The number of items to skip before starting to collect the result set.
        :param limit: Optional. The number of items to return.
        :param order: Optional. Sort indication. Available values : ascending, descending (default).
        """
        path_params = PathParam(name=name)
        query_params = QueryParams(offset=offset, limit=limit, order=order)
        return self._make_request(
            "/terraforms/{name}/history".format(**path_params.model_dump()),
            params=query_params.model_dump(),
        )

    def get_module_schema(self, name: str) -> dict:
        """
        Get the schema for a Terraform module.

        :param name: Name of the terraform module.
        """
        path_params = PathParam(name=name)
        return self._make_request(
            f"/terraforms/{name}/schema".format(**path_params.model_dump())
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
        Get list of Terraform modules.

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
            "/terraforms", params=query_params.model_dump(exclude_none=True)
        )

    def refresh(self) -> dict:
        """
        Perform Terraform discovery and update internal cache.
        """
        return self._make_request("/terraforms/refresh", method="post")

    def update_module_schema(self, name: str, schema_object: dict) -> dict:
        """
        Update/Insert a Terraform schema document.

        :param name: Name of script.
        :param schema_object: Schema to apply to terraform module identified in path.
        """
        path_params = PathParam(name=name)
        body = Schema(**schema_object)
        return self._make_request(
            "/terraforms/{name}/schema".format(**path_params.model_dump()),
            method="put",
            jsonbody=body.model_dump(exclude_none=True),
        )
