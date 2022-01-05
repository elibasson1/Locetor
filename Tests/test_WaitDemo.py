import time

from PageObject.WaitDemo import Waitdemo
from Utilties.Base import Base


class Test_waitdemo(Base):

    def test_wait(self):
        wait = Waitdemo(self.driver)
        wait.load_page()
        wait.implicit_time()
        wait.search_Vegetables().send_keys("ber")
        products = wait.get_products()
        print(len(products))

        time.sleep(2)
        buttons = wait.Click_TO_CART_Button()

        for button in buttons:
            button.click()

        wait.click_image().click()
        wait.Click_CHECKOUT().click()

        wait.enter_promocode().send_keys("rahulshettyacademy")

        wait.promo_Btn().click()
        print(wait.get_promoInfo().text)
