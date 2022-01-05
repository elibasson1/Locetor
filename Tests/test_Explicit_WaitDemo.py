import time
from PageObject.Explicit_WaitDemo import ExplicitWaitdemo
from Utilties.Base import Base


class Test_waitdemo2(Base):

    def test_wait(self):
        wait = ExplicitWaitdemo(self.driver)
        wait.load_page()
        wait.search_Vegetables().send_keys("ber")
        products = wait.get_products()
        print(len(products))

        time.sleep(2)
        products_name = wait.get_product_name()
        product_list_1 = []
        for product in products_name:
            product_list_1.append(product.text)

        buttons = wait.Click_TO_CART_Button()
        for button in buttons:
            button.click()

        wait.click_image().click()
        wait.Click_CHECKOUT().click()

        product_list_2 = []
        Product_Name2 = wait.get_ProductSName()
        for product2 in Product_Name2:
            product_list_2.append(product2.text)

        while("" in product_list_2):
            product_list_2.remove("")

        assert product_list_1 == product_list_2

        wait.wait_promocode()
        orginalApplay = wait.get_discountAmt().text
        wait.enter_promocode().send_keys("rahulshettyacademy")

        wait.promo_Btn().click()

        wait.wait_promoInfo()
        print(wait.get_promoInfo().text)
        discountAmt = wait.get_discountAmt().text
        assert float(discountAmt) < int(orginalApplay)

        amounts = wait.get_TotalPrice()

        sum = 0
        for amount in amounts:
            sum = sum + int(amount.text)
        print(sum)

        totalAmount = int(wait.get_totAmount().text)

        assert sum == totalAmount
