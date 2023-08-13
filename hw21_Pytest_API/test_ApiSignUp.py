from ApiTestBaseFolder.ApiTestBase import Auth, Users, ApiTestBaseClass, CustomApiCalls


class TestSignUp(ApiTestBaseClass):
    """Test class which contain SignUP tests with using API"""

    def setup_class(self):
        """Method Prepare NOT registered test user
        Try to sign IN and delete test account if test user is registered

        """

        CustomApiCalls.delete_registered_user_via_api(
            session=self.session, url=self.url, valid_signin_data=self.valid_signin_data
        )

    def setup_method(self):
        """Method reset sign UP credentials to default"""

        self.valid_signup_test_data = self.valid_signup_data

    def test_sign_up_valid_data(self):
        """Test: Try to Sign UP with valid data and assert success status"""

        request = Auth.signup(
            session=self.session,
            basic_api_url=self.url,
            data=self.valid_signup_test_data,
        )
        assert request["status"] == "ok", request["message"]

    def test_sign_up_invalid_repeat_pass(self):
        """Test: Try to Sign UP with invalid data and assert success status"""

        #  Preparing test data
        self.valid_signup_test_data["repeatPassword"] = 0

        # Proceeds Sign Up POST request
        request = Auth.signup(
            session=self.session,
            basic_api_url=self.url,
            data=self.valid_signup_test_data,
        )
        assert request["status"] != "ok", request["message"]

    def teardown_method(self):
        """Method delete test user after each case"""

        Auth.signin(
            session=self.session,
            basic_api_url=self.url,
            data=self.valid_signup_test_data,
        )
        Users.delete_user(session=self.session, basic_api_url=self.url)
