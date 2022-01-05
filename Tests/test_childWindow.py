from selenium import webdriver
from selenium.webdriver import ChromeOptions


def test_childWindow():
    driver_path = "D:\\working\\Documents\\Pyhon-1\\Old\\Chromedrive\\"
    opts = ChromeOptions()
    opts.add_experimental_option("detach", True)
    opts.add_experimental_option("excludeSwitches", ['enable-logging'])
    driver = webdriver.Chrome(driver_path + "chromedriver", options=opts)

    driver.maximize_window()
    driver.get("https://the-internet.herokuapp.com/windows")
    print("start test")
    driver.find_element_by_link_text("Click Here").click()
    # ("parentid = 0","childid = 1" , etc..)
    childidwindow = driver.window_handles[1]
    driver.switch_to.window(childidwindow)
    print(driver.find_element_by_tag_name("h3").text)
    driver.close()
    parentwindow = driver.window_handles[0]
    driver.switch_to.window(parentwindow)
    print(driver.find_element_by_tag_name("h3").text)
    driver.close()
    driver.quit()