from itertools import product
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Utilties.Base import Base


class ShopPage:

    def __init__(self,driver):
        self.driver = driver

    def load_page(self):
        self.driver.maximize_window()
        self.driver.get("https://www.rahulshettyacademy.com/angularpractice/")

    shoplink = (By.LINK_TEXT, "Shop")

    def get_shoplink(self):
        return self.driver.find_element(*ShopPage.shoplink)

    products = (By.XPATH, "//div[@class='card h-100']")

    def get_products(self):
        products = self.driver.find_elements(*ShopPage.products)
        return products

    # products_name = //div[@class='card h-100']/div/h4/a
    #  Add button = //div[@class='card h-100']/div/button
    def get_spesificproduct(self):
        for product in self.get_products():
            productName = product.find_element_by_xpath("div/h4/a").text
            if productName == "Blackberry":
                product.find_element_by_xpath("div/button").click()

    checkoutButton = (By.CSS_SELECTOR, "a[class*='btn-primary']")

    def get_checkoutButton(self):
        return self.driver.find_element(*ShopPage.checkoutButton)

    checkOutBu = (By.CSS_SELECTOR, "button[class*='btn-success']")

    def get_checkOutBu(self):
        return self.driver.find_element(*ShopPage.checkOutBu)

    country = (By.ID, "country")

    def get_country(self):
        return self.driver.find_element(*ShopPage.country)

    selectedCuntry = (By.LINK_TEXT, "India")

    def get_selectedCuntry(self):
        return self.driver.find_element(*ShopPage.selectedCuntry)

    def wait_country(self):
        wait = WebDriverWait(self.driver, 7)
        return wait.until(EC.presence_of_element_located(ShopPage.selectedCuntry))

    checkBox = (By.XPATH, "//div[@class='checkbox checkbox-primary']")

    def get_checkBox(self):
        return self.driver.find_element(*ShopPage.checkBox)

    PurchaseButton = (By.CSS_SELECTOR, "input[class*='btn-success']")

    def get_PurchaseButton(self):
        return self.driver.find_element(*ShopPage.PurchaseButton)

    alert = (By.CSS_SELECTOR, "div[class*='alert-success']")

    def get_alert(self):
        return self.driver.find_element(*ShopPage.alert)
