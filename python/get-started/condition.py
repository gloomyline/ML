# -*- coding: utf-8 -*-
# @Author: Administrator
# @Date:   2018-05-10 11:34:22
# @Last Modified by:   Administrator
# @Last Modified time: 2018-05-10 11:55:24
import math

age = 6
print('Your age is', age)
if age >= 18:
  print('adult')
elif age >= 6:
  print('teenager')
else:
  print('kid')

# if语句执行有个特点，它是从上往下判断，
# 如果在某个判断上是True，把该判断对应的语句执行后，就忽略掉剩下的elif和else

birth = input('birth: ')
birth_year = int(birth)
if birth_year >= 2000:
  print('00后')
elif birth_year >= 1990:
  print('90后')
else:
  print('Sorry, you are too old.')

# practice
# 小明身高1.75，体重80.5kg。请根据BMI公式（体重除以身高的平方）帮小明计算他的BMI指数，
# 并根据BMI指数
# 低于18.5：过轻
# 18.5-25：正常
# 25-28：过重
# 28-32：肥胖
# 高于32：严重肥胖

h = 1.75
w = 80.5
BMI = w / math.pow(h, 2)

if BMI < 18.5:
  print('过轻')
elif BMI <= 25:
  print('正常')
elif BMI <= 28:
  print('过重')
elif BMI <= 32:
  print('肥胖')
else:
  print('严重肥胖')