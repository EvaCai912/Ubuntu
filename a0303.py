from selenium import webdriver

browser = webdriver.Chrome()
browser.get("http://www.dapenti.com/blog/index.asp")
print 'Wait...'
print browser.title
print "OK!"

