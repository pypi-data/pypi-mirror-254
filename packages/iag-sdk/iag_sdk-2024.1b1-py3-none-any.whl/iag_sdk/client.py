import logging
from typing import Any, Optional, Union

import requests

from iag_sdk.client_base import ClientBase
from iag_sdk.modules import (
    Account,
    Collection,
    Config,
    Device,
    Group,
    HttpRequest,
    Inventory,
    Ldap,
    Module,
    Netconf,
    Netmiko,
    Nornir,
    PasswordReset,
    Playbook,
    Pronghorn,
    Rbac,
    Role,
    Script,
    Secret,
    SecurityQuestion,
    System,
    Terraform,
    UserSchema,
)

logging.basicConfig(level=logging.INFO)


class Iag(ClientBase):
    def __init__(
        self,
        host: str,
        username: str,
        password: str,
        base_url: Optional[str] = "/api/v2.0",
        protocol: Optional[str] = "http",
        port: Optional[Union[int, str]] = 8083,
        verify: Optional[bool] = True,
    ) -> None:
        """
        Constructor to build a new object. Automatically collects an
        authorization token and assembles the headers used for all
        future requests.

        :param host: Itential IAG FQDN or IP address.
        :param username: Username for IAG login.
        :param password: Password for IAG login.
        :param base_url: Optional. The initial part of the IAG API URL (default "/api/v2.0").
        :param protocol: Option. Choose between "http" (default) and "https".
        :param port: Optonal. Select server port (default 8083).
        :param verify: Optional. Verify/ignore SSL certificates (default True)
        """
        self.host: str = host
        self.username: str = username
        self.password: str = password
        self.base_url: str = base_url
        self.protocol: str = protocol
        self.port: str = str(port)
        self.verify: bool = verify
        self.session = requests.Session()
        self.token = None
        # If verify is false, we should disable unnecessary SSL logging
        if not verify:
            requests.packages.urllib3.disable_warnings()
        # Build common headers
        self.headers = {
            "accept": "application/json",
            "Content-Type": "application/json",
        }
        # ensure base_url starts with a forward slash
        if not self.base_url.startswith("/"):
            self.base_url = f"/{self.base_url}"
        # ensure host value does not contain protocol or port information
        if "://" in self.host:
            self.host = self.host.split(":")[1]
        if ":" in self.host:
            self.host = self.host.split(":")[0]
        # get a token
        self.login()
        # update headers with authorization token
        self.session.headers.update(self.headers)
        super().__init__(
            self.host,
            self.username,
            self.password,
            self.base_url,
            self.protocol,
            self.port,
            self.verify,
            self.session,
            self.token,
        )

    def login(self) -> None:
        try:
            auth_resp = self.session.post(
                f"{self.protocol}://{self.host}:{self.port}{self.base_url}/login",
                headers=self.headers,
                json={"username": self.username, "password": self.password},
                verify=self.verify,
            )
            auth_resp.raise_for_status()
            data = auth_resp.json()
            self.token = data.get("token")
            self.headers["Authorization"] = self.token
        except requests.exceptions.RequestException as auth_error:
            logging.log(
                logging.ERROR,
                msg=f"Unable to authenticate with {self.host} using {self.username}.",
            )
            logging.log(logging.ERROR, msg=str(auth_error))

    def logout(self) -> None:
        self.session.close()

    def query(
        self,
        endpoint: str,
        method: Optional[str] = "get",
        data: Optional[dict[str, Any]] = None,
        jsonbody: Optional[dict[str, Any]] = None,
        params: Optional[dict[str, Any]] = None,
    ) -> Optional[dict[str, Any]]:
        """
        Issues a generic single request. Basically, a wrapper for "requests"
        using the already-stored host, headers, and verify parameters.

        :param endpoint: Itential IAG API endpoint. E.g. /devices.
        :param method: Optional. API method: get (default),post,put,patch,delete.
        :param data: Optional. A dictionary to send as the body.
        :param jsonbody: Optional. A JSON object to send as the body.
        :param params: Optional. A dictionary to send as URL parameters.
        """
        return self._make_request(
            endpoint=endpoint,
            method=method,
            data=data,
            jsonbody=jsonbody,
            params=params,
        )

    @property
    def accounts(self) -> Account:
        return Account(
            self.host,
            self.username,
            self.password,
            self.base_url,
            self.protocol,
            self.port,
            self.verify,
            self.session,
            self.token,
        )

    @property
    def collections(self) -> Collection:
        return Collection(
            self.host,
            self.username,
            self.password,
            self.base_url,
            self.protocol,
            self.port,
            self.verify,
            self.session,
            self.token,
        )

    @property
    def config(self) -> Config:
        return Config(
            self.host,
            self.username,
            self.password,
            self.base_url,
            self.protocol,
            self.port,
            self.verify,
            self.session,
            self.token,
        )

    @property
    def devices(self) -> Device:
        return Device(
            self.host,
            self.username,
            self.password,
            self.base_url,
            self.protocol,
            self.port,
            self.verify,
            self.session,
            self.token,
        )

    @property
    def groups(self) -> Group:
        return Group(
            self.host,
            self.username,
            self.password,
            self.base_url,
            self.protocol,
            self.port,
            self.verify,
            self.session,
            self.token,
        )

    @property
    def http_requests(self) -> HttpRequest:
        return HttpRequest(
            self.host,
            self.username,
            self.password,
            self.base_url,
            self.protocol,
            self.port,
            self.verify,
            self.session,
            self.token,
        )

    @property
    def inventory(self) -> Inventory:
        return Inventory(
            self.host,
            self.username,
            self.password,
            self.base_url,
            self.protocol,
            self.port,
            self.verify,
            self.session,
            self.token,
        )

    @property
    def ldap(self) -> Ldap:
        return Ldap(
            self.host,
            self.username,
            self.password,
            self.base_url,
            self.protocol,
            self.port,
            self.verify,
            self.session,
            self.token,
        )

    @property
    def modules(self) -> Module:
        return Module(
            self.host,
            self.username,
            self.password,
            self.base_url,
            self.protocol,
            self.port,
            self.verify,
            self.session,
            self.token,
        )

    @property
    def netconf(self) -> Netconf:
        return Netconf(
            self.host,
            self.username,
            self.password,
            self.base_url,
            self.protocol,
            self.port,
            self.verify,
            self.session,
            self.token,
        )

    @property
    def netmiko(self) -> Netmiko:
        return Netmiko(
            self.host,
            self.username,
            self.password,
            self.base_url,
            self.protocol,
            self.port,
            self.verify,
            self.session,
            self.token,
        )

    @property
    def nornir(self) -> Nornir:
        return Nornir(
            self.host,
            self.username,
            self.password,
            self.base_url,
            self.protocol,
            self.port,
            self.verify,
            self.session,
            self.token,
        )

    @property
    def password_reset(self) -> PasswordReset:
        return PasswordReset(
            self.host,
            self.username,
            self.password,
            self.base_url,
            self.protocol,
            self.port,
            self.verify,
            self.session,
            self.token,
        )

    @property
    def playbooks(self) -> Playbook:
        return Playbook(
            self.host,
            self.username,
            self.password,
            self.base_url,
            self.protocol,
            self.port,
            self.verify,
            self.session,
            self.token,
        )

    @property
    def pronghorn(self) -> Pronghorn:
        return Pronghorn(
            self.host,
            self.username,
            self.password,
            self.base_url,
            self.protocol,
            self.port,
            self.verify,
            self.session,
            self.token,
        )

    @property
    def rbac(self) -> Rbac:
        return Rbac(
            self.host,
            self.username,
            self.password,
            self.base_url,
            self.protocol,
            self.port,
            self.verify,
            self.session,
            self.token,
        )

    @property
    def roles(self) -> Role:
        return Role(
            self.host,
            self.username,
            self.password,
            self.base_url,
            self.protocol,
            self.port,
            self.verify,
            self.session,
            self.token,
        )

    @property
    def scripts(self) -> Script:
        return Script(
            self.host,
            self.username,
            self.password,
            self.base_url,
            self.protocol,
            self.port,
            self.verify,
            self.session,
            self.token,
        )

    @property
    def secrets(self) -> Secret:
        return Secret(
            self.host,
            self.username,
            self.password,
            self.base_url,
            self.protocol,
            self.port,
            self.verify,
            self.session,
            self.token,
        )

    @property
    def security_questions(self) -> SecurityQuestion:
        return SecurityQuestion(
            self.host,
            self.username,
            self.password,
            self.base_url,
            self.protocol,
            self.port,
            self.verify,
            self.session,
            self.token,
        )

    @property
    def system(self) -> System:
        return System(
            self.host,
            self.username,
            self.password,
            self.base_url,
            self.protocol,
            self.port,
            self.verify,
            self.session,
            self.token,
        )

    @property
    def terraforms(self) -> Terraform:
        return Terraform(
            self.host,
            self.username,
            self.password,
            self.base_url,
            self.protocol,
            self.port,
            self.verify,
            self.session,
            self.token,
        )

    @property
    def user_schema(self) -> UserSchema:
        return UserSchema(
            self.host,
            self.username,
            self.password,
            self.base_url,
            self.protocol,
            self.port,
            self.verify,
            self.session,
            self.token,
        )
