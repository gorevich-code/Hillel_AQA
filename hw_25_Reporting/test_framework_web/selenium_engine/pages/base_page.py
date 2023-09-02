import selenium
from selenium.webdriver.support.expected_conditions import (
    element_to_be_clickable as is_clicable,
)
from selenium.webdriver.support.wait import WebDriverWait

import allure
from allure_commons.types import AttachmentType


class SeleniumBasic:
    def __init__(self, driver):
        self.driver = driver

    def wait_for_element(self, web_element: selenium, timeout: int = 10):
        (
            WebDriverWait(self.driver, timeout=timeout).until(
                method=is_clicable((web_element()))
            )
        )

    @allure.step('Proceed to web page via http address')
    def navigate_via_link(self, http_address: str):
        self.driver.get(url="https://guest:welcome2qauto@qauto2.forstudy.space/")
        allure.attach(self.driver.get_screenshot_as_png(), name='Opened web page', attachment_type=AttachmentType.PNG)
