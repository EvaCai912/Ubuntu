# coding=utf-8

#使用 selenium 的 webdriver里的函数
from selenium import webdriver

#调用Chrome浏览器
browser = webdriver.Chrome()
#测试baidu页面
browser.get("http://www.baidu.com")
#查找id为kw的控件，键入selenium
browser.find_element_by_id("kw").send_keys("selenium")
#查找id为su的控件，点击
browser.find_element_by_id("su").click()
#退出并关闭插口的每个相关驱动程序
#browser.quit()

#关闭当前窗口
#browser.close()
