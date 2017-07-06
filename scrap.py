#!/bin/bash
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
import sqlite3
import time

driver = webdriver.Firefox()
url = 'https://www.otcmarkets.com/stock/FNMA/quote'
driver.get(url)
stocks = []

while True:
    # myElem = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, 'price')))
    driver.refresh()
    price = driver.find_element_by_class_name('price')
    misc = driver.find_elements_by_css_selector('span.value')
    close = float(misc[0].text)
    open = float(misc[1].text)
    vol = int(misc[4].text.replace(',',''))
    price = price.text
    price = float(price)
    ts = time.time()
    conn = sqlite3.connect('otc.db')
    conn.execute("INSERT INTO COMPANY (ID,NAME,PRICE,OPEN,CLOSE,VOL) VALUES ("+str(ts)+", 'FNMA'," + str(price) +","+ str(open) +"," + str(close) +"," + str(vol) +" )")
    conn.commit()
    print "Records created successfully";
    conn.close()
    time.sleep(900) #900
# button = driver.find_element_by_id('periodBtn')
# for i in misc:
#     print(i.text)
# print "Price: ",price
# print "Close: ",close
# print "Open: ",open
# print "Volume: ",vol
