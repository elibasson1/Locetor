import pytest

from PageObject.salesforce import salesforce
from Utilties.Base import Base

@pytest.mark.sanity
class Test_salesforce(Base):

    def test_Test_sales(self):
        sal_salesforce = salesforce(self.driver)
        sal_salesforce.load_page()
        sal_salesforce.get_user_name().send_keys("eli")
        sal_salesforce.get_Password().send_keys("basson")
        sal_salesforce.ForgotPassword().click()
        sal_salesforce.Cancel_Button().click()
        print(sal_salesforce.Uname_Text().text)
        print(sal_salesforce.Pass_Text().text)

