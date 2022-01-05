from PageObject.Locetors import HomePage
from PageObject.ShopPage import ShopPage
from TestData.Locetors_Data import Locetors_Data
from Utilties.Base import Base
import pytest


@pytest.mark.sanity
class TestP(Base):

    def test_formSubmission(self, getData_formSubmission):
        home = HomePage(self.driver)
        home.load_page()
        home.get_name().send_keys(getData_formSubmission["Firstname"])
        home.get_mail().send_keys(getData_formSubmission["Lastname"])
        home.click_check_box().click()
        home.submit().click()
        msg = home.message_success().text
        assert "Success" in msg
        home.select_from_dropdown().select_by_index(1)

    def test_shop(self, getData_shop):
        shop = ShopPage(self.driver)
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

    @pytest.fixture(params=Locetors_Data.test_locetors_data)
    def getData_formSubmission(self, request):
        return request.param

    @pytest.fixture(params=["ind"])
    def getData_shop(self, request):
        return request.param
