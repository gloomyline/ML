# -*- coding: utf-8 -*-
# @Author: Administrator
# @Date:   2018-05-21 14:33:46
# @Last Modified by:   1211071880@qq.com
# @Last Modified time: 2018-05-21 17:58:12

# from selenium import webdriver
# import csv
from downloader import Downloader
from htmlparser import HtmlParser
from urlmanager import UrlManager
from outputer import Outputer

# 网易云音乐歌单第一页 url
url = 'http://music.163.com/#/discover/playlist/' \
  '?order=hot&cat=%E5%85%A8%E9%83%A8&limit=35&offset=0'

# driver = webdriver.Firefox()

def crawl(init_url):
  url_pool = UrlManager()
  downloader = Downloader()
  parser = HtmlParser()
  outputer = Outputer()
  temp_url = init_url
  while temp_url:
    driver = downloader.download(temp_url)
    content, temp_url = parser.parse(driver)
    outputer.write(content)
  outputer.close()
    # url_pool.add_url(nxt_url)

  # # 准备好存储歌单的csv文件
  # csv_file = open(output, 'w', encoding='utf-8', newline='')
  # writer = csv.writer(csv_file)
  # writer.writerow(['标题', '播放数', '链接'])

  # # 解析每一页，直到“下一页”为空
  # while temp_url != 'javascript:void(0)':
  #   # 用 WebDriver 加载页面
  #   driver.get(temp_url)
  #   # 切换到内容的 iframe
  #   driver.switch_to.frame('contentFrame')
  #   # 定位歌单标签
  #   data = driver.find_element_by_id("m-pl-container").\
  #     find_elements_by_tag_name('li')
  #   # 解析一页中所有歌单
  #   for i in range(len(data)):
  #     # 获取播放数
  #     nb = data[i].find_element_by_class_name('nb').text
  #     if '万' in nb and int(nb.split('万')[0]) > 500:
  #       # 获取播放数大于500万的歌单封面
  #       msk = data[i].find_element_by_css_selector('a.msk')
  #       # 把封面上的标题和链接联通播放数一起写到文件中
  #       writer.writerow([msk.get_attribute('title'), nb, msk.get_attribute('href')])

  #   # 定位“下一页”的 url
  #   temp_url = driver.find_element_by_css_selector('a.zbtn.znxt').get_attribute('href')
  # return csv_file.close()

if __name__ == '__main__':
  crawl(url)