import selenium
from selenium.webdriver.support.expected_conditions import (
    element_to_be_clickable as is_clicable,
)
from selenium.webdriver.support.wait import WebDriverWait


class SeleniumBasic:
    def __init__(self, driver):
        self.driver = driver

    def wait_for_element(self, web_element: selenium, timeout: int = 10):
        (
            WebDriverWait(self.driver, timeout=timeout).until(
                method=is_clicable((web_element()))
            )
        )

    def navigate_via_link(self, http_address: str):
        self.driver.get(url="https://guest:welcome2qauto@qauto2.forstudy.space/")
