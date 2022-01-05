from selenium.webdriver.common.by import By


class AutoDropdownTrip:

    def __init__(self, driver):
        self.driver = driver

    def load_page(self):
        self.driver.maximize_window()
        self.driver.get("https://www.makemytrip.com/")

    SelectCuntry = (By.CSS_SELECTOR, "input[data-cy='fromCity']")

    def Select_Cuntry(self):
        return self.driver.find_element(*AutoDropdownTrip.SelectCuntry)

    click_Item = (By.CSS_SELECTOR, "input[placeholder='From']")

    def Select_Item(self):
        return self.driver.find_element(*AutoDropdownTrip.click_Item)

    SelectCity= (By.CSS_SELECTOR, "p[class*='blackText']")

    def Select_City(self):
        return self.driver.find_elements(*AutoDropdownTrip.SelectCity)

    tocity = (By.XPATH, "//p[text()='Delhi, India']")

    def to_City(self):
        return self.driver.find_element(*AutoDropdownTrip.tocity)




