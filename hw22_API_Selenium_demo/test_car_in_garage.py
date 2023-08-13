import pytest
from selenium import webdriver
from Hillel_AQA_homeworks.hw21_Pytest_API.ApiTestBaseFolder.ApiTestBase import (
    ApiTestBaseClass,
    Auth,
    CustomApiCalls,
)
from Selenuim.ui_tests_base import LoginForm, GarageAddNewCar, GarageMain


class TestCarInGarage(ApiTestBaseClass):
    def setup_method(self):
        CustomApiCalls.delete_registered_user_via_api(
            session=self.session,
            url=self.url,
            valid_signin_data=self.valid_signin_data,
        )
        self.driver = webdriver.Chrome()

    def test_car_present_in_garage(self):
        driver = self.driver
        # Step 1
        request = Auth.signup(
            session=self.session,
            basic_api_url=self.url,
            data=self.valid_signup_data,
        )
        if request["status"] != "ok":
            raise Exception(
                "Step 1: User SignUp Error, Error message %s", request["message"]
            )

        LoginForm(driver=driver).fill_sign_in_form(
            email=ApiTestBaseClass.valid_signin_data["email"],
            password=ApiTestBaseClass.valid_signin_data["password"],
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
            valid_signin_data=self.valid_signin_data,
        )
