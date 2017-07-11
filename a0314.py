# coding:utf-8
from selenium import webdriver
import time
import os

browser = webdriver.Chrome()
browser.get('file:///'+os.path.abspath('drop_down.html'))
a=browser.find_element_by_name('ShippingMethod')
time.sleep(5)

a.find_element_by_xpath("//option[@value='9.03']").click()

time.sleep(10)
browser.quit()

