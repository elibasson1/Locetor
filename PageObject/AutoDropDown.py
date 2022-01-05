from selenium.webdriver.common.by import By


class AutoDropdown:

    def __init__(self, driver):
        self.driver = driver

    def load_page(self):
        self.driver.maximize_window()
        self.driver.get("https://rahulshettyacademy.com/dropdownsPractise/")

    SelectCuntry = (By.ID, "autosuggest")

    def Select_Cuntry(self):
        return self.driver.find_element(*AutoDropdown.SelectCuntry)

    SelectItem = (By.CSS_SELECTOR, "li[class='ui-menu-item'] a")

    def Select_Item(self):
        return self.driver.find_elements(*AutoDropdown.SelectItem)

    def close(self):
        self.driver.close()
        self.driver.quit()




