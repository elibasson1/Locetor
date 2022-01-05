from selenium import webdriver
from selenium.webdriver import ChromeOptions, ActionChains


def test_mouseover():
    driver_path = "D:\\working\\Documents\\Pyhon-1\\Old\\Chromedrive\\"
    opts = ChromeOptions()
    opts.add_experimental_option("detach", True)
    opts.add_experimental_option("excludeSwitches", ['enable-logging'])
    driver = webdriver.Chrome(driver_path + "chromedriver", options=opts)

    driver.maximize_window()
    driver.get("https://rahulshettyacademy.com/AutomationPractice/")

    action = ActionChains(driver)
    menu = driver.find_element_by_id("mousehover")
    action.move_to_element(menu).perform()
    chaildMenu = driver.find_element_by_link_text("Top")
    action.move_to_element(chaildMenu).click().perform()
    driver.close()
    driver.quit()


