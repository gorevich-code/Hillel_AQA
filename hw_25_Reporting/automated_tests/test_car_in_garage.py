from ..test_framework_web.api_engine import Auth, ApiTestBaseClass, CustomApiCalls
from ..test_framework_web.selenium_engine.driver import Driver
from ..test_framework_web.selenium_engine.pages import GarageMain, GarageAddNewCar, LoginForm, SeleniumBasic
from ..test_framework_web.test_data import TestDataProcessor
import allure


class TestCarInGarage(ApiTestBaseClass):
    def setup_method(self):
        self.valid_signup_data = TestDataProcessor().get_sign_up_data(test_data_src=self.data_source)
        self.valid_signin_data = TestDataProcessor().get_sign_in_data(test_data_src=self.data_source)
        CustomApiCalls.delete_registered_user_via_api(
            session=self.session,
            url=self.url,
            valid_signin_data=self.valid_signin_data.__dict__,
        )
        self.driver = Driver().driver

    def test_car_present_in_garage(self):
        driver = self.driver
        with allure.step("Proceed sign UP new test user"):
            request = Auth.signup(
                session=self.session,
                basic_api_url=self.url,
                data=self.valid_signup_data.__dict__,
            )
            if request["status"] != "ok":
                raise Exception(
                    "Step 1: User SignUp Error, Error message %s", request["message"]
                )
        SeleniumBasic(driver=self.driver).navigate_via_link(
            http_address="https://guest:welcome2qauto@qauto2.forstudy.space/"
        )
        LoginForm(driver=driver).call_and_fill_sign_in_form(
            email=self.valid_signup_data.email,
            password=self.valid_signup_data.password,
        )
        GarageAddNewCar(driver=driver).add_new_car_to_garage(
            brand="BMW", model="X5", mileage="1000"
        )
        assert GarageMain(self.driver).check_one_car_is_in_garage(
            brand="BMW", model="X5", mileage="1000"
        )

    def teardown_method(self):
        self.driver.quit()
        CustomApiCalls.delete_registered_user_via_api(
            session=self.session,
            url=self.url,
            valid_signin_data=self.valid_signin_data.__dict__,
        )
