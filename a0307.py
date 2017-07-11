#-*-coding:utf-8 -*-
from selenium import webdriver
#from selenium.webdriver.common.keys import Keys #引入keys包
from selenium.webdriver.common.keys import Keys
import time


driver = webdriver.Chrome()
driver.get('https://www.google.com/')
time.sleep(3)
driver.maximize_window()
driver.find_element_by_id('lst-ib').send_keys(Keys.TAB)
print(u'成功执行TAB')
time.sleep(3)

driver.find_element_by_id('lst-ib').clear()
time.sleep(3)
print(u'成功清除')
driver.find_element_by_id('lst-ib').send_keys(Keys.SHIFT,'V')
print(u'成功输入大写V')

driver.find_element_by_name('btnK').submit()
print(u'提交submit成功')
time.sleep(30)
driver.quit()
