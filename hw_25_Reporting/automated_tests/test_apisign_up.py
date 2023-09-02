from copy import copy

from ..test_framework_web.api_engine import (
    Auth,
    Users,
    ApiTestBaseClass,
    CustomApiCalls,
)
from ..test_framework_web.test_data import TestDataProcessor


class TestSignUp(ApiTestBaseClass):
    """Test class which contain SignUP tests with using API"""

    def setup_class(self):
        """Method Prepare NOT registered test user
        Try to sign IN and delete test account if test user is registered

        """
        # Prepare test data
        self.valid_signup_data = TestDataProcessor().get_sign_up_data(test_data_src=self.data_source)
        self.valid_signin_data = TestDataProcessor().get_sign_in_data(test_data_src=self.data_source)

        CustomApiCalls.delete_registered_user_via_api(
            session=self.session, url=self.url, valid_signin_data=self.valid_signin_data.__dict__
        )

    def setup_method(self):
        self.sign_in_creds = copy(self.valid_signin_data.__dict__)
        self.sign_up_creds = copy(self.valid_signup_data.__dict__)

    def test_sign_up_valid_data(self):
        """Test: Try to Sign UP with valid data and assert success status"""
        request = Auth.signup(
            session=self.session,
            basic_api_url=self.url,
            data=self.sign_up_creds,
        )
        assert request["status"] == "ok", request["message"]

    def test_sign_up_invalid_repeat_pass(self):
        """Test: Try to Sign UP with invalid data and assert success status"""

        #  Preparing (invalidate) test data
        invalid_data = self.sign_up_creds
        invalid_data["repeatPassword"] = 0

        # Proceeds Sign Up POST request
        request = Auth.signup(
            session=self.session,
            basic_api_url=self.url,
            data=invalid_data,
        )
        assert request["status"] != "ok", request["message"]

    def teardown_method(self):
        """Method delete test user after each case"""

        Auth.signin(
            session=self.session,
            basic_api_url=self.url,
            data= self.valid_signup_data,
        )
        Users.delete_user(session=self.session, basic_api_url=self.url)

    def teardown_class(self):
        self.session.close()
