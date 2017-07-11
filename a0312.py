from selenium import webdriver
import time

browser = webdriver.Chrome()
browser.get('http://www.google.com')
browser.add_cookie({'name':'key-aaaaaaa', 'value':'value-bbbb'})
browser.delete_cookie('domain')
browser.delete_all_cookies()
print browser.get_cookies()
#browser.add_cookie({'name':'key-aaaaaaa', 'value':'value-bbbb'})
#for cookie in browser.get_cookies():
#	print cookie['name']

time.sleep(10)
browser.quit()
