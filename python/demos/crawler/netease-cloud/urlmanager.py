# -*- coding: utf-8 -*-
# @Author: 1211071880@qq.com
# @Date:   2018-05-21 17:32:23
# @Last Modified by:   1211071880@qq.com
# @Last Modified time: 2018-05-21 17:59:15
class UrlManager(object):
  """docstring for UrlManager"""
  def __init__(self, init_url=''):
    self.url_pool = list()
    self.url_pool.append(init_url)

  def get_url(self):
    if len(self.url_pool) > 0:
      return url_pool.pop()
    else:
      return False

  def add_url(self, url):
    self.url_pool.append(url)