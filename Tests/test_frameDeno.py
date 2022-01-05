from selenium import webdriver
from selenium.webdriver import ChromeOptions


def test_framesDemo():
    driver_path = "D:\\working\\Documents\\Pyhon-1\\Old\\Chromedrive\\"
    opts = ChromeOptions()
    opts.add_experimental_option("detach", True)
    opts.add_experimental_option("excludeSwitches", ['enable-logging'])
    driver = webdriver.Chrome(driver_path + "chromedriver", options=opts)

    driver.maximize_window()
    driver.get("https://the-internet.herokuapp.com/iframe")
    driver.switch_to.frame("mce_0_ifr")  # frame id or frame name or frame index
    driver.find_element_by_xpath("//body[@id='tinymce']").clear()
    print("************")
    driver.find_element_by_xpath("//body[@id='tinymce']").send_keys("I am able to Automate")
    driver.switch_to.default_content()  # bring to normal HTML browser ( exit fro, frame)
    print(driver.find_element_by_tag_name("h3").text)
    driver.close()
    driver.quit()
