import time

from PageObject.Makemytrip import AutoDropdownTrip
from Utilties.Base import Base


class Test_makemytripAll(Base):

    def test_Auto_Drop_down(self):
        drop = AutoDropdownTrip(self.driver)
        drop.load_page()
        time.sleep(2)
        drop.Select_Cuntry().click()

        drop.Select_Item().send_keys("del")
        time.sleep(5)

        cities = drop.Select_City()

        for city in cities:
            if city.text == "Del Rio, United States":
                city.click()
                break

        drop.to_City().click()
