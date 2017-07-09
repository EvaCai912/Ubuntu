#-*-coding:utf-8 -*-

from selenium import webdriver
import time

browser = webdriver.Chrome()
browser.get("http://www.baidu.com")

#浏览器固定宽高
browser.set_window_size(400,300)
print "wait 10s..."
time.sleep(10)

browser.maximize_window()
print "Wait 10s..."
time.sleep(10)

browser.close()
