# -*- coding: utf-8 -*-
# @Author: Administrator
# @Date:   2018-05-11 14:07:56
# @Last Modified by:   Administrator
# @Last Modified time: 2018-05-16 09:16:49

# Higher-order function
# 变量可以指向函数
# 函数名也是变量
# 编写高阶函数，就是让函数的参数能够接收别的函数。

# map() && reduce()
# map()函数接收两个参数，一个是函数，一个是Iterable，map将传入的函数依次作用到序列的每个元素，
# 并把结果作为新的Iterator返回
# 
# reduce把一个函数作用在一个序列[x1, x2, x3, ...]上，这个函数必须接收两个参数，
# reduce把结果继续和序列的下一个元素做累积计算，其效果就是：
# reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)

from functools import reduce
DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
def str2int(s):
  def cha2num(ch):
    if DIGITS[ch]:
      return DIGITS[ch]
    else:
      raise ReferenceError('The str needs to only include int')
  return reduce(lambda x, y: x * 10 + y, map(cha2num, s))

print(str2int('12345'))

# practice
# 1. 利用map()函数，把用户输入的不规范的英文名字，
# 变为首字母大写，其他小写的规范名字。输入：['adam', 'LISA', 'barT']，输出：['Adam', 'Lisa', 'Bart']
def normalize(name):
  return name[:1].upper() + name.lower()[1:]

# 测试:
L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)

# 2. Python提供的sum()函数可以接受一个list并求和，请编写一个prod()函数，可以接受一个list并利用reduce()求积：
def prod(L):
  return reduce(lambda x, y: x * y, L)
# test
print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))
if prod([3, 5, 7, 9]) == 945:
    print('测试成功!')
else:
    print('测试失败!')

# 3. 利用map和reduce编写一个str2float函数，把字符串'123.456'转换成浮点数123.456：
def str2float(s):
  # divide the number str into integer and decimals
  l = s.split('.')
  # the integer part
  intP = l[0]
  # the decimal part
  decP = l[1]
  return str2int(intP + decP) / (10 ** len(decP))
# test
print('str2float(\'123.456\') =', str2float('123.456'))
if abs(str2float('123.456') - 123.456) < 0.00001:
    print('测试成功!')
else:
    print('测试失败!')

# filter() 用于过滤序列
# 和map()类似，filter()也接收一个函数和一个序列。和map()不同的是，
# filter()把传入的函数依次作用于每个元素，然后根据返回值是True还是False决定保留还是丢弃该元素

# 在一个list中，删掉偶数，只保留奇数，
def is_odd(num):
  return num % 2 != 0

l = list(filter(is_odd, [1, 2, 4, 5, 6, 9, 10, 15]))
print(l)
# => [1, 5, 9, 15]

# 把一个序列中的空字符串删掉，可以这么写:
def i_trip(l):
  return list(filter(lambda e: e and e.strip(), l))

print(i_trip(['A', '', 'B', None, 'C', '  ']))
# => ['A', 'B', 'C']

# filter()函数返回的是一个Iterator，也就是一个惰性序列，
# 所以要强迫filter()完成计算结果，需要用list()函数获得所有结果并返回lis

# 用filter求素数
r'''
计算素数的一个方法是埃氏筛法，它的算法理解起来非常简单：

首先，列出从2开始的所有自然数，构造一个序列：

2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, ...

取序列的第一个数2，它一定是素数，然后用2把序列的2的倍数筛掉：

3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, ...

取新序列的第一个数3，它一定是素数，然后用3把序列的3的倍数筛掉：

5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, ...

取新序列的第一个数5，然后用5把序列的5的倍数筛掉：

7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, ...

不断筛下去，就可以得到所有的素数。
'''
# iterator for constructing a list consist of odd natural number
def _odd_iter():
  n = 1
  while True:
    n += 2
    yield n

# filter function, filter number which are not multiple of given 'n'
def _not_divisible(n):
  return lambda x: x % n > 0

def g_prime():
   yield 2
   # construct the list consist of odd natural number from 3
   it = _odd_iter()
   while True:
    # get the first number of current iterable
    n = next(it)
    # the first number is certainly a prime, yield it
    yield n
    # delete the multiple number of which was yielded before to get a new iterable
    it = filter(_not_divisible(n), it)

# print prime less than 100
for prime in g_prime():
  if prime > 100:
    break
  print(prime)

# Note: Iterator是惰性计算的序列，所以我们可以用Python表示“全体自然数”，“全体素数”这样的序列，而代码非常简洁

# practice
# 回数是指从左向右读和从右向左读都是一样的数，例如12321，909。请利用filter()筛选出回数
def is_palindrome(n):
  return str(n) == str(n)[::-1]

# 测试:
output = filter(is_palindrome, range(1, 1000))
print('1~1000:', list(output))
if list(filter(is_palindrome, range(1, 200))) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22, 33, 44, 55, 66, 77, 88, 99, 101, 111, 121, 131, 141, 151, 161, 171, 181, 191]:
    print('测试成功!')
else:
    print('测试失败!')

# sorted
# 排序也是在程序中经常用到的算法。无论使用冒泡排序还是快速排序，排序的核心是比较两个元素的大小

# practice
# 假设我们用一组tuple表示学生名字和成绩：
L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
# 请用sorted()对上述列表分别按名字排序
def by_name(t):
  return t[0]
L1 = sorted(L, key=by_name)
print(L1)
def by_score(t):
  # 按照分数从高到底排序，sorted默认从低到高，让映射函数返回值取其相反数，即可满足从高到低的要求
  return -t[1]
L2 = sorted(L, key=by_score)
print(L2)

# 函数作为返回值
# 高阶函数除了可以接受函数作为参数外，还可以把函数作为结果值返回
def calc_num(*args):
  ax = 0
  for n in args:
    ax += n
  return ax

def lazy_sum(*args):
  def sum():
    res = 0
    for n in args:
      res += n
    return res
  return sum

r'''
我们在函数lazy_sum中又定义了函数sum，
并且，内部函数sum可以引用外部函数lazy_sum的参数和局部变量，
当lazy_sum返回函数sum时，相关参数和变量都保存在返回的函数中，
这种称为“闭包（Closure）”的程序结构拥有极大的威力。

请再注意一点，当我们调用lazy_sum()时，每次调用都会返回一个新的函数，即使传入相同的参数：
'''
f1 = lazy_sum(1, 2, 3, 4)
f2 = lazy_sum(1, 2, 3, 4)
print(f1())
print(f1 == f2)
# => False
# f1()和f2()的调用结果互不影响。

# Closure

# 返回的函数并没有立刻执行，而是直到调用了f()才执行。
# 返回闭包时牢记一点：返回函数不要引用任何循环变量，或者后续会发生变化的变量
def count():
  fs = []
  def f(x):
    return lambda: x * x
  for i in range(1, 4):
    fs.append(f(i))
  return fs

f1, f2, f3 = count()
print(f1(), f2(), f3())

# practice
# 利用闭包返回一个计数器函数，每次调用它返回递增整数：
def createCounter():
  n = 0
  def counter():
    nonlocal n # 此处可使用list可变对象存储计数，int不是可变对象，返回的n每次都新建了一个整数对象
    n = n + 1
    return n
  return counter

# 测试:
counterA = createCounter()
print(counterA(), counterA(), counterA(), counterA(), counterA()) # 1 2 3 4 5
counterB = createCounter()
if [counterB(), counterB(), counterB(), counterB()] == [1, 2, 3, 4]:
  print('测试通过!')
else:
  print('测试失败!')

# Decorator
from functools import wraps
def log(func):
  @wraps(func)
  def wrapper(*args, **kw):
    print('call %s' % func.__name__)
    return func(*args, **kw)
  return wrapper

@log
def i_sum(*args):
  res = 0
  for n in args:
    res += n
  return res
print(i_sum(1, 2, 3, 4))

# 把@log放到now()函数的定义处，相当于执行了语句：
# i_sum = log(i_sum)
# 
# 如果decorator本身需要传入参数，那就需要编写一个返回decorator的高阶函数，写出来会更复杂。
# 比如，要自定义log的文本
def cus_log(text):
  def decorator(func):
    # 经过decorator装饰之后的函数，它们的__name__已经从原来的'now'变成了'wrapper'
    @wraps(func)
    def wrapper(*args, **kw):
      print('%s %s()' % (text, func.__name__))
      return func(*args, **kw)
    return wrapper
  return decorator

@cus_log('excute')
def now():
  print('2018-5-11')
now()
# 和两层嵌套的decorator相比，3层嵌套的效果是： now = cus_log('excute')(now)
print(now.__name__)

# practice
# 请设计一个decorator，它可作用于任何函数上，并打印该函数的执行时间：
import time
def metric(func):
  @wraps(func)
  def wrapper(*args, **kw):
    start = time.time()
    result = func(*args, **kw)
    print('%s excuted in %s ms' % (func.__name__, time.time() - start))
    return result
  return wrapper

# 测试
@metric
def fast(x, y):
    time.sleep(0.0012)
    return x + y;

@metric
def slow(x, y, z):
    time.sleep(0.1234)
    return x * y * z;

f = fast(11, 22)
s = slow(11, 22, 33)
if f != 33:
    print('测试失败!')
elif s != 7986:
    print('测试失败!')

# 偏函数(Partial function)
# functools.partial就是帮助我们创建一个偏函数的，
# 不需要我们自己定义int2()，可以直接使用下面的代码创建一个新的函数int2：
import functools
int2 = functools.partial(int, base=2)

# 简单总结functools.partial的作用就是，把一个函数的某些参数给固定住（也就是设置默认值），
# 返回一个新的函数，调用这个新函数会更简单