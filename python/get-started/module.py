# -*- coding: utf-8 -*-
# @Author: Administrator
# @Date:   2018-05-16 09:18:37
# @Last Modified by:   Administrator
# @Last Modified time: 2018-05-16 09:46:44

' a test module '

__author__ = 'AlanWang'

import sys

def test():
  args = sys.argv
  print(args)
  if len(args) == 1:
    print('Hello, World!')
  elif len(args) == 2:
    print('Hello, %s' % args[1])
  else:
    print('Too many arguments.')

if __name__ == '__main__':
  test()

# 作用域
r'''
在一个模块中，我们可能会定义很多函数和变量，但有的函数和变量我们希望给别人使用，
有的函数和变量我们希望仅仅在模块内部使用。在Python中，是通过_前缀来实现的
正常的函数和变量名是公开的（public），可以被直接引用，比如：abc，x123，PI等
类似__xxx__这样的变量是特殊变量，可以被直接引用，但是有特殊用途，比如上面的__author__，__name__就是特殊变量
hello模块定义的文档注释也可以用特殊变量__doc__访问，我们自己的变量一般不要用这种变量名；
类似_xxx和__xxx这样的函数或变量就是非公开的（private），不应该被直接引用，比如_abc，__abc等；
之所以我们说，private函数和变量“不应该”被直接引用，而不是“不能”被直接引用，
是因为Python并没有一种方法可以完全限制访问private函数或变量，但是，从编程习惯上不应该引用private函数或变量。
'''

def _private_1(name):
  return 'Hello %s' % name

def _private_2(name):
  return 'Hi %s' % name

def greeting(name):
  if len(name) > 3:
    return _private_1(name)
  else:
    return _private_2(name)

r'''
我们在模块里公开greeting()函数，而把内部逻辑用private函数隐藏起来了，

这样，调用greeting()函数不用关心内部的private函数细节，这也是一种非常有用的代码封装和抽象的方法，即：

外部不需要引用的函数全部定义成private，只有外部需要引用的函数才定义为public。
'''

# 模块搜索路径
r'''
默认情况下，Python解释器会搜索当前目录、所有已安装的内置模块和第三方模块，搜索路径存放在sys模块的path变量中：

如果我们要添加自己的搜索目录，有两种方法：

一是直接修改sys.path，添加要搜索的目录：

>>> import sys
>>> sys.path.append('/Users/michael/my_py_scripts')
这种方法是在运行时修改，运行结束后失效。

第二种方法是设置环境变量PYTHONPATH，该环境变量的内容会被自动添加到模块搜索路径中。

设置方式与设置Path环境变量类似。注意只需要添加你自己的搜索路径，Python自己本身的搜索路径不受影响

'''