from ApiTestBase.ApiTestBase import Auth, Users, ApiTestBaseClass


class TestSignUp(ApiTestBaseClass):
    """Test class which contain SignUP tests with using API"""

    def setup_method(self):
        """Method Prepare NOT registered test user
        Try to sign IN and delete test account if test user is registered

        """
        if Auth.signin(session=self.session, basic_api_url=self.url, data=self.valid_signin_data) == "ok":
            Users.delete_user(session=self.session, basic_api_url=self.url, get_status=False)
        self.valid_signup_test_data = self.valid_signup_data

    def test_sign_up_valid_data(self):
        """Test: Try to Sign UP with valid data and assert success status"""

        status = Auth.signup(session=self.session, basic_api_url=self.url, data=self.valid_signup_test_data)
        print('valid_signup_test_data', self.valid_signup_test_data)
        assert status == "ok"

    def test_sign_up_invalid_repeat_pass(self):
        """Test: Try to Sign UP with invalid data and assert success status"""

        #  Preparing test data
        self.valid_signup_test_data["repeatPassword"] = 0

        # Proceeds Sign Up POST request
        status = Auth.signup(session=self.session, basic_api_url=self.url, data=self.valid_signup_test_data)
        assert status != "ok"

    def teardown_method(self):
        """Method delete test user after each case"""

        Users.delete_user(session=self.session, basic_api_url=self.url, get_status=False)
