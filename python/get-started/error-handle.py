# -*- coding: utf-8 -*-
# @Author: Administrator
# @Date:   2018-05-16 16:43:28
# @Last Modified by:   Administrator
# @Last Modified time: 2018-05-17 10:43:38
import logging

# 错误处理

# def bar(s):
#   return 10 / int(s)

# def foo(s):
#   return 2 * bar(s)

# def main():
#   try:
#     foo('0')
#   except Exception as e:
#     logging.exception(e)

# if __name__ == '__main__':
#   main()
#   print('End')

# practice: 运行下面的代码，根据异常信息进行分析，定位出错误源头，并修复
from functools import reduce

'''
@desc convert str into number
@params s origin str
@return destination number
'''
def str2num(s):
  Digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
  def cha2num(ch):
    if not Digits[ch] and Digits[ch] != 0:
      raise ValueError('Expression included other literals which are not Number.')
    return Digits[ch]
  ls = s.strip().split('.')
  if len(ls) == 1:
    return reduce(lambda x, y: x * 10 + y, map(cha2num, ls[0]))
  elif len(ls) == 2:
    return reduce(lambda x, y: x * 10 + y, map(cha2num, ls[0] + ls[1])) / 10 ** len(ls[1])

def calc(exp):
  ss = exp.split('+')
  ns = map(str2num, ss)
  return reduce(lambda acc, x: acc + x, ns)

def main():
  r = calc('100 + 200 + 345')
  print('100 + 200 + 345 =', r)
  r = calc('99 + 88 + 7.6')
  print('99 + 88 + 7.6 =', r)

# main()

# 调试
# 凡是用print()来辅助查看的地方，都可以用断言（assert）来替代
# 如如果断言失败，assert语句本身就会抛出AssertionError
# 启动Python解释器时可以用-O参数来关闭assert，关闭后，所有的assert可被当做pass
# 把print()替换为logging是第3种方式，和assert比，logging不会抛出错误，而且可以输出到文件
'''
import logging
logging.basicConfig(level=logging.INFO)
'''
# Note: 注意logging的配置，它允许你指定记录信息的级别，有debug，info，warning，error等几个级别
# logging的另一个好处是通过简单的配置，一条语句可以同时输出到不同的地方，比如console和文件。
# 第4种方式是启动Python的调试器pdb，让程序以单步方式运行，可以随时查看运行状态。
'''
# err.py
s = '0'
n = int(s)
print(10 / n)
然后启动：

$ python -m pdb err.py
> /Users/michael/Github/learn-python3/samples/debug/err.py(2)<module>()
-> s = '0'
'''
# pdb.set_trace()
# 这个方法也是用pdb，但是不需要单步执行，我们只需要import pdb，
# 然后，在可能出错的地方放一个pdb.set_trace()，就可以设置一个断点：
# 运行代码，程序会自动在pdb.set_trace()暂停并进入pdb调试环境，可以用命令p查看变量，或者用命令c继续运行：

# UnitTest
class IDict(dict):
  def __init__(self, **kw):
    super(IDict, self).__init__(**kw)

  def __getattr__(self, key):
    try:
      return self[key]
    except KeyError:
      raise AttributeError(r"'IDict' object has no attribute '%s'" % key)

  def __setattr__(self, key, value):
    self[key] = value

import unittest

class TestIDict(unittest.TestCase):
  """docstring for TestIDict"""
  def test_init(self):
    d = IDict(a=1, b='test')
    self.assertEqual(d.a, 1)
    self.assertEqual(d.b, 'test')
    self.assertTrue(isinstance(d, dict))

  def test_key(self):
    d = IDict()
    d['key'] = 'value'
    self.assertEqual(d.key, 'value')

  def test_attr(self):
    d = IDict()
    d.key = 'value'
    self.assertTrue('key' in d)
    self.assertEqual(d['key'], 'value')

  def test_keyerror(self):
    d = IDict()
    with self.assertRaises(KeyError):
      value = d['empty']

  def test_attrerror(self):
    d = IDict()
    with self.assertRaises(AttributeError):
      value = d.empty
    
if __name__ == '__main__':
  unittest.main()

# 可以在单元测试中编写两个特殊的setUp()和tearDown()方法。这两个方法会分别在每调用一个测试方法的前后分别被执行。