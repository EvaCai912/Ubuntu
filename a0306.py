from selenium import webdriver
import time

browser=webdriver.Chrome()

url1 = "http://www.baidu.com"
url2 = "http://www.google.com"

browser.get(url1)
print url1
time.sleep(10)

browser.get(url2)
print url2
time.sleep(10)

browser.back()
print 'back to %s' %(url1)
browser.forward()
print 'foward to %s' %(url2)
