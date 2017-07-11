from selenium import webdriver
import time

browser = webdriver.Chrome()
browser.get('http://passport.cnblogs.com/login.aspx?ReturnUrl=http://www.cnblogs.com/fnng/admin/EditPosts.aspx')
browser.find_element_by_id('input1').send_keys('912908216')
browser.find_element_by_id('input2').send_keys('1qaz2wsx!')
#browser.find_element_by_id('remember_me').click()
browser.find_element_by_id('signin').submit()

print browser.get_cookies()
time.sleep(10)
browser.quit()
