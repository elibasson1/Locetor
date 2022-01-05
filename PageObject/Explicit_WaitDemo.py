from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ExplicitWaitdemo:

    def __init__(self, driver):
        self.driver = driver

    def load_page(self):
        self.driver.maximize_window()
        self.driver.get("https://rahulshettyacademy.com/seleniumPractise/")

    searchVegetables = (By.CSS_SELECTOR, "input[type='search']")

    def search_Vegetables(self):
        return self.driver.find_element(*ExplicitWaitdemo.searchVegetables)

    products = (By.CSS_SELECTOR, "div[class='product']")

    def get_products(self):
        return self.driver.find_elements(*ExplicitWaitdemo.products)

    ADD_TO_CART_Button = (By.XPATH, "//div[@class='product-action']/button")

    def Click_TO_CART_Button(self):
        return self.driver.find_elements(*ExplicitWaitdemo.ADD_TO_CART_Button)

    clickimage = (By.CSS_SELECTOR, "img[alt='Cart']")

    def click_image(self):
        return self.driver.find_element(*ExplicitWaitdemo.clickimage)

    PROCEED = (By.XPATH, "// button[text() = 'PROCEED TO CHECKOUT']")

    def Click_CHECKOUT (self):
        return self.driver.find_element(*ExplicitWaitdemo.PROCEED)

    promocode = (By.CSS_SELECTOR, "input[class='promoCode']")

    def enter_promocode(self):
        return self.driver.find_element(*ExplicitWaitdemo.promocode)

    promoBtn = (By.CSS_SELECTOR, "button[class='promoBtn']")

    def promo_Btn(self):
        return self.driver.find_element(*ExplicitWaitdemo.promoBtn)

    promoInfo = (By.CSS_SELECTOR, "span[class='promoInfo']")

    def get_promoInfo(self):
        return self.driver.find_element(*ExplicitWaitdemo.promoInfo)

    def wait_promoInfo(self):
        x = WebDriverWait(self.driver, 10)
        return x.until(EC.presence_of_element_located(ExplicitWaitdemo.promoInfo))

    def wait_promocode(self):
        x = WebDriverWait(self.driver, 5)
        return x.until(EC.presence_of_element_located(ExplicitWaitdemo.promocode))

    product_name = (By.CSS_SELECTOR, "h4[class='product-name']")

    def get_product_name(self):
        return self.driver.find_elements(*ExplicitWaitdemo.product_name)

    ProductSName = (By.CSS_SELECTOR,"p[class='product-name']")

    def get_ProductSName(self):
        return self.driver.find_elements(*ExplicitWaitdemo.ProductSName)

    discountAmt = (By.CSS_SELECTOR, "span[class='discountAmt']")

    def get_discountAmt(self):
        return self.driver.find_element(*ExplicitWaitdemo.discountAmt)

    TotalPrice = (By.XPATH, "//tr/td[5]/p")

    def get_TotalPrice(self):
        return self.driver.find_elements(*ExplicitWaitdemo.TotalPrice)

    totAmount = (By.CSS_SELECTOR, "span[class='totAmt']")

    def get_totAmount(self):
        return self.driver.find_element(*ExplicitWaitdemo.totAmount)
