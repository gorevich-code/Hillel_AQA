from selenium.webdriver.common.by import By

from ...selenium_engine import pages
from ....test_framework_web.selenium_engine import controls

import allure
from allure_commons.types import AttachmentType


class LoginForm:
    def __init__(self, driver):
        self.driver = driver
        self.LoginForm_xpath_dictionary = {
            "email_input_xpath": ".//div[@class='modal-body']/app-signin-form/form//input[@name='email']",
            "password_input_xpath": ".//div[@class='modal-content']//div[@class='modal-body']/app-signin-form/form//input[@name='password']",
            "login_btn_xpath": ".//div[contains(@class,'modal-footer')]/button[text()='Login']",
        }
        self.driver = driver
        self.email_input_field = lambda: controls.TextBox(
            self.driver.find_element(
                By.XPATH, self.LoginForm_xpath_dictionary["email_input_xpath"]
            )
        )
        self.password_input_field = lambda: controls.TextBox(
            self.driver.find_element(
                By.XPATH, self.LoginForm_xpath_dictionary["password_input_xpath"]
            )
        )
        self.login_accept_button = lambda: controls.TextBox(
            self.driver.find_element(
                By.XPATH, self.LoginForm_xpath_dictionary["login_btn_xpath"]
            )
        )

    @allure.step('Call sign in form, fill it and submit if specified')
    def call_and_fill_sign_in_form(
        self, email: str, password: str, click_login_btn: bool = True
    ):
        pages.Header(self.driver).signin_button().wait_for_clickable()
        pages.Header(self.driver).signin_button().click()
        LoginForm(self.driver).email_input_field().wait_for_clickable()
        LoginForm(self.driver).email_input_field().send_keys(email)
        LoginForm(self.driver).password_input_field().send_keys(password)
        allure.attach(self.driver.get_screenshot_as_png(), name='Sign IN form', attachment_type=AttachmentType.PNG)
        if click_login_btn:
            LoginForm(self.driver).login_accept_button().click()
            pages.Header(self.driver).my_profile_button().wait_for_clickable()
