from ApiTestBase.ApiTestBase import Auth, Users, ApiTestBaseClass
import requests


class TestSignIn(ApiTestBaseClass):

    def setup_method(self):
        # Prepare registered test user
        Auth.signup(session=self.session, basic_api_url=self.url, data=self.valid_signup_data)
        # Reset sign IN data to valid for each test
        self.signin_data = self.valid_signin_data

    def test_sign_in_valid_data(self):
        status = Auth.signin(session=self.session, basic_api_url=self.url, data=self.signin_data)
        assert status == "ok"

    def test_sign_in_invalid_repeat_pass(self):
        #  Preparing invalid test data
        self.signin_data["password"] = 0

        # Proceeds Sign Up POST request
        status = Auth.signin(session=self.session, basic_api_url=self.url, data=self.signin_data)
        assert status != "ok"

    def teardown_method(self):
        # Delete test user
        if Users.current(session=self.session, basic_api_url=self.url) == 'ok':
            # Auth.logout(session=self.session, basic_api_url=self.url, get_status=False)
            Users.delete_user(session=self.session, basic_api_url=self.url, get_status=False)