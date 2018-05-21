# -*- coding: utf-8 -*-
# @Author: Administrator
# @Date:   2018-05-18 14:24:37
# @Last Modified by:   Administrator
# @Last Modified time: 2018-05-18 16:28:43
import curses
from itertools import chain
from screen import Screen
from grid import Grid
from action import Action

class GameManager(object):

  def __init__(self, size=4, win_num=2048):
    self.size = size
    self.win_num = win_num
    self.reset()

  def reset(self):
    self.state = 'init'
    self.win = False
    self.over = False
    self.score = 0
    self.grid = Grid(self.size)
    self.grid.reset()

  @property
  def screen(self):
    return Screen(screen=self.stdscr, score=self.score, grid=self.grid, win=self.win, over=self.over)

  def move(self, direction):
    if self.can_move(direction):
      getattr(self.grid, 'move_' + direction)()
      self.grid.add_random_item()
      return True
    else:
      return False

  @property
  def is_win(self):
    self.win = max(chain(*self.grid.cells)) >= self.win_num
    return self.win

  @property
  def is_over(self):
    self.over = not any(self.can_move(move) for move in self.action.actions)
    return self.over

  def can_move(self, direction):
    return getattr(self.grid, 'can_move_' + direction)()

  def state_init(self):
    self.reset()
    return 'game'

  def state_game(self):
    self.screen.draw()
    action = self.action.get()

    if action == Action.RESTART:
        return 'init'
    if action == Action.EXIT:
        return 'exit'
    if self.move(action):
        if self.is_win:
            return 'win'
        if self.is_over:
            return 'over'
    return 'game'

  def _restart_or_exit(self):
    self.screen.draw()
    return 'init' if self.action.get() == Action.RESTART else 'exit'

  def state_win(self):
    return self._restart_or_exit()

  def state_over(self):
    return self._restart_or_exit()

  def __call__(self, stdscr):
    curses.use_default_colors()
    self.stdscr = stdscr
    self.action = Action(stdscr)
    while self.state != 'exit':
        self.state = getattr(self, 'state_' + self.state)()
