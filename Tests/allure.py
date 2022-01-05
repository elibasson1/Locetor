import allure
import pytest
from allure_commons.types import AttachmentType
from selenium import webdriver
from selenium.webdriver import ChromeOptions


@allure.severity(allure.severity_level.NORMAL)
class TestHRM:

    @allure.severity(allure.severity_level.MINOR)
    def test_Logo(self):
        driver_path = "D:\\working\\Documents\\Pyhon-1\\Old\\Chromedrive\\"
        opts = ChromeOptions()
        opts.add_experimental_option("detach", True)
        opts.add_experimental_option("excludeSwitches", ['enable-logging'])
        driver = webdriver.Chrome(driver_path + "chromedriver", options=opts)

        driver.maximize_window()
        driver.get("https://opensource-demo.orangehrmlive.com/")
        status = driver.find_element_by_css_selector("div[id='divLogo'] img").is_displayed()
        if status:
            assert True
        else:
            assert False
        driver.close()

    @allure.severity(allure.severity_level.NORMAL)
    def test_listemployees(self):
        pytest.skip("Skipping Test ..Later U will implement")

    @allure.severity(allure.severity_level.CRITICAL)
    def test_Login(self):
        driver_path = "D:\\working\\Documents\\Pyhon-1\\Old\\Chromedrive\\"
        opts = ChromeOptions()
        opts.add_experimental_option("detach", True)
        opts.add_experimental_option("excludeSwitches", ['enable-logging'])
        driver = webdriver.Chrome(driver_path + "chromedriver", options=opts)

        driver.maximize_window()
        driver.get("https://opensource-demo.orangehrmlive.com/")

        driver.find_element_by_id("txtUsername").send_keys("Admin")
        driver.find_element_by_id("txtPassword").send_keys("admin123")
        driver.find_element_by_id("btnLogin").click()
        act_title = driver.title

        if act_title == "OrangeHRM":
        # if act_title == "OrangeHRM123":
            driver.close()
            driver.quit()
        else:
            # allure.attach(driver.get_screenshot_as_png(), name="testLogin",
            #               attachment_type=AttachmentType.png)
            driver.close()
            driver.quit()
            assert False
