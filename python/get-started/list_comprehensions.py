# -*- coding: utf-8 -*-
# @Author: Administrator
# @Date:   2018-05-11 10:04:50
# @Last Modified by:   Administrator
# @Last Modified time: 2018-05-11 10:18:25

l = list(range(1, 11))
# l => [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

l1 = [x * x for x in range(1, 11)] 
print(l1)
# => [1, 4, ... 81, 100]

# for循环后面还可以加上if判断，这样我们就可以筛选出仅偶数的平方：
l2 = [x * x for x in range(1, 11) if x % 2 == 0]
print(l2)
# => [4, 16, 36, 64, 100]

# 还可以使用两层循环，可以生成全排列：
l3 = [m + n for m in 'ABC' for n in 'XYZ']
print(l3)
# => ['AX', 'AY', 'AZ', 'BX', 'BY', 'BZ', 'CX', 'CY', 'CZ']

# 列出当前目录下的所有文件和目录名，可以通过一行代码实现
import os
# os.listdir can list the files and directories
l4 = [d for d in os.listdir('.')]
print(l4)

# 列表生成式也可以使用两个变量来生成list
d = {'x': 'A', 'y': 'B', 'z': 'C' }
l5 = [k + '=' + v for k, v in d.items()]
print(l5)
# => ['x=A', 'y=B', 'z=C']

# 把一个list中所有的字符串变成小写
L = ['Hello', 'World', 'IBM', 'Apple']
ll = [s.lower() for s in L]
print(ll)
# => ['hello', 'world', 'ibm', 'apple']
# 
# practice
# 如果list中既包含字符串，又包含整数，由于非字符串类型没有lower()方法，所以列表生成式会报错：
r'''
>>> L = ['Hello', 'World', 18, 'Apple', None]
>>> [s.lower() for s in L]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 1, in <listcomp>
AttributeError: 'int' object has no attribute 'lower'
使用内建的isinstance函数可以判断一个变量是不是字符串：
>>> x = 'abc'
>>> y = 123
>>> isinstance(x, str)
True
>>> isinstance(y, str)
False
请修改列表生成式，通过添加if语句保证列表生成式能正确地执行：
'''
L1 = ['Hello', 'World', 18, 'Apple', None]
L2 = [s.lower() for s in L1 if isinstance(s, str)]
print(L2)
# => ['hello', 'world', 'apple']