import json
from dataclasses import dataclass


class TestDataProcessor:
    @staticmethod
    def _get_test_data_from_json(data_source: str):
        """Method which get data from json file"""

        with open(file=data_source, mode='r') as file:
            return json.load(file)

    @staticmethod
    def get_sign_up_data(test_data_src):
        test_data = TestDataProcessor._get_test_data_from_json(data_source=test_data_src)
        filtered_test_data = ValidSignUpData(
            name=test_data["name"],
            lastname=test_data["lastName"],
            email=test_data["email"],
            password=test_data["password"],
            repeatpassword=test_data["repeatPassword"],
        )
        return filtered_test_data

    @staticmethod
    def get_sign_in_data(test_data_src, remember_option_status: bool = False):
        test_data = TestDataProcessor._get_test_data_from_json(data_source=test_data_src)
        filtered_test_data = ValidSignInData(
            email=test_data["email"],
            password=test_data["password"],
            remember=remember_option_status,
        )
        return filtered_test_data


class ValidSignUpData(dict):
    def __init__(
        self, name: str, lastname: str, email: str, password: str, repeatpassword: str
    ):
        super().__init__()
        self.name = name
        self.lastName = lastname
        self.email = email
        self.password = password
        self.repeatPassword = repeatpassword

    def __repr__(self):
        self.__setitem__("name", self.name)
        self.__setitem__("lastName", self.lastName)
        self.__setitem__("email", self.email)
        self.__setitem__("password", self.password)
        self.__setitem__("repeatPassword", self.repeatPassword)
        return super().__repr__()


@dataclass
class ValidSignInData(dict):
    def __init__(self, email: str, password: str, remember: bool = False):
        super().__init__()
        self.email = email
        self.password = password
        self.remember = remember

    def __repr__(self):
        self.__setitem__("email", self.email)
        self.__setitem__("password", self.password)
        self.__setitem__("remember", self.remember)
        return super().__repr__()
