import json
from typing import Dict, Union, Any

import requests
from requests import Session


class Auth:
    """Class which contains USERS API commands"""

    @staticmethod
    def logout(session: Session, basic_api_url: str, get_status: bool = True) -> Union[requests.Response, str]:
        """Authorization API Method which Ends up user session. Clears session cookies"""

        request = session.get(url=basic_api_url+'/auth/logout').json()["status"] \
            if get_status \
            else session.get(url=basic_api_url+'/auth/logout')
        return request

    @staticmethod
    def signup(session: Session, basic_api_url: str, data: Dict[str, Any], get_status: bool = True) -> Union[requests.Response, str]:
        """Authorization API Method which Registers NEW users in the system"""

        request = session.post(url=basic_api_url+'/auth/signup', data=data).json()["status"] \
            if get_status \
            else session.post(url=basic_api_url+'/auth/signup', data=data)
        return request

    @staticmethod
    def signin(session: Session, basic_api_url: str, data: Dict[str, Any], get_status: bool = True) -> Union[requests.Response, str]:
        """Authorization API Method which Registers EXISTING users in the system"""

        request = session.post(url=basic_api_url+'/auth/signin', data=data).json()["status"] \
            if get_status \
            else session.post(url=basic_api_url+'/auth/signin', data=data)
        return request


class Users:
    @staticmethod
    def current(session: Session, basic_api_url: str, get_status: bool = True) -> Union[requests.Response, str]:
        """Users API Method which authorization API Method which Registers EXISTING users in the system"""

        request = session.get(url=basic_api_url+'/users/current').json()["status"] \
            if get_status \
            else session.get(url=basic_api_url+'/users/current')
        return request

    @staticmethod
    def delete_user(session: Session, basic_api_url: str, get_status: bool = True):
        """Users API Method which Deletes user's account and current user session"""

        request = session.delete(url=basic_api_url+'/users').json()["status"] \
            if get_status \
            else session.delete(url=basic_api_url+'/users')
        return request


class TestDataProcessor:
    @classmethod
    def _get_test_data_from_json(cls, data_source: str):
        """Method which get data from json file"""

        with open(data_source) as file:
            return json.load(file)

    @classmethod
    def get_valid_user_data(cls, data_source: str):
        """Method which converts data from json to Dict

        :arg data_source str json file name
        :return Dictionary with data for user Sign UP

        """
        test_data = cls._get_test_data_from_json(data_source)
        return SignUpUserDataModel(
            name=test_data["name"],
            lastName=test_data["lastName"],
            email=test_data["email"],
            password=test_data["password"],
            repeatPassword=test_data["repeatPassword"],
        ).__dict__

    @classmethod
    def get_valid_signin_data(cls, data_source: str, remember_option_status: bool = False):
        """Method which converts data from json to Dict
        :arg data_source str json file name
        :arg remember_option_status: Default False
        :return Dictionary with data for user Sign IN

        """
        test_data = cls._get_test_data_from_json(data_source)
        return {
            "email": test_data["email"],
            "password": test_data["password"],
            "remember": str(remember_option_status)
        }


class SignUpUserDataModel:
    """Class which defines required fields for user SignUp"""

    def __init__(self, name, lastName, email, password, repeatPassword):
        self.name = name
        self.lastName = lastName
        self.email = email
        self.password = password
        self.repeatPassword = repeatPassword


class ApiTestBaseClass:
    """Class which contains basic data to provide API testing"""

    url = "https://qauto2.forstudy.space/api"
    session = requests.session()
    # Prepare test data Processor
    valid_signup_data = TestDataProcessor.get_valid_user_data(data_source='test_data/valid_user_data.json')
    valid_signin_data = TestDataProcessor.get_valid_signin_data(data_source='test_data/valid_user_data.json')