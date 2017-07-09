#!/usr/bin/python
#-*-coding:utf-8 -*-

from selenium import webdriver
import time

browser = webdriver.Chrome()
browser.get("http://www.google.com")
browser.find_element_by_name("q").send_keys(u'哈哈')
browser.find_element_by_name("btnK").click()
time.sleep(5)
browser.close()
