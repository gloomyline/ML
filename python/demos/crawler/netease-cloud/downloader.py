# -*- coding: utf-8 -*-
# @Author: 1211071880@qq.com
# @Date:   2018-05-21 16:57:36
# @Last Modified by:   1211071880@qq.com
# @Last Modified time: 2018-05-21 18:02:35
from selenium import webdriver

class Downloader(object):
  def __init__(self, browser_path=None):
    self.path = browser_path
    self._init_web_driver()

  def _init_web_driver(self):
    # 用 Firefox 接口创建一个 Selenium 的 WebDriver
    # There is an optional arg for 'firefox', if not referrence, 
    # it will search environ path to find the 'geckodriver.exe'
    self._driver = None
    if self.path:
      self._driver = webdriver.Firefox(self.path)
    else:
      self._driver = webdriver.Firefox()

  def download(self, url):
    self._driver.get(url)
    self._driver.switch_to.frame('contentFrame')
    return self._driver
