from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
import time

try:
    driver = webdriver.Chrome()
    driver.get("https://www.otcmarkets.com/research/stock-screener")
    en = driver.find_element_by_css_selector('#price > div > div.slider.slider-horizontal > div.slider-handle.max-slider-handle.round')
    move = ActionChains(driver)
    print(width)
    move.click_and_hold(en).move_by_offset(-(195), 0).release().perform()
    # for i in range(990):
    en.send_keys(Keys.RIGHT)
    download = driver.find_element_by_css_selector('#root > div > div.col-md-12.header-container > span.util-header > button').click()
    time.sleep(10)

finally:
    driver.close()
