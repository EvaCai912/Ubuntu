#coding:utf-8

from selenium import webdriver
import os
import time

browser = webdriver.Chrome()
browser.get('file:///'+os.path.abspath('modal.html'))

browser.find_element_by_id('show_modal').click()
c=browser.find_element_by_id('myModal').find_element_by_id('click')
browser.execute_script('$(arguments[0]).click()',c)
print '成功点击link'
time.sleep(10)
browser.quit()
