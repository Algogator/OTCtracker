from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
import time
import csv
import time
import uuid
import sqlite3
import os

def downloadfile():
    try:
        driver = webdriver.Chrome()
        driver.get("https://www.otcmarkets.com/research/stock-screener")
        en = driver.find_element_by_css_selector('#price > div > div.slider.slider-horizontal > div.slider-handle.max-slider-handle.round')
        vol = driver.find_element_by_css_selector('#vol > div.price-change-container.dropdown > input:nth-child(1)')
        move = ActionChains(driver)
        # print(width)
        move.click_and_hold(en).move_by_offset(-(195), 0).release().perform()
        # for i in range(990):
        en.send_keys(Keys.RIGHT)
        time.sleep(5)
        vol.send_keys("100000")
        time.sleep(5)
        download = driver.find_element_by_css_selector('#root > div > div.col-md-12.header-container > span.util-header > button').click()
        time.sleep(10)
    finally:
        driver.close()

def dfile():
    downloadfile()
    # conn = sqlite3.connect('otc.db')
    # cursor = conn.cursor()
    # count = 0
    # while not os.path.exists('/home/anna/Downloads/Stock_Screener.csv'):
    #     print "Not found"
    #     count += 1
    #     if count == 4:
    #         downloadfile()
    #     time.sleep(5)
    # with open('/home/anna/Downloads/Stock_Screener.csv', 'rb') as f:
    #     reader = csv.reader(f)
    #     for row in reader:
    #         # stocks.append(str(row[0]))
    #         print(row)
    #         ts = time.time()
    #         conn.execute("INSERT INTO STOCKS (ID,NAME,PRICE,OPEN,CLOSE,VOL)  VALUES ('"+str(uuid.uuid4())+"','"+row[0]+"', '"+row[3]+"', '0', '0', '"+row[5]+"')")
    # conn.commit()
    # conn.close()
    # os.remove('/home/anna/Downloads/Stock_Screener.csv')

while True:
    dfile()
    time.sleep(900)
