import json
from typing import Dict, Any

import requests
from requests import Session


class Auth:
    """Class which contains USERS API commands"""

    @staticmethod
    def logout(session: Session, basic_api_url: str) -> json:
        """Authorization API Method which Ends up user session. Clears session cookies"""

        return session.get(url=basic_api_url + "/auth/logout").json()

    @staticmethod
    def signup(session: Session, basic_api_url: str, data: Dict[str, Any]) -> json:
        """Authorization API Method which Registers NEW users in the system"""
        return session.post(url=basic_api_url + "/auth/signup", data=data).json()

    @staticmethod
    def signin(session: Session, basic_api_url: str, data: Dict[str, Any]) -> json:
        """Authorization API Method which Registers EXISTING users in the system"""

        return session.post(url=basic_api_url + "/auth/signin", data=data).json()


class Users:
    @staticmethod
    def current(session: Session, basic_api_url: str) -> json:
        """Users API Method which authorization API Method which Registers EXISTING users in the system"""

        return session.get(url=basic_api_url + "/users/current").json()

    @staticmethod
    def delete_user(session: Session, basic_api_url: str) -> json:
        """Users API Method which Deletes user's account and current user session"""

        return session.delete(url=basic_api_url + "/users").json()


class ApiTestBaseClass:
    """Class which contains basic data to provide API testing"""

    session = requests.session()
    url = "https://qauto2.forstudy.space/api"

    project_path = r'D:\Courses\Hillel_AQA\Hillel_AQA_homeworks'
    data_source = project_path + r'\hw_24_API_Selenium_test_project\test_framework_web\test_data\validUserData.json'


class CustomApiCalls(ApiTestBaseClass):
    @staticmethod
    def delete_registered_user_via_api(
        session: Session, url: str, valid_signin_data: Dict
    ):
        try_login = Auth.signin(
                session=session,
                basic_api_url=url,
                data=valid_signin_data,
        )
        if try_login["status"] == "ok":
            Users.delete_user(session=session, basic_api_url=url)
