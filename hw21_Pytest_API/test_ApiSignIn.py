from ApiTestBase.ApiTestBase import Auth, Users, ApiTestBaseClass


class TestSignIn(ApiTestBaseClass):
    """Test class which contain SignIN tests with using API"""

    def setup_method(self):
        """Method Prepare registered test user
         Resets sign IN data to valid for each test
         """
        Auth.signup(session=self.session, basic_api_url=self.url, data=self.valid_signup_data)
        self.signin_data = self.valid_signin_data

    def test_sign_in_valid_data(self):
        """Test: Try to Sign IN with valid data and assert success status"""
        status = Auth.signin(session=self.session, basic_api_url=self.url, data=self.signin_data)
        assert status == "ok"

    def test_sign_in_invalid_repeat_pass(self):
        """Test: Try to Sign IN with invalid data (invalid repeat password) and assert success status"""
        #  Preparing invalid test data
        self.signin_data["password"] = 0

        # Proceeds Sign Up POST request
        status = Auth.signin(session=self.session, basic_api_url=self.url, data=self.signin_data)
        assert status != "ok"

    def teardown_method(self):
        """Method which delete test user account"""
        if Users.current(session=self.session, basic_api_url=self.url) == 'ok':
            # Auth.logout(session=self.session, basic_api_url=self.url, get_status=False)
            Users.delete_user(session=self.session, basic_api_url=self.url, get_status=False)