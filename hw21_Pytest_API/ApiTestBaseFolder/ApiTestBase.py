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


class TestDataProcessor:
    @staticmethod
    def _get_test_data_from_json(data_source: str):
        """Method which get data from json file"""

        with open(file=data_source) as file:
            return json.load(file)

    @staticmethod
    def _get_sign_up_data(test_data):
        return {
            "name": test_data["name"],
            "lastName": test_data["lastName"],
            "email": test_data["email"],
            "password": test_data["password"],
            "repeatPassword": test_data["repeatPassword"],
        }

    @staticmethod
    def _get_sign_in_data(test_data, remember_option_status: bool = False):
        return {
            "email": test_data["email"],
            "password": test_data["password"],
            "remember": str(remember_option_status),
        }

    @staticmethod
    def valid_test_data(data_source: str, remember_option_status_sign_in: bool = False):
        test_data = TestDataProcessor._get_test_data_from_json(data_source=data_source)
        return [
            TestDataProcessor._get_sign_up_data(test_data),
            TestDataProcessor._get_sign_in_data(
                test_data, remember_option_status=remember_option_status_sign_in
            ),
        ]


class ApiTestBaseClass:
    """Class which contains basic data to provide API testing"""

    session = requests.session()
    url = "https://qauto2.forstudy.space/api"
    data_source = r"D:/Courses/Hillel_AQA/Hillel_AQA_homeworks/hw21_Pytest_API/ApiTestBaseFolder/test_data/validUserData.json"

    # Prepare test data
    (
        valid_signup_data,
        valid_signin_data,
    ) = TestDataProcessor.valid_test_data(
        data_source, remember_option_status_sign_in=True
    )


class CustomApiCalls(ApiTestBaseClass):
    @staticmethod
    def delete_registered_user_via_api(
        session: Session, url: str, valid_signin_data: Dict
    ):
        if (
            Auth.signin(
                session=session,
                basic_api_url=url,
                data=valid_signin_data,
            )["status"]
            == "ok"
        ):
            Users.delete_user(session=session, basic_api_url=url)
