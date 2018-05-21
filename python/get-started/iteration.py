# -*- coding: utf-8 -*-
# @Author: Administrator
# @Date:   2018-05-11 09:30:02
# @Last Modified by:   Administrator
# @Last Modified time: 2018-05-11 09:49:43

d = { 'a': 1, 'b': 2, 'c': 3 }
for key in d:
  print(key)

print(d.values())
for value in d.values():
  print(value)

print(d.items())
for k, v in d.items():
  print('k: %s, v: %s' % (k, v))

# 当我们使用for循环时，只要作用于一个可迭代对象，for循环就可以正常运行，
# 而我们不太关心该对象究竟是list还是其他数据类型
# 如何判断一个对象是可迭代对象呢？方法是通过collections模块的Iterable类型判断
from collections import Iterable
print(isinstance('abc', Iterable))
# => True
print(isinstance(123, Iterable))
# => False

# 如果要对list实现类似Java那样的下标循环怎么办？
# Python内置的enumerate函数可以把一个list变成索引-元素对，
# 这样就可以在for循环中同时迭代索引和元素本身
l = [1, 2, 3]
for i, v in enumerate(l):
  print('l[%s] = %s' % (i, v))

# practice
# 请使用迭代查找一个list中最小和最大值，并返回一个tuple：
def findMinAndMax(L):
  if len(L) == 0:
    return (None, None)
  min = max = L[0]
  for v in L:
    if v >= max:
      max = v
    elif v < min:
      min = v
  return (min, max)

# 测试
if findMinAndMax([]) != (None, None):
  print('测试失败!')
elif findMinAndMax([7]) != (7, 7):
  print('测试失败!')
elif findMinAndMax([7, 1]) != (1, 7):
  print('测试失败!')
elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
  print('测试失败!')
else:
  print('测试成功!')