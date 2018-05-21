# -*- coding: utf-8 -*-
# @Author: Administrator
# @Date:   2018-05-17 11:32:06
# @Last Modified by:   Administrator
# @Last Modified time: 2018-05-17 13:32:04
class Filer(object):
  """docstring for WriteAndRead"""
  def __init__(self, fpath='', content='test'):
    self._fpath = fpath
    self._content = content

  def write(self, content, mode):
    with open(self._fpath, mode) as f:
      f.write(content or self._content)
    
  def read(self):
    with open(self._fpath, 'r') as f:
      return f.read()

fpath = r'test.txt'
filer = Filer(fpath)
filer.write('', 'a')
print(filer.read())
