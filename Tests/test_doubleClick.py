from selenium import webdriver
from selenium.webdriver import ChromeOptions, ActionChains


def test_doubleClick():
    driver_path = "D:\\working\\Documents\\Pyhon-1\\Old\\Chromedrive\\"
    opts = ChromeOptions()
    opts.add_experimental_option("detach", True)
    opts.add_experimental_option("excludeSwitches", ['enable-logging'])
    driver = webdriver.Chrome(driver_path + "chromedriver", options=opts)

    driver.maximize_window()
    driver.get("https://chercher.tech/practice/practice-pop-ups-selenium-webdriver")

    action = ActionChains(driver)
    action.double_click(driver.find_element_by_id("double-click")).perform()
    alert = driver.switch_to.alert
    assert alert.text == "You double clicked me!!!, You got to be kidding me"
    alert.accept()
    driver.close()
    driver.quit()