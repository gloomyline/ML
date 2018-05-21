# -*- coding: utf-8 -*-
# @Author: Administrator
# @Date:   2018-05-10 10:38:27
# @Last Modified by:   Administrator
# @Last Modified time: 2018-05-10 11:15:38

# ord() is a built-in global method which is used to 
# get the number of corresponding character under decimalism
n = ord('A')
print(n)
# chr() is also a build-in global method used to
# convert number to corresponding character
print(chr(n))

# '\u4e2d\u6587' is tha same as '中文'

# Python对bytes类型的数据用带b前缀的单引号或双引号表示：
x = b'ABC'

r'''
要注意区分'ABC'和b'ABC'，前者是str，后者虽然内容显示得和前者一样，

但bytes的每个字符都只占用一个字节。

以Unicode表示的str通过encode()方法可以编码为指定的bytes。

纯英文的str可以用ASCII编码为bytes，内容是一样的，含有中文的str可以用UTF-8编码为bytes。

含有中文的str无法用ASCII编码，因为中文编码的范围超过了ASCII编码的范围，Python会报错。

在bytes中，无法显示为ASCII字符的字节，用\x##显示。
'''

# 要计算str包含多少个字符，可以用len()函数：
len('ABC')
# => 3
len('中文')
# => 2

# format
r'''
%运算符就是用来格式化字符串的。
在字符串内部，%s表示用字符串替换，%d表示用整数替换，
有几个%?占位符，后面就跟几个变量或者值，顺序要对应好。如果只有一个%?，括号可以省略
格式化整数和浮点数还可以指定是否补0和整数与小数的位数
'''
print('%2d-%02d' % (3, 1))
# =>  3-01
print('%.2f' % 3.1415926)
# => 3.14
print('%2f' % 3.1415926)
# => 3.141593

# practice
# 小明的成绩从去年的72分提升到了今年的85分，请计算小明成绩提升的百分点，
# 并用字符串格式化显示出'xx.x%'，只保留小数点后1位：
s1 = 72
s2 = 85
p = (s2 - s1) / s1 * 100
print('小明的成绩去年是%d, 今年是%d, 提高了%.1f%%' % (s1, s2, p))