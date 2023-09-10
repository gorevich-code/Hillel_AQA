from selenium.webdriver.support.expected_conditions import (
    element_to_be_clickable as is_clickable,
)
from selenium.webdriver.support.wait import WebDriverWait


class Button:
    def __init__(self, button_element):
        self.element = button_element

    def click(self):
        self.element.click()

    def is_enabled(self):
        self.element.is_enabled()

    def wait_for_clickable(self, timeout: int = 10):
        (
            WebDriverWait(self.element, timeout=timeout).until(
                method=is_clickable(self.element)
            )
        )
