# -*- coding: utf-8 -*-
# @Author: Administrator
# @Date:   2018-05-18 13:37:45
# @Last Modified by:   Administrator
# @Last Modified time: 2018-05-18 16:26:00
class Screen(object):

  help_string1 = '(W)up (S)down (A)left (D)right'
  help_string2 = '     (R)Restart (Q)Exit'
  over_string = '           GAME OVER'
  win_string = '          YOU WIN!'

  def __init__(self, screen=None, grid=None, score=0, best_score=0, over=False, win=False):
    self.grid = grid
    self.score = score
    self.over = over
    self.win = win
    self.screen = screen
    self.counter = 0

  def cast(self, string):
    self.screen.addstr(string + '\n')

  def draw_row(self, row):
    self.cast(''.join('|{: ^5}'.format(num) if num > 0 else '|     ' for num in row) + '|')

  def draw(self):
    self.screen.clear()
    self.cast('SCORE: ' + str(self.score))
    for row in self.grid.cells:
        self.cast('+-----' * self.grid.size + '+')
        self.draw_row(row)
    self.cast('+-----' * self.grid.size + '+')

    if self.win:
        self.cast(self.win_string)
    else:
        if self.over:
            self.cast(self.over_string)
        else:
            self.cast(self.help_string1)

    self.cast(self.help_string2)
