from PageObject.AutomationPractice import AutomationPractice
from Utilties.Base import Base


class Test_Automation_Practice(Base):

    def test_Automation_Practice(self):
        auto = AutomationPractice(self.driver)
        auto.load_page()
        checkboxes = auto.All_check_box()
        print(len(checkboxes))

        for checkbox in checkboxes:
            if checkbox.get_attribute("value") == "option2":
                checkbox.click()
                assert checkbox.is_selected()

        radioButton = auto.radio_Button()
        for radio in radioButton:
            if radio.get_attribute("value") == "radio2":
                radio.click()
                assert radio.is_selected()


