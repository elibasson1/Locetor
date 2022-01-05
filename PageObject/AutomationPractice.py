from selenium.webdriver.common.by import By


class AutomationPractice:

    def __init__(self, driver):
        self.driver = driver

    def load_page(self):
        self.driver.maximize_window()
        self.driver.get("https://rahulshettyacademy.com/AutomationPractice/")

    all_check_box = (By.CSS_SELECTOR, "input[type='checkbox']")

    def All_check_box(self):
        return self.driver.find_elements(*AutomationPractice.all_check_box)

    radioButton = (By.CSS_SELECTOR, "input[name='radioButton']")

    def radio_Button(self):
        return self.driver.find_elements(*AutomationPractice.radioButton)

    def close(self):
        self.driver.close()
        self.driver.quit()