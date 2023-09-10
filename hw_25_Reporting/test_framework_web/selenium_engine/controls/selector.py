from selenium.webdriver.support.expected_conditions import (
    element_to_be_clickable as is_clickable,
)
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait


class Selector:
    def __init__(self, selector_element):
        self.element = selector_element

    def select_by_visible_text(self, visible_text: str):
        Select(self.element).select_by_visible_text(visible_text)

    def wait_for_clickable(self, timeout: int = 10):
        (
            WebDriverWait(self.element, timeout=timeout).until(
                method=is_clickable(self.element)
            )
        )
