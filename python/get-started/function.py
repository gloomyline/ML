# -*- coding: utf-8 -*-
# @Author: Administrator
# @Date:   2018-05-10 14:36:47
# @Last Modified by:   Administrator
# @Last Modified time: 2018-05-10 16:48:25
import math

# 1111 1111 => 0xff
a = 255
# 0011 1110 0111 => 0x3e8
b = 1000
print(hex(a), hex(b))

def my_abs(x):
  if not isinstance(x, (int, float)):
    raise TypeError('bad operand type')
  if x >- 0:
    return x
  else:
    return -x
print(my_abs(-1.1))

def move(x, y, step, angle=0):
  dx = x + step * math.cos(angle)
  dy = x + step * math.sin(angle)
  return dx, dy
print(move(0, 0, math.sqrt(2), math.pi / 4))

# practice
# 请定义一个函数quadratic(a, b, c)，接收3个参数，返回一元二次方程：
# ax ^ 2 + bx + c = 0 的两个解。
# 
def quadratic(a, b, c):
  x = math.pow(b, 2) - 4 * a * c
  y = 4 * math.pow(a, 2)
  z = math.sqrt(x / y)
  return (z - b / (2 * a)), (-z - b / (2 * a)) 

# 测试:
print('quadratic(2, 3, 1) =', quadratic(2, 3, 1))
print('quadratic(1, 3, -4) =', quadratic(1, 3, -4))

if quadratic(2, 3, 1) != (-0.5, -1.0):
    print('测试失败')
elif quadratic(1, 3, -4) != (1.0, -4.0):
    print('测试失败')
else:
    print('测试成功')

# position args
def power(x, n):
  s = 1
  while n > 0:
    s *= x
    n -= 1
  return s
print(power(16, 4))

# default args
def power1(x, n = 2):
  s = 1
  while n > 0:
    s *= x
    n -= 1
  return s
print(power1(5))

def enroll(name, gender, age=6, city='Beijing'):
  print('name:', name)
  print('gender:', gender)
  print('age:', age)
  print('city:', city)

# 也可以不按顺序提供部分默认参数。当不按顺序提供部分默认参数时，
# 需要把参数名写上。比如调用enroll('Adam', 'M', city='Tianjin')，
# 意思是，city参数用传进去的值，其他默认参数继续使用默认值。
# 
# Note: 定义默认参数要牢记一点：默认参数必须指向不变对象！

# alterble args
def calc(numbers):
  sum = 0
  for number in numbers:
    sum += power1(number)
  return sum

def calc1(*numbers):
  sum = 0
  for number in numbers:
    sum += power1(number)
  return sum

# Python允许你在list或tuple前面加一个*号，把list或tuple的元素变成可变参数传进去

# keyword args
# 关键字参数允许你传入0个或任意个含参数名的参数，这些关键字参数在函数内部自动组装为一个dict
def person(name, age, **kw):
  pass

# practice
# 以下函数允许计算两个数的乘积，请稍加改造，变成可接收一个或多个数并计算乘积：
# def product(x, y):
#   return x * y
def product(*args):
  if len(args) == 0:
    raise TypeError('needed at least one arguments')
  s = 1
  for x in args:
    s *= x
  return s

# 测试
print('product(5) =', product(5))
print('product(5, 6) =', product(5, 6))
print('product(5, 6, 7) =', product(5, 6, 7))
print('product(5, 6, 7, 9) =', product(5, 6, 7, 9))
if product(5) != 5:
  print('测试失败!')
elif product(5, 6) != 30:
  print('测试失败!')
elif product(5, 6, 7) != 210:
  print('测试失败!')
elif product(5, 6, 7, 9) != 1890:
  print('测试失败!')
else:
  try:
    product()
    print('测试失败!')
  except TypeError:
    print('测试成功!')

# 小结
r'''
默认参数一定要用不可变对象，如果是可变对象，程序运行时会有逻辑错误！

要注意定义可变参数和关键字参数的语法：

*args是可变参数，args接收的是一个tuple；

**kw是关键字参数，kw接收的是一个dict。

以及调用函数时如何传入可变参数和关键字参数的语法：

可变参数既可以直接传入：func(1, 2, 3)，又可以先组装list或tuple，再通过*args传入：func(*(1, 2, 3))；

关键字参数既可以直接传入：func(a=1, b=2)，又可以先组装dict，再通过**kw传入：func(**{'a': 1, 'b': 2})。

使用*args和**kw是Python的习惯写法，当然也可以用其他参数名，但最好使用习惯用法。

命名的关键字参数是为了限制调用者可以传入的参数名，同时可以提供默认值。

定义命名的关键字参数在没有可变参数的情况下不要忘了写分隔符*，否则定义的将是位置参数。
'''

# recursion function
# 如果一个函数在内部调用其自身，那么这个函数就是递归函数

# fact(n) = n! = 1 * 2 * 3 ... (n-1) * n
# time complexity O(n)
def fact(n):
  if n <= 1:
    return 1
  else:
    return n * fact(n - 1)

print(fact(100))

# tail recursion call
# time complexity O(1)
def fac(n, s = 1):
  if n <= 1:
    return s
  else:
    return fac(n - 1, s * n)

print(fac(110))

# practice
# 汉诺塔的移动可以用递归函数非常简单地实现
# 请编写move(n, a, b, c)函数，它接收参数n，
# 表示3个柱子A、B、C中第1个柱子A的盘子数量，然后打印出把所有盘子从A借助B移动到C的方法，例如：
def move(n, a, b, c):
  if n == 1:
    print('move', a, '-->', c)
  else:
    move(n - 1, a, c, b)
    move(1, a, b, c)
    move(n - 1, b, a, c)

move(3, 'A', 'B', 'C')