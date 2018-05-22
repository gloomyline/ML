# -*- coding: utf-8 -*-
# @Author: 1211071880@qq.com
# @Date:   2018-05-21 16:05:16
# @Last Modified by:   1211071880@qq.com
# @Last Modified time: 2018-05-21 16:17:01
from selenium import webdriver
import time
import os
os.environ['LANG'] = 'en_US.UTF-8'

driver = webdriver.Chrome()  # Optional argument, if not specified will search path.
driver.get('http://www.google.com/xhtml');
time.sleep(5) # Let the user actually see something!
search_box = driver.find_element_by_name('q')
search_box.send_keys('ChromeDriver')
search_box.submit()
time.sleep(5) # Let the user actually see something!
driver.quit()

r'''
There is a problem in the process of using WebDriver created by Selenium with chromedriver.
It seems that my chrome versions is too out.
But I just do not wanna upgrade it, so I turn to Firefox, it seems working.
'''