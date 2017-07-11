#coding:utf-8
from selenium import webdriver
import os
import time


browser = webdriver.Chrome()
file_path='file:///'+os.path.abspath('upload_file.html')
browser.get(file_path)

browser.find_element_by_name('file').send_keys('/home/eva/Ubuntu_git/readme.txt')
time.sleep(10)
browser.quit()
