from ApiTestBase.ApiTestBase import Auth, Users, ApiTestBaseClass
import requests


class TestSignUp(ApiTestBaseClass):

    def setup_method(self):
        # Prepare NOT registered test user || Try to sign IN and delete test account if test user is registered
        if Auth.signin(session=self.session, basic_api_url=self.url, data=self.valid_signin_data) == "ok":
            Users.delete_user(session=self.session, basic_api_url=self.url, get_status=False)
        self.valid_signup_test_data = self.valid_signup_data

    def test_sign_up_valid_data(self):
        status = Auth.signup(session=self.session, basic_api_url=self.url, data=self.valid_signup_test_data)
        print('valid_signup_test_data', self.valid_signup_test_data)
        assert status == "ok"

    def test_sign_up_invalid_repeat_pass(self):
        #  Preparing test data
        self.valid_signup_test_data["repeatPassword"] = 0

        # Proceeds Sign Up POST request
        status = Auth.signup(session=self.session, basic_api_url=self.url, data=self.valid_signup_test_data)
        assert status != "ok"

    def teardown_method(self):
        Users.delete_user(session=self.session, basic_api_url=self.url, get_status=False)
