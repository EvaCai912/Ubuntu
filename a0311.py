from selenium import webdriver
import time

browser = webdriver.Chrome()
browser.get('http://www.google.com')
cookies=browser.get_cookies();
print cookies
time.sleep(5)

browser.quit()
