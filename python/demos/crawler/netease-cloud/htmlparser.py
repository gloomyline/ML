# -*- coding: utf-8 -*-
# @Author: 1211071880@qq.com
# @Date:   2018-05-21 17:12:35
# @Last Modified by:   1211071880@qq.com
# @Last Modified time: 2018-05-21 18:03:29
class HtmlParser(object):
  def parse(self, driver):
    play_list = list()
    data = driver.find_element_by_id('m-pl-container')\
      .find_elements_by_tag_name('li')
    for idx in range(len(data)):
      nb = data[idx].find_element_by_class_name('nb').text
      if '万' in nb and int(nb.split('万')[0]) > 100:
        msk = data[idx].find_element_by_css_selector('a.msk')
        play_list.append([msk.get_attribute('title'), nb, msk.get_attribute('href')])
    nxt_url = driver.find_element_by_css_selector('a.zbtn.znxt').get_attribute('href')
    return play_list, nxt_url
