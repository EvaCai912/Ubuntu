from selenium import webdriver
import time

browser = webdriver.Chrome()
browser.get("https://www.google.com")
browser.find_element_by_link_text("Gmail").click()
browser.implicitly_wait(30)

browser.find_element_by_id("identifierId").send_keys('912908216@qq.com')
#browser.find_element_by_class_name("RveJvd snByac").click()
browser.implicitly_wait(10)
browser.close()
