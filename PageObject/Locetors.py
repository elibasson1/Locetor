from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class HomePage:

    def __init__(self, driver):
        self.driver = driver

    def load_page(self):
        self.driver.maximize_window()
        self.driver.get("https://www.rahulshettyacademy.com/angularpractice/")

    name = (By.NAME, "name")

    def get_name(self):
        return self.driver.find_element(*HomePage.name)

    check_box = (By.ID, "exampleCheck1")

    def click_check_box(self):
        return self.driver.find_element(*HomePage.check_box)

    email = (By.CSS_SELECTOR, "input[name='email']")

    def get_mail(self):
        return self.driver.find_element(*HomePage.email)

    submit_button = (By.XPATH, "//input[@type='submit']")

    def submit(self):
        return self.driver.find_element(*HomePage.submit_button)

    Success_Message = (By.CSS_SELECTOR, "div[class*='alert-success']")

    def message_success(self):
        return self.driver.find_element(*HomePage.Success_Message)


# select class provide the method to handle the option in dropdown Tag name shouls be select
    dropdown = (By.ID, "exampleFormControlSelect1")

    def select_from_dropdown(self):
        return Select(self.driver.find_element(*HomePage.dropdown))

    def close(self):
        self.driver.close()
        self.driver.quit()


