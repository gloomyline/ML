# -*- coding: utf-8 -*-
# @Author: Administrator
# @Date:   2018-05-18 14:18:41
# @Last Modified by:   Administrator
# @Last Modified time: 2018-05-18 16:18:21
class Action(object):

  UP = 'up'
  LEFT = 'left'
  DOWN = 'down'
  RIGHT = 'right'
  RESTART = 'restart'
  EXIT = 'exit'

  letter_codes = [ord(ch) for ch in 'WASDRQwasdrq']
  actions = [UP, LEFT, DOWN, RIGHT, RESTART, EXIT]
  actions_dict = dict(zip(letter_codes, actions * 2))

  def __init__(self, stdscr):
    self.stdscr = stdscr

  def get(self):
    char = "N"
    while char not in self.actions_dict:
        char = self.stdscr.getch()
    return self.actions_dict[char]