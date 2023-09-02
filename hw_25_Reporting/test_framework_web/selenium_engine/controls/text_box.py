from selenium.webdriver.support.expected_conditions import (
    element_to_be_clickable as is_clickable,
)
from selenium.webdriver.support.wait import WebDriverWait


class TextBox:
    def __init__(self, text_box):
        self.element = text_box

    def click(self):
        self.element.click()

    def send_keys(self, keys_to_send):
        self.element.send_keys(keys_to_send)

    def wait_for_clickable(self, timeout: int = 10):
        (
            WebDriverWait(self.element, timeout=timeout).until(
                method=is_clickable(self.element)
            )
        )
