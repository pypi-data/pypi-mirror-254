from typing import Optional, Union

from iag_sdk.client_base import ClientBase
from iag_sdk.models import (
    AccountParameters,
    AccountUpdateParameters,
    AccountUpdatePassword,
    PathParam,
    QueryParamsFilter,
)


class Account(ClientBase):
    """
    Class that contains methods for the IAG Accounts API routes.
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

    def add_account(
        self,
        username: str,
        password: str,
        email: str,
        firstname: Optional[str] = None,
        lastname: Optional[str] = None,
    ) -> dict:
        """
        Add a new user account.

        :param username: Username for the account.
        :param password: Password for the account.
        :param email: Email address of user.
        :param firstname: Optional. First name of user.
        :param lastname: Optional. Last name of user.
        """
        body = AccountParameters(
            email=email,
            firstname=firstname,
            lastname=lastname,
            password=password,
            username=username,
        )
        return self._make_request(
            "/accounts", method="post", jsonbody=body.model_dump(exclude_none=True)
        )

    def confirm_eula(self, name: str) -> dict:
        """
        Confirm EULA for an account.

        :param name: Name of user account
        """
        path_params = PathParam(name=name)
        return self._make_request(
            "/accounts/{name}/confirm_eula".format(**path_params.model_dump()),
            method="post",
        )

    def delete_account(self, name: str) -> dict:
        """
        Delete a user account.

        :param name: Name of user account
        """
        path_params = PathParam(name=name)
        return self._make_request(
            "/accounts/{name}".format(**path_params.model_dump()), method="delete"
        )

    def get_account(self, name: str) -> dict:
        """
        Get information for a user account.

        :param name: Name of the user account.
        """
        path_params = PathParam(name=name)
        return self._make_request("/accounts/{name}".format(**path_params.model_dump()))

    def get_accounts(
        self,
        offset: int = 0,
        limit: int = 50,
        filter: str = None,
        order: str = "ascending",
    ) -> dict:
        """
        Get a list of user accounts.

        :param offset: Optional. The number of items to skip before starting to collect the result set.
        :param limit: Optional. Number of results to return (default 50).
        :param filter: Optional. Response filter function with JSON name/value pair argument, i.e., 'contains({"username":"admin"})' Valid filter functions - contains, equals, startswith, endswith
        :param order: Optional. Sort indication. Available values : 'ascending' (default), 'descending'.
        """
        query_params = QueryParamsFilter(
            offset=offset, limit=limit, filter=filter, order=order
        )
        return self._make_request(
            "/accounts", params=query_params.model_dump(exclude_none=True)
        )

    def update_account(
        self, name: str, email: str, firstname: str, lastname: str
    ) -> dict:
        """
        Update details of a user account.
        Tip: Use get_account() to get an idea of the format of the config_object.

        :param name: Name of user account
        :param config_object: dictionary containing the variables to be updated.
        """
        path_params = PathParam(name=name)
        body = AccountUpdateParameters(
            email=email, firstname=firstname, lastname=lastname
        )
        return self._make_request(
            "/accounts/{name}".format(**path_params.model_dump()),
            method="put",
            jsonbody=body.model_dump(),
        )

    def update_password(self, name: str, old_password: str, new_password: str) -> dict:
        """
        Update user login credentials.

        :param name: Name of user account
        :param old_password: Old user password.
        :param new_password: New user password.
        """
        path_params = PathParam(name=name)
        body = AccountUpdatePassword(
            new_password=new_password, old_password=old_password
        )
        return self._make_request(
            "/accounts/{name}/update_password".format(**path_params.model_dump()),
            method="post",
            jsonbody=body.model_dump(),
        )
