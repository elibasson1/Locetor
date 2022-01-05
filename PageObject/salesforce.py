from Utilties.Base import Base
from selenium.webdriver.common.by import By


class salesforce:

    def __init__(self, driver):
        self.driver = driver

    def load_page(self):
        self.driver.maximize_window()
        self.driver.get("https://login.salesforce.com/")

    Uname = (By.ID, "username")

    def get_user_name(self):
        return self.driver.find_element(*salesforce.Uname)

    Password = (By.ID, "password")

    def get_Password(self):
        return self.driver.find_element(*salesforce.Password)

    Forgot_Password = (By.LINK_TEXT, "Forgot Your Password?")

    def ForgotPassword(self):
        return self.driver.find_element(*salesforce.Forgot_Password)

    Cancel = (By.XPATH,"// a[text() = 'Cancel']")

    def Cancel_Button(self):
        return self.driver.find_element(*salesforce.Cancel)

    Username_Text = (By.XPATH, "//form[@name='login']/div[1]/label")

    def Uname_Text(self):
        return self.driver.find_element(*salesforce.Username_Text)

    Password_Text = (By.CSS_SELECTOR, "form[name='login'] label:nth-child(3)")

    def Pass_Text(self):
        return self.driver.find_element(*salesforce.Password_Text)


#  from parent to child by Xpath :    //div[@id='usernamegroup']/label
#  from parent to child by CSS: there is a Space:      div[id='usernamegroup'] label
#  from grand parent to grand chaild by xpath        : //form[@name='login']/div[1]/label
#  Password label by css : form[name='login'] label:nth-child(3)


