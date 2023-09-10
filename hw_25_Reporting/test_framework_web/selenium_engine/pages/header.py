from selenium.webdriver.common.by import By

from ..controls import Button


class Header:
    def __init__(self, driver):
        self.driver = driver
        self.Header_xpath_dictionary = {
            "signin_button_xpath": ".//header//button[text()='Sign In']",
            "my_profile_button_xpath": ".//header//button[text()=' My profile ']",
        }

        self.signin_button = lambda: Button(
            self.driver.find_element(
                By.XPATH, self.Header_xpath_dictionary["signin_button_xpath"]
            )
        )

        self.my_profile_button = lambda: Button(
            self.driver.find_element(
                By.XPATH, self.Header_xpath_dictionary["my_profile_button_xpath"]
            )
        )
