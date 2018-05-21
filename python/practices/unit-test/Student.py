# -*- coding: utf-8 -*-
# @Author: Administrator
# @Date:   2018-05-17 10:46:51
# @Last Modified by:   Administrator
# @Last Modified time: 2018-05-17 11:04:06
class Student(object):
  """docstring for Student"""
  def __init__(self, name, score):
    self.name = name
    # if score >= 0 and score <= 100:
    #   self._score = score
    # else:
    #   raise ValueError('Score should in range of 0 and 100')
    self._score = score

  def get_grade(self):
    score = self._score
    if score > 100:
      raise ValueError('score should less than 100')
    elif score >= 80:
      return 'A'
    elif score >= 60:
      return 'B'
    elif score < 0:
      raise ValueError('score should larger than 0')
    return 'C'
    