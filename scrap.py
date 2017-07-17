#!/bin/bash
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from multiprocessing import Queue, Process
import concurrent.futures

from selenium.webdriver.common.by import By
import sqlite3
import time
import csv

driver = webdriver.Chrome()

def getPrices(name):
    url = 'https://www.otcmarkets.com/stock/'+name+'/quote'
    try:
        driver.get(url)
    except Exception as e:
        print(e)
        driver = webdriver.Chrome()
        driver.get(url)
    # driver.refresh()
    try:
        price = driver.find_element_by_class_name('price')
        misc = driver.find_elements_by_css_selector('span.value')
        close = float(misc[0].text)
        try:
            open = float(misc[1].text)
        except ValueError:
            print "Error"
            open = 0
        vol = int(misc[4].text.replace(',',''))
        price = price.text
        price = float(price)
        ts = time.time()

        conn.execute("INSERT INTO COMPANY (ID,NAME,PRICE,OPEN,CLOSE,VOL) VALUES ("+str(ts)+",'"+ name +"'," + str(price) +","+ str(open) +"," + str(close) +"," + str(vol) +" )")
        conn.commit()
        # print "Records created successfully", name
    except Exception:
        print "Can't get an element"


stocks = []
with open('/home/anna/Downloads/Stock_Screener.csv', 'rb') as f:
    reader = csv.reader(f)
    for row in reader:
        if row[0] == 'Symbol':
            continue
        stocks.append(row[0])
        # print(stocks)
print(len(stocks))


while True:
    conn = sqlite3.connect('otc.db')
    start_time = time.time()
    for i in stocks:
        getPrices(i)
    conn.close()
    print("--- %s seconds ---" % (time.time() - start_time))

    # myElem = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, 'price')))


# button = driver.find_element_by_id('periodBtn')
# for i in misc:
#     print(i.text)
# print "Price: ",price
# print "Close: ",close
# print "Open: ",open
# print "Volume: ",vol
