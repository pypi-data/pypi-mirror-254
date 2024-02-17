import logging
from typing import Any, Optional, Union

import requests

logging.basicConfig(level=logging.INFO)


class ClientBase:
    """
    Base class the module classes inherit from. Provides generic query method.
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
        session: Optional[requests.Session] = None,
        token: Optional[str] = None,
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
        :param session: requests.session object (provided by Iag() class).
        :param token: Session token (provided by Iag() class).
        """
        self.host: str = host
        self.username: str = username
        self.password: str = password
        self.base_url: str = base_url
        self.protocol: str = protocol
        self.port: str = str(port)
        self.verify: bool = verify
        self.session = session
        self.token = token

    def login(self) -> None:
        try:
            headers = {
                "accept": "application/json",
                "Content-Type": "application/json",
            }
            auth_resp = self.session.post(
                f"{self.protocol}://{self.host}:{self.port}{self.base_url}/login",
                headers=headers,
                json={"username": self.username, "password": self.password},
                verify=self.verify,
            )
            auth_resp.raise_for_status()
            data = auth_resp.json()
            self.token = data.get("token")
            headers["Authorization"] = self.token
            self.session.headers.update(headers)
        except requests.exceptions.RequestException as auth_error:
            logging.log(
                logging.ERROR,
                msg=f"Unable to authenticate with {self.host} using {self.username}.",
            )
            logging.log(logging.ERROR, msg=str(auth_error))

    def logout(self) -> None:
        self.session.close()

    def _make_request(
        self,
        endpoint: str,
        method: str = "get",
        data: Optional[dict[str, Any]] = None,
        jsonbody: Optional[dict[str, Any]] = None,
        params: Optional[dict[str, Any]] = None,
    ) -> Optional[requests.Response]:
        """
        Issues a generic single request. Basically, a wrapper for "requests"
        using the already-stored host, headers, and verify parameters.

        :param endpoint: Itential IAG API endpoint. E.g. /devices.
        :param method: Optional. API method: get (default),post,put,patch,delete.
        :param data: Optional. A dictionary to send as the body.
        :param jsonbody: Optional. A JSON object to send as the body.
        :param params: Optional. A dictionary to send as URL parameters.
        """
        if not self.token:
            self.login()
        # check for and add missing leading forward slash in API endpoint
        if not endpoint.startswith("/"):
            endpoint = f"/{endpoint}"

        try:
            if method.upper() == "GET":
                response = self.session.get(
                    url=f"{self.protocol}://{self.host}:{self.port}{self.base_url}{endpoint}",
                    data=data,
                    json=jsonbody,
                    params=params,
                    verify=self.verify,
                )
            elif method.upper() == "POST":
                response = self.session.post(
                    url=f"{self.protocol}://{self.host}:{self.port}{self.base_url}{endpoint}",
                    data=data,
                    json=jsonbody,
                    params=params,
                    verify=self.verify,
                )
            elif method.upper() == "PUT":
                response = self.session.put(
                    url=f"{self.protocol}://{self.host}:{self.port}{self.base_url}{endpoint}",
                    data=data,
                    json=jsonbody,
                    params=params,
                    verify=self.verify,
                )
            elif method.upper() == "PATCH":
                response = self.session.patch(
                    url=f"{self.protocol}://{self.host}:{self.port}{self.base_url}{endpoint}",
                    data=data,
                    json=jsonbody,
                    params=params,
                    verify=self.verify,
                )
            elif method.upper() == "DELETE":
                response = self.session.delete(
                    url=f"{self.protocol}://{self.host}:{self.port}{self.base_url}{endpoint}",
                    data=data,
                    json=jsonbody,
                    params=params,
                    verify=self.verify,
                )

            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as error:
            logging.log(
                logging.ERROR,
                msg=f"Failed to retrieve response from {self.protocol}://{self.host}:{self.port}{self.base_url}{endpoint}.",
            )
            logging.log(logging.ERROR, msg=str(error))
            return None
