# coding:utf-8
from selenium import webdriver
import os
import time

browser = webdriver.Chrome()
browser.get('file:///'+os.path.abspath('frame.html'))

browser.implicitly_wait(30)
#找到ifrome1
browser.switch_to_frame('f1')
browser.switch_to_frame('f2')

browser.find_element_by_id('kw').send_keys(u'哈哈')
browser.find_element_by_id('kw').submit()
print '百度哈哈'
time.sleep(10)

browser.quit()
