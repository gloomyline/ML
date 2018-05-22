# -*- coding: utf-8 -*-
# @Author: 1211071880@qq.com
# @Date:   2018-05-21 16:10:51
# @Last Modified by:   1211071880@qq.com
# @Last Modified time: 2018-05-21 16:11:53
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()
driver.get("http://www.python.org")
assert "Python" in driver.title
elem = driver.find_element_by_name("q")
elem.clear()
elem.send_keys("pycon")
elem.send_keys(Keys.RETURN)
assert "No results found." not in driver.page_source
driver.close()