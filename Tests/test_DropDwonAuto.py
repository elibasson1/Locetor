import time

from PageObject.AutoDropDown import AutoDropdown
from Utilties.Base import Base


class Test_DropdownAuto(Base):

    def test_Auto_Drop_down(self):
        drop = AutoDropdown(self.driver)
        drop.load_page()
        drop.Select_Cuntry().send_keys("ind")
        time.sleep(2)
        cities = drop.Select_Item()
        print(len(cities))

        for city in cities:
            if city.text == "India":
                city.click()
                break

        assert drop.Select_Cuntry().get_attribute('value') == "India"






