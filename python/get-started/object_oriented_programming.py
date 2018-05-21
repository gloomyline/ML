# -*- coding: utf-8 -*-
# @Author: Administrator
# @Date:   2018-05-16 09:47:28
# @Last Modified by:   Administrator
# @Last Modified time: 2018-05-16 11:16:59

# 在Python中，所有数据类型都可以视为对象，当然也可以自定义对象。自定义的对象数据类型就是面向对象中的类（Class）的概念。

# 访问限制
# practice: 请把下面的Student对象的gender字段对外隐藏起来，用get_gender()和set_gender()代替，并检查参数有效性：

class Student(object):
  count = 0

  def __init__(self, name, gender = 'male'):
    Student.count += 1
    self.__name = name
    self.__gender = gender

  def get_gender(self):
    return self.__gender

  def set_gender(self, gen):
    if gen != 'male' and gen != 'female':
      raise ValueError('bad gender argument')
    self.__gender = gen

# 测试:
bart = Student('Bart', 'male')
if bart.get_gender() != 'male':
    print('测试失败!')
else:
    bart.set_gender('female')
    if bart.get_gender() != 'female':
        print('测试失败!')
    else:
        print('测试成功!')

# 继承和多态
class Animal(object):
  # def __init__(self, kind = 'cat', name = 'Tom', age = 6, **kw):
  #   self.__kind = kind
  #   self.__name = name
  #   self.__age = age

  def run(self):
    # print('%s is barking!' % self.__name)
    print('Animal is running...')

# opts = { 'kind': 'dog', 'name': 'bruto', 'age': 7 }
# bruto = Animal(**opts)
# bruto.bark()
# tom = Animal()
# tom.bark()
class Dog(Animal):
  def run(self):
    print('Dog is running...')

  def eat(self):
    print('Eating meat...')

class Cat(Animal):
  def run(self):
    print('Cat is running...')

dog = Dog()
dog.run()
cat = Cat()
cat.run()

# practice: 为了统计学生人数，可以给Student类增加一个类属性，每创建一个实例，该属性自动增加：

# 测试:
if Student.count != 1:
  print('测试失败!')
else:
  bart1 = Student('Bart')
  if Student.count != 2:
    print('测试失败!')
  else:
    lisa = Student('Lisa', 'female')
    if Student.count != 3:
      print('测试失败!')
    else:
      print('Students:', Student.count)
      print('测试通过!')