# -*- coding: utf-8 -*-
# @Author: Administrator
# @Date:   2018-05-18 13:50:43
# @Last Modified by:   Administrator
# @Last Modified time: 2018-05-18 16:21:47
import random

class Grid(object):

  def __init__(self, size):
    self.size = size
    self.cells = None
    self.reset()

  def reset(self):
    self.cells = [[0 for i in range(self.size)] for j in range(self.size)]
    self.add_random_item()
    self.add_random_item()

  def add_random_item(self):
    empty_cells = [(i, j) for i in range(self.size) for j in range(self.size) if self.cells[i][j] == 0]
    (i, j) = random.choice(empty_cells)
    self.cells[i][j] = 4 if random.randrange(100) >= 90 else 2

  def transpose(self):
    self.cells = [list(row) for row in zip(*self.cells)]

  def invert(self):
    self.cells = [row[::-1] for row in self.cells]

  @staticmethod
  def move_row_left(row):
    def tighten(row):
      new_row = [i for i in row if i != 0]
      new_row += [0 for i in range(len(row) - len(new_row))]
      return new_row

    def merge(row):
      pair = False
      new_row = []
      for i in range(len(row)):
        if pair:
          new_row.append(2 * row[i])
          # self.score += 2 * row[i]
          pair = False
        else:
          if i + 1 < len(row) and row[i] == row[i + 1]:
            pair = True
            new_row.append(0)
          else:
            new_row.append(row[i])
      assert len(new_row) == len(row)
      return new_row
    return tighten(merge(tighten(row)))

  def move_left(self):
    self.cells = [self.move_row_left(row) for row in self.cells]

  def move_right(self):
    self.invert()
    self.move_left()
    self.invert()

  def move_up(self):
    self.transpose()
    self.move_left()
    self.transpose()

  def move_down(self):
    self.transpose()
    self.move_right()
    self.transpose()

  @staticmethod
  def row_can_move_left(row):
    def change(i):
      if row[i] == 0 and row[i + 1] != 0:
        return True
      if row[i] != 0 and row[i + 1] == row[i]:
        return True
      return False
    return any(change(i) for i in range(len(row) - 1))

  def can_move_left(self):
    return any(self.row_can_move_left(row) for row in self.cells)

  def can_move_right(self):
    self.invert()
    can = self.can_move_left()
    self.invert()
    return can

  def can_move_up(self):
    self.transpose()
    can = self.can_move_left()
    self.transpose()
    return can

  def can_move_down(self):
    self.transpose()
    can = self.can_move_right()
    self.transpose()
    return can