from ApiTestBaseFolder.ApiTestBase import (
    Auth,
    Users,
    ApiTestBaseClass,
    TestDataProcessor,
)


class TestSignIn(ApiTestBaseClass):
    """Test class which contain SignIN tests with using API"""

    def setup_class(self):
        """Method Prepare registered test user and clean test session"""
        # Prepare test data Processor
        (
            self.valid_signup_data,
            self.valid_signin_data,
        ) = TestDataProcessor.valid_test_data(self.data_source)
        Auth.signup(
            session=self.session, basic_api_url=self.url, data=self.valid_signup_data
        )
        Auth.logout(session=self.session, basic_api_url=self.url)

    def teardown_class(self):
        """Method delete test user account via API"""

        Auth.signin(
            session=self.session, basic_api_url=self.url, data=self.valid_signin_data
        )
        Users.delete_user(session=self.session, basic_api_url=self.url)

    def setup_method(self):
        """Method reset sign IN credentials to default"""

        self.signin_data = self.valid_signin_data

    def teardown_method(self):
        """Method delete log OUT test user account and clean test session after each test"""

        Auth.logout(session=self.session, basic_api_url=self.url)

    def test_sign_in_valid_data(self):
        """Test: Try to Sign IN with valid data and assert success status"""

        request = Auth.signin(
            session=self.session, basic_api_url=self.url, data=self.signin_data
        )
        assert request["status"] == "ok", request["message"]

    def test_sign_in_invalid_repeat_pass(self):
        """Test: Try to Sign IN with invalid data (invalid repeat password) and assert success status"""

        #  Preparing invalid test data
        self.signin_data["password"] = 0

        # Proceeds Sign Up POST request
        request = Auth.signin(
            session=self.session, basic_api_url=self.url, data=self.signin_data
        )
        assert request["status"] != "ok", request["message"]
