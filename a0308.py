# coding:utf-8
from selenium import webdriver
import os,time

browser=webdriver.Chrome()
browser.get('file:///'+os.path.abspath('1.html'))
#inputs=browser.find_elements_by_tag_name('input')
#for input in inputs:
#	if input.get_attribute('type')=='radio':
#		input.click()

checkboxs=browser.find_elements_by_css_selector('input[type=checkbox]')
for checkbox in checkboxs:
	checkbox.click()
print '勾选所有checkbox'
time.sleep(2)

browser.find_elements_by_css_selector('input[type=checkbox]').pop().click()
print('取消勾选最后一个checkbox')
time.sleep(10)


browser.quit()
