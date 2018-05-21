# -*- coding: utf-8 -*-
# @Author: Administrator
# @Date:   2018-05-18 14:53:59
# @Last Modified by:   Administrator
# @Last Modified time: 2018-05-18 14:54:57
import curses
from manager import GameManager

if __name__ == '__main__':
  curses.wrapper(GameManager())