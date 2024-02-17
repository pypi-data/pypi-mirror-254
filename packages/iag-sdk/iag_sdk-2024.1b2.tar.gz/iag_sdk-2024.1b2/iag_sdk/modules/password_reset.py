from typing import Optional, Union

from iag_sdk.client_base import ClientBase
from iag_sdk.models import (
    PasswordResetParameters,
    PasswordUpdateParameters,
    PasswordUpdateQuestionsParameters,
    PathParam,
)


class PasswordReset(ClientBase):
    """
    Class that contains methods for the IAG password_reset API routes.
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

    def reset_password(
        self,
        username: str,
        email: str,
        new_password: str,
        security_ques1: str,
        security_ques1_ans: str,
        security_ques2: str,
        security_ques2_ans: str,
        temp_password: str,
    ) -> dict:
        """
        Reset password for user on the AG server.

        :param username: Username of account.
        :param email: Email address of account.
        :param new_password: The new password.
        :param security_ques1: Security question #1.
        :param security_ques1_ans: Answer to security question #1.
        :param security_ques2: Security question #2.
        :param security_ques2_ans: Answer to security question #2.
        :param temp_password: Temporary password.
        """
        body = PasswordResetParameters(
            username=username,
            email=email,
            new_password=new_password,
            security_ques1=security_ques1,
            security_ques1_ans=security_ques1_ans,
            security_ques2=security_ques2,
            security_ques2_ans=security_ques2_ans,
            temp_password=temp_password,
        )
        return self._make_request(
            "/password_reset", method="post", jsonbody=body.model_dump()
        )

    def update_password(
        self,
        username: str,
        email: str,
        password: str,
        security_ques1: str = None,
        security_ques1_ans: str = None,
        security_ques2: str = None,
        security_ques2_ans: str = None,
    ) -> dict:
        """
        Update password for user on the AG server.

        :param username: Username of account.
        :param email: Email address of account.
        :param password: The new password.
        :param security_ques1: Optional. Security question #1.
        :param security_ques1_ans: Optional. Answer to security question #1.
        :param security_ques2: Optional. Security question #2.
        :param security_ques2_ans: Optional. Answer to security question #2.
        """
        body = PasswordUpdateParameters(
            username=username,
            email=email,
            password=password,
            security_ques1=security_ques1,
            security_ques1_ans=security_ques1_ans,
            security_ques2=security_ques2,
            security_ques2_ans=security_ques2_ans,
        )
        return self._make_request(
            "/password_reset/update",
            method="post",
            jsonbody=body.model_dump(exclude_none=True),
        )

    def update_change_flag(self, username: str) -> dict:
        """
        Update the password change flag to false on the AG server.

        :param username: Username of account.
        """
        path_params = PathParam(name=username)
        return self._make_request(
            "/password_reset/update_flag/{name}".format(**path_params.model_dump()),
            method="post",
        )

    def update_security_questions(
        self,
        username: str,
        security_ques1: str,
        security_ques1_ans: str,
        security_ques2: str,
        security_ques2_ans: str,
    ) -> dict:
        """
        Update security questions and answers for user on the AG server.

        :param username: Username of account.
        :param security_ques1: Optional. Security question #1.
        :param security_ques1_ans: Optional. Answer to security question #1.
        :param security_ques2: Optional. Security question #2.
        :param security_ques2_ans: Optional. Answer to security question #2.
        """
        body = PasswordUpdateQuestionsParameters(
            username=username,
            security_ques1=security_ques1,
            security_ques1_ans=security_ques1_ans,
            security_ques2=security_ques2,
            security_ques2_ans=security_ques2_ans,
        )
        return self._make_request(
            "/password_reset/update_questions",
            method="post",
            jsonbody=body.model_dump(),
        )

    def validate_password_change(self, username: str) -> dict:
        """
        Validate if password is changed in the IAG server

        :param username: Username of account.
        """
        path_params = PathParam(name=username)
        return self._make_request(
            "/password_reset/validate_pass_change/{name}".format(
                **path_params.model_dump()
            ),
            method="post",
        )
