from copy import copy

from ..test_framework_web.api_engine import Auth, Users, ApiTestBaseClass
from ..test_framework_web.test_data import TestDataProcessor


class TestSignIn(ApiTestBaseClass):
    """Test class which contain SignIN tests with using API"""

    def setup_class(self):
        """Method Prepare registered test user and clean test session"""
        # Prepare test data
        self.valid_signup_data = TestDataProcessor().get_sign_up_data(test_data_src=self.data_source)
        self.valid_signin_data = TestDataProcessor().get_sign_in_data(test_data_src=self.data_source)

        Auth.signup(
            session=self.session, basic_api_url=self.url, data=self.valid_signup_data.__dict__
        )
        Auth.logout(session=self.session, basic_api_url=self.url)

    def teardown_class(self):
        """Method delete test user account via API"""
        Auth.signin(
            session=self.session, basic_api_url=self.url, data=self.valid_signin_data.__dict__
        )
        Users.delete_user(session=self.session, basic_api_url=self.url)
        self.session.close()

    def setup_method(self):
        """Method reset sign IN credentials to default"""

        self.signin_data = copy(self.valid_signin_data)

    def teardown_method(self):
        """Method delete log OUT test user account and clean test session after each test"""

        Auth.logout(session=self.session, basic_api_url=self.url)

    def test_sign_in_valid_data(self):
        """Test: Try to Sign IN with valid data and assert success status"""
        email = self.signin_data.email
        password = self.signin_data.password
        remember = False

        request = Auth.signin(
            session=self.session,
            basic_api_url=self.url,
            data={"email": email, "password": password, "remember": remember},
        )
        assert request["status"] == "ok", f'response: {request["message"]}. Used creds: {email}, {password}, {remember}'

    def test_sign_in_invalid_repeat_pass(self):
        """Test: Try to Sign IN with invalid data (invalid repeat password) and assert success status"""

        #  Preparing invalid test data
        email = self.signin_data.email
        password = "0"
        remember = False

        # Proceeds Sign Up POST request
        request = Auth.signin(
            session=self.session,
            basic_api_url=self.url,
            data={"email": email, "password": password, "remember": remember},
        )
        expected_response = (request["status"] == "error", request["message"] == 'Wrong email or password')
        assert all(expected_response) is True, f'{request["status"]}, {request["message"]}'
