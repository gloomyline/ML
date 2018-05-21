# -*- coding: utf-8 -*-
# @Author: Administrator
# @Date:   2018-05-10 11:57:24
# @Last Modified by:   Administrator
# @Last Modified time: 2018-05-10 14:17:24
from random import randint

sum = 0
for x in range(1, 11):
  sum += x
print(sum)

s = 0
i = 99
while i > 0:
  s += i
  i -= 2
print(s)

# practice
# 请利用循环依次对list中的每个名字打印出Hello, xxx!：
names = ['CTT', 'Alan', 'James', 'Bob']
for name in names:
  print('Hello, %s!' % name)

def bre(s_n):
  sum = 0
  while s_n > 0:
    s_n -= 2
    sum += s_n
    if s_n <= 90:
      break
  return sum
print(bre(99))

def con(s_n, e_n):
  n = s_n
  while n < e_n:
    n += 1
    if n % 2 != 0:
      continue
    print(n)
con(0, 10)