from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class alert:

    def __init__(self, driver):
        self.driver = driver

    def load_page(self):
        self.driver.maximize_window()
        self.driver.get("https://rahulshettyacademy.com/AutomationPractice/")

    myname = (By.ID, "name")

    def my_name(self):
        return self.driver.find_element(*alert.myname)

    alertbutton = (By.ID, "alertbtn")

    def Alert_button(self):
        return self.driver.find_element(*alert.alertbutton)

    def Switch_Alert(self):
        return self.driver.switch_to_alert()

    def close(self):
        return self.driver.close()
        # self.driver.quit()

    def wait_alert(self):
        wait = WebDriverWait(self.driver, 7)
        return wait.until(EC.alert_is_present())

# DeprecationWarning: use driver.switch_to.alert instead