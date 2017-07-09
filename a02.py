# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

#创建一个WebDriver实例
driver=webdriver.Chrome()
#用实例打开Python官网
driver.get('http://www.python.org')
assert "Python" in driver.title
#找到属性name为q的元素
elem = driver.find_element_by_name('q')
elem.send_keys('pycon')
elem.send_keys(Keys.RETURN)
print driver.page_source
