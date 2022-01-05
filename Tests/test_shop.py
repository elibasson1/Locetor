import time
import pytest

from PageObject.ShopPage import ShopPage
from Tests.conftest import setup
from Utilties.Base import Base


class Testshop(Base):

    def test_home(self):
        shop = ShopPage(self.driver)
        shop.load_page()
        shop.get_shoplink().click()
        shop.get_spesificproduct()
        shop.get_checkoutButton().click()
        shop.get_checkOutBu().click()
        shop.get_country().send_keys("ind")
        shop.wait_country()
        shop.get_selectedCuntry().click()
        shop.get_checkBox().click()
        shop.get_PurchaseButton().click()
        alert = shop.get_alert().text
        assert "Success" in alert
