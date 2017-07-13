# coding:utf-8
#Path
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
browser.get('http://www.dapenti.com/blog/index.asp')
try:
	WebDriverWait(browser,5,0.5).until(EC.presence_of_element_located((By.ID,'tanx-s-mm_10006712_103995_70582412')))
	print '成功实现显性等待'
	lis=browser.find_element_by_xpath('//*[@id="center"]/table[1]/tbody/tr[2]/td[1]/div/ul/li[6]/a/..').text
	print lis
finally:
	browser.close()



browser.quit()
