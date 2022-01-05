from selenium import webdriver
from selenium.webdriver import ChromeOptions
import pytest
driver = None


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome")


@pytest.fixture(scope="class")
def setup(request):
    global driver
    browser = request.config.getoption("--browser")
    if browser == "chrome":
        driver_path = "D:\\working\\Documents\\Pyhon-1\\Old\\Chromedrive\\"
        opts = ChromeOptions()
        opts.add_experimental_option("detach", True)
        # opts.headless = True
        opts.add_experimental_option("excludeSwitches", ['enable-logging'])
        driver = webdriver.Chrome(driver_path + "chromedriver", options=opts)
    elif browser == "firefox":
        driver_path = "D:\\working\\Documents\\Pyhon-1\\Old\\Chromedrive\\"
        driver = webdriver.Firefox(executable_path=driver_path + "geckodriver")

    request.cls.driver = driver
    yield
    driver.close()
    driver.quit()

