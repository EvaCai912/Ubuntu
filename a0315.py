# coding:utf-8
#显性等待webdriver
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
browser.get('http://www.dapenti.com/blog/index.asp')
try:
	WebDriverWait(browser,20,0.5).until(EC.presence_of_element_located((By.ID,'tanx-s-mm_10006712_103995_70582412')))
	print '成功实现显性等待'
finally:
	browser.close()



browser.quit()
