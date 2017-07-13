# coding:utf-8
#谷歌设置

from selenium import webdriver
from time import sleep

browser = webdriver.Chrome()
browser.get('http://www.google.com')
#找到设置按钮，并点击
browser.find_element_by_xpath('//a[@id="fsettl"]').click()
sleep(3)
browser.find_element_by_xpath('//span[@id="fsett"]/a[1]').click()
sleep(3)
browser.find_element_by_xpath('//*[@id="langSecLink"]/a').click()
sleep(3)
browser.find_element_by_xpath('//div[@id="langten"]').click()
sleep(3)
browser.find_element_by_xpath('//*[@id="form-buttons"]/div[1]').click()
sleep(3)
browser.switch_to_alert().accept()
sleep(10)
browser.quit()
