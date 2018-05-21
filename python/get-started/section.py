# -*- coding: utf-8 -*-
# @Author: Administrator
# @Date:   2018-05-11 08:45:53
# @Last Modified by:   Administrator
# @Last Modified time: 2018-05-11 09:29:34

L = ['Alan', 'CTT', 'James', 'Lebron', 'Bob']

# L[0:3]表示，从索引0开始取，直到索引3为止，但不包括索引3。即索引0，1，2，正好是3个元素。
l = L[0:3]
# l => ['Alan', 'CTT', 'James']

# 如果第一个索引是0，还可以省略：
l1 = L[:3]

# Python支持L[-1]取倒数第一个元素，那么它同样支持倒数切片\
l2 = L[-2:]
# l2 => ['Lebron', 'Bob']

# tuple也是一种list，唯一区别是tuple不可变。因此，tuple也可以用切片操作，只是操作的结果仍是tuple：
# >>> (0, 1, 2, 3, 4, 5)[:3]
# (0, 1, 2)

# practice
# 利用切片操作，实现一个trim()函数，去除字符串首尾的空格，注意不要调用str的strip()方法：

def trim(s):
  if len(s) == 0:
    return ''
  # if first character of the str is space, delete it by splicing until it is nonespace
  while s[:1] == ' ':
    s = s[1:]
  # if last character of the str is space, delete it by splicing until it is nonespace
  while s[-1:] == ' ':
    s = s[:-1]
  return s

# 测试:
if trim('hello  ') != 'hello':
  print('测试失败!')
elif trim('  hello') != 'hello':
  print('测试失败!')
elif trim('  hello  ') != 'hello':
  print('测试失败!')
elif trim('  hello  world  ') != 'hello  world':
  print('测试失败!')
elif trim('') != '':
  print('测试失败!')
elif trim('    ') != '':
  print('测试失败!')
else:
  print('测试成功!')