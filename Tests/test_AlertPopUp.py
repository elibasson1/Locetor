from PageObject.AlertPopUp import alert
from Utilties.Base import Base


class TestAlertsPopUp(Base):

    def test_alert(self):
        ValidateAletTest = "eli"
        callalert = alert(self.driver)
        callalert.load_page()
        callalert.my_name().send_keys(ValidateAletTest)
        callalert.Alert_button().click()
        myalet = callalert.Switch_Alert()
        assert ValidateAletTest in myalet.text
        myalet.accept()



