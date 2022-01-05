from selenium.webdriver.common.by import By


class Waitdemo:

    def __init__(self, driver):
        self.driver = driver

    def load_page(self):
        self.driver.maximize_window()
        self.driver.get("https://rahulshettyacademy.com/seleniumPractise/")

    searchVegetables = (By.CSS_SELECTOR, "input[type='search']")

    def search_Vegetables(self):
        return self.driver.find_element(*Waitdemo.searchVegetables)

    products = (By.CSS_SELECTOR, "div[class='product']")

    def get_products(self):
        return self.driver.find_elements(*Waitdemo.products)

    ADD_TO_CART_Button = (By.XPATH, "//div[@class='product-action']/button")

    def Click_TO_CART_Button(self):
        return self.driver.find_elements(*Waitdemo.ADD_TO_CART_Button)

    clickimage = (By.CSS_SELECTOR, "img[alt='Cart']")

    def click_image(self):
        return self.driver.find_element(*Waitdemo.clickimage)

    PROCEED = (By.XPATH, "// button[text() = 'PROCEED TO CHECKOUT']")

    def Click_CHECKOUT (self):
        return self.driver.find_element(*Waitdemo.PROCEED)

    promocode = (By.CSS_SELECTOR, "input[class='promoCode']")

    def enter_promocode(self):
        return self.driver.find_element(*Waitdemo.promocode)

    promoBtn = (By.CSS_SELECTOR, "button[class='promoBtn']")

    def promo_Btn(self):
        return self.driver.find_element(*Waitdemo.promoBtn)

    promoInfo = (By.CSS_SELECTOR, "span[class='promoInfo']")

    def get_promoInfo(self):
        return self.driver.find_element(*Waitdemo.promoInfo)

    # Global Wait
    def implicit_time(self):
        return self.driver.implicitly_wait(5)

    def close(self):
        self.driver.close()
        self.driver.quit()
