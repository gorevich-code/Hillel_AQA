import selenium
from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import (
    element_to_be_clickable as is_clicable,
)
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait


class SeleniumBasic:
    def __init__(self, driver):
        self.driver = driver
        self.driver.implicitly_wait(time_to_wait=10)

    def wait_for_element(self, web_element: selenium, timeout: int = 10):
        (
            WebDriverWait(self.driver, timeout=timeout).until(
                method=is_clicable((web_element()))
            )
        )


class Header:
    def __init__(self, driver):
        self.driver = driver
        self.Header_xpath_dictionary = {
            "signin_button_xpath": ".//header//button[text()='Sign In']",
            "my_profile_button_xpath": ".//header//button[text()=' My profile ']",
        }

        self.signin_button = lambda: self.driver.find_element(
            By.XPATH, self.Header_xpath_dictionary["signin_button_xpath"]
        )
        self.my_profile_button = lambda: self.driver.find_element(
            By.XPATH, self.Header_xpath_dictionary["my_profile_button_xpath"]
        )


class LoginForm:
    def __init__(self, driver):
        self.driver = driver
        self.LoginForm_xpath_dictionary = {
            "email_input_xpath": ".//div[@class='modal-body']/app-signin-form/form//input[@name='email']",
            "password_input_xpath": ".//div[@class='modal-content']//div[@class='modal-body']/app-signin-form/form//input[@name='password']",
            "login_btn_xpath": ".//div[contains(@class,'modal-footer')]/button[text()='Login']",
        }
        self.driver = driver
        self.email_input_field = lambda: self.driver.find_element(
            By.XPATH, self.LoginForm_xpath_dictionary["email_input_xpath"]
        )
        self.password_input_field = lambda: self.driver.find_element(
            By.XPATH, self.LoginForm_xpath_dictionary["password_input_xpath"]
        )
        self.login_accept_button = lambda: self.driver.find_element(
            By.XPATH, self.LoginForm_xpath_dictionary["login_btn_xpath"]
        )

    def fill_sign_in_form(
        self, email: str, password: str, click_login_btn: bool = True
    ):
        self.driver.get(url="https://guest:welcome2qauto@qauto2.forstudy.space/")
        Header(self.driver).signin_button().click()
        SeleniumBasic(self.driver).wait_for_element(web_element=self.email_input_field)
        LoginForm(self.driver).email_input_field().send_keys(email)
        LoginForm(self.driver).password_input_field().send_keys(password)
        if click_login_btn:
            LoginForm(self.driver).login_accept_button().click()
            SeleniumBasic(self.driver).wait_for_element(
                web_element=Header(self.driver).my_profile_button
            )


class GarageMain:
    def __init__(self, driver):
        self.driver = driver
        self.Garage_main_page_xpath_dictionary = {
            "Garage_h1_label_xpath": ".//div[contains(@class, 'panel-page')]/h1[text()= 'Garage']",
            "Add_car_button_initial_xpath": ".//div[contains(@class, 'panel-layout')]//div[contains(@class, 'panel-page')]/button[text()='Add car']",
            "Car_list_web_element_xpath": ".//div[contains(@class, 'panel-page_cars')]/ul[contains(@class, 'car-list')]",
            "Car_item_of_list_web_element_xpath": ".//ul[contains(@class, 'car-list')]//div[contains(@class, 'jumbotron')]",
            "car_brand_space_model_label_xpath": ".//div[contains(@class, 'car-group')]/p[contains(@class, 'car_name')]",
            "update_mileage_input_xpath": ".//div[contains(@class, 'car-body')]//input[contains(@class, 'update-mileage-form_input')]",
        }
        self.add_car_button_initial = lambda: (
            self.driver.find_element(
                By.XPATH,
                self.Garage_main_page_xpath_dictionary["Add_car_button_initial_xpath"],
            )
        )
        self.common_car_item = lambda: (
            self.driver.find_element(
                By.XPATH,
                self.Garage_main_page_xpath_dictionary[
                    "Car_item_of_list_web_element_xpath"
                ],
            )
        )
        self.car_brand_space_model_itemS = lambda: (
            self.driver.find_element(
                By.XPATH,
                self.Garage_main_page_xpath_dictionary[
                    "car_brand_space_model_label_xpath"
                ],
            )
        )
        self.update_mileage_input = lambda: (
            self.driver.find_element(
                By.XPATH,
                self.Garage_main_page_xpath_dictionary["update_mileage_input_xpath"],
            )
        )

    def check_one_car_is_in_garage(self, brand: str, model: str, mileage: str):
        actual_brand, actual_model = (
            GarageMain(self.driver)
            .car_brand_space_model_itemS()
            .get_attribute("innerHTML")
            .split(" ")
        )
        actual_mileage = (
            GarageMain(self.driver).update_mileage_input().get_attribute("value")
        )
        return (
            True
            if (
                actual_mileage == brand,
                actual_model == model,
                actual_mileage == mileage,
            )
            else False
        )


class GarageAddNewCar:
    def __init__(self, driver):
        self.driver = driver
        self.Garage_xpath_addcar_dictionary = {
            "Add_a_car_form_xpath": ".//div[contains(@class, 'modal-content')]//app-add-car-modal",
            "brand_car_selector_xpath": ".//div[contains(@class, 'modal-content')]//app-add-car-modal//select[@id = 'addCarBrand']",
            "model_car_selector_xpath": ".//div[contains(@class, 'modal-content')]//app-add-car-modal//select[@id = 'addCarModel']",
            "mileage_car_text_field_xpath": ".//div[contains(@class, 'modal-content')]//app-add-car-modal//input[@id = 'addCarMileage']",
            "add_car_submit_form_xpath": ".//div[contains(@class, 'modal-footer')]/button[text()='Add']",
        }
        self.add_car_popup_form = lambda: (
            self.driver.find_element(
                By.XPATH, self.Garage_xpath_addcar_dictionary["Add_a_car_form_xpath"]
            )
        )
        self.brand_car_selector = lambda: (
            self.driver.find_element(
                By.XPATH,
                self.Garage_xpath_addcar_dictionary["brand_car_selector_xpath"],
            )
        )
        self.model_car_selector = lambda: (
            self.driver.find_element(
                By.XPATH,
                self.Garage_xpath_addcar_dictionary["model_car_selector_xpath"],
            )
        )
        self.mileage_text_field = lambda: (
            self.driver.find_element(
                By.XPATH,
                self.Garage_xpath_addcar_dictionary["mileage_car_text_field_xpath"],
            )
        )
        self.add_car_submit_btn = lambda: (
            self.driver.find_element(
                By.XPATH,
                self.Garage_xpath_addcar_dictionary["add_car_submit_form_xpath"],
            )
        )

    def add_new_car_to_garage(
        self,
        brand: str,
        model: str,
        mileage: str,
        click_add_car_to_submit_form: bool = True,
    ):
        GarageMain(self.driver).add_car_button_initial().click()
        SeleniumBasic(self.driver).wait_for_element(
            web_element=GarageAddNewCar(self.driver).add_car_popup_form
        )

        Select(self.brand_car_selector()).select_by_visible_text(brand)
        Select(self.model_car_selector()).select_by_visible_text(model)
        self.mileage_text_field().send_keys(mileage)
        if click_add_car_to_submit_form:
            self.add_car_submit_btn().click()
