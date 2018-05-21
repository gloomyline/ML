# -*- coding: utf-8 -*-
# @Author: Administrator
# @Date:   2018-05-11 10:22:27
# @Last Modified by:   Administrator
# @Last Modified time: 2018-05-11 14:02:16

# 要创建一个generator，有很多种方法。第一种方法很简单，
# 只要把一个列表生成式的[]改成()，就创建了一个generator：
g = (x * x for x in range(1, 11))
print(g)
# => <generator object <genexpr> at 0x006581B0>

# generator保存的是算法，每次调用next(g)，
# 就计算出g的下一个元素的值，直到计算到最后一个元素，
# 没有更多的元素时，抛出StopIteration的错误

# 不断调用next(g)实在是太变态了，正确的方法是使用for循环，因为generator也是可迭代对象
for n in g:
  print(n)

# generator非常强大。如果推算的算法比较复杂，
# 用类似列表生成式的for循环无法实现的时候，还可以用函数来实现
# 著名的斐波拉契数列（Fibonacci），除第一个和第二个数外，任意一个数都可由前两个数相加得到：
# 1, 1, 2, 3, 5, 8, 13, 21, 34, ...
# 斐波拉契数列用列表生成式写不出来，但是，用函数把它打印出来却很容易：
def fib(max):
  n, a, b = 0, 0, 1
  while n < max:
    print(b)
    a, b = b, a + b # the same as t = (b, a + b), a = t[0], b = t[1]
    n += 1
  print('done')
fib(6)

# 上面的函数和generator仅一步之遥。要把fib函数变成generator，只需要把print(b)改为yield b就可以了
def g_fib(max):
  n, a, b = 0, 0, 1
  while n < max:
    yield b
    a, b = b, a + b
    n += 1
  return 'done'
# 如果一个函数定义中包含yield关键字，那么这个函数就不再是一个普通函数，而是一个generator
# >>> f = g_fib(6)
# >>> f
# <generator object fib at 0x104feaaa0>

# practice
r'''
杨辉三角定义如下：

          1
         / \
        1   1
       / \ / \
      1   2   1
     / \ / \ / \
    1   3   3   1
   / \ / \ / \ / \
  1   4   6   4   1
 / \ / \ / \ / \ / \
1   5   10  10  5   1
把每一行看做一个list，试写一个generator，不断输出下一行的list：
'''
def triangles():
  n, l = 0, [1]
  while True:
    yield l
    l = [1] + [l[i] + l[i + 1] for i in list(range(len(l) - 1))] + [1]

# 期待输出:
# [1]
# [1, 1]
# [1, 2, 1]
# [1, 3, 3, 1]
# [1, 4, 6, 4, 1]
# [1, 5, 10, 10, 5, 1]
# [1, 6, 15, 20, 15, 6, 1]
# [1, 7, 21, 35, 35, 21, 7, 1]
# [1, 8, 28, 56, 70, 56, 28, 8, 1]
# [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]
n = 0
results = []
for t in triangles():
  print(t)
  results.append(t)
  n = n + 1
  if n == 10:
    break
if results == [
  [1],
  [1, 1],
  [1, 2, 1],
  [1, 3, 3, 1],
  [1, 4, 6, 4, 1],
  [1, 5, 10, 10, 5, 1],
  [1, 6, 15, 20, 15, 6, 1],
  [1, 7, 21, 35, 35, 21, 7, 1],
  [1, 8, 28, 56, 70, 56, 28, 8, 1],
  [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]
]:
  print('测试通过!')
else:
  print('测试失败!')