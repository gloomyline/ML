# -*- coding: utf-8 -*-
# @Author: 1211071880@qq.com
# @Date:   2018-05-21 17:36:35
# @Last Modified by:   1211071880@qq.com
# @Last Modified time: 2018-05-21 18:01:34
import csv

class Outputer(object):
  def __init__(self, output=None):
    temp_output = output or 'playlist.hot.csv'
    csv_file = open(temp_output, 'w', encoding='utf-8', newline='')
    self.writer = csv.writer(csv_file)
    self.writer.writerow(['标题', '播放数', '链接'])

  def write(self, content):
    self.writer.writerow(content)

  def close(self):
    self.writer.close()