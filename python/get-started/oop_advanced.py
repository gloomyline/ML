# -*- coding: utf-8 -*-
# @Author: Administrator
# @Date:   2018-05-16 11:18:11
# @Last Modified by:   Administrator
# @Last Modified time: 2018-05-16 16:36:20

# __slots__
# 如果我们想要限制实例的属性怎么办？比如，只允许对Student实例添加name和age属性
# 为了达到限制的目的，Python允许在定义class的时候，定义一个特殊的__slots__变量，来限制该class实例能添加的属性
# 使用__slots__要注意，__slots__定义的属性仅对当前类实例起作用，对继承的子类是不起作用的：
# 除非在子类中也定义__slots__，这样，子类实例允许定义的属性就是自身的__slots__加上父类的__slots__

# @property
# Python内置的@property装饰器就是负责把一个方法变成属性调用的：
# practice: 请利用@property给一个Screen对象加上width和height属性，以及一个只读属性resolution：
from numbers import Number
class Screen(object):
  @property
  def width(self):
    return self._width

  @width.setter
  def width(self, w):
    if not isinstance(w, Number):
      raise ValueError('width need to be a number')
    self._width = w
  
  @property
  def height(self):
    return self._height
  
  @height.setter
  def height(self, h):
    if not isinstance(h, Number):
      raise ValueError('height need to be a number')
    self._height = h

  @property
  def resolution(self):
    return self._width * self._height

# 测试:
s = Screen()
s.width = 1024
s.height = 768
print('resolution =', s.resolution)
if s.resolution == 786432:
    print('测试通过!')
else:
    print('测试失败!')
  
# 多重继承(拓扑排序)
class A(object):
  def foo(self):
    print('A foo')
  def bar(self):
    print('A bar')

class B(object):
  def foo(self):
    print('B foo')
  def bar(self):
    print('B bar')

class C1(A, B):
  pass

class C2(A, B):
  def bar(self):
      print('C2-bar')

class D(C1,C2):
  pass

if __name__ == '__main__':
  print(D.__mro__)
  d = D()
  d.foo()
  d.bar()

# 定制类
# __str__
# 这是因为直接显示变量调用的不是__str__()，而是__repr__()，两
# 者的区别是__str__()返回用户看到的字符串，而__repr__()返回程序开发者看到的字符串，
# 也就是说，__repr__()是为调试服务的。
# __getattr__ 当调用不存在的属性时，比如score，
# Python解释器会试图调用__getattr__(self, 'score')来尝试获得属性，这样，我们就有机会返回score的值
# 只有在没有找到属性的情况下，才调用__getattr__，已有的属性，比如name，不会在__getattr__中查找
class Student(object):
  """docstring for Student"""
  def __init__(self, name, score = 85):
    super(Student, self).__init__()
    self.__name = name
    self.__score = score

  def __str__(self):
    return 'Student object (name: %s)' % self.__name

  __repr__ = __str__

  def __getattr__(self, attr):
    if attr == 'score':
      return self.__score

alan = Student('Alan')
print(alan)
print(alan.score)

# __iter__
# __next__
# __getitem__
class  Fib(object):
  """docstring for  Fib"""
  def __init__(self, a = 0, b = 1):
    self.__a = a
    self.__b = b

  def __iter__(self):
    return self

  def __next__(self):
    self.__a, self.__b = self.__b, self.__a + self.__b
    if self.__a > 1000:
      raise StopIteration()
    return self.__a

  def __getitem__(self, n):
    a, b = 1, 1
    if isinstance(n, int):
      for x in range(n):
        a, b = b, a + b
      return a
    elif isinstance(n, slice):
      start = n.start or 0
      stop = n.stop
      L = []
      for x in range(stop):
        if x >= start: 
          L.append(a)
        a, b = b, a + b
      return L


for n in Fib():
  if n > 10:
    break
  print(n)

print(Fib()[4])
print(Fib()[4:10])

# __getattr__ and __call__ => chain 调用
class Chain(object):
  def __init__(self, path=''):
    self._path = path

  def __getattr__(self, path):
    return Chain('%s/%s' % (self._path, path))

  def __call__(self, fpath=''):
    return Chain('%s/%s' % (self._path, fpath))

  def __str__(self):
    return self._path

  __repr__ = __str__

# /users/:user/repos
print((Chain().status.users)('Alan').repos)

# 枚举类
r'''
当我们需要定义常量时，一个办法是用大写变量通过整数来定义，例如月份：

JAN = 1
FEB = 2
MAR = 3
...
NOV = 11
DEC = 12
好处是简单，缺点是类型是int，并且仍然是变量。

更好的方法是为这样的枚举类型定义一个class类型，

然后，每个常量都是class的一个唯一实例。Python提供了Enum类来实现这个功能：

from enum import Enum

Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))
这样我们就获得了Month类型的枚举类，可以直接使用Month.Jan来引用一个常量，或者枚举它的所有成员：

for name, member in Month.__members__.items():
  print(name, '=>', member, ',', member.value)

value属性则是自动赋给成员的int常量，默认从1开始计数。
'''
from enum import Enum, unique
Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))

# 如果需要更精确地控制枚举类型，可以从Enum派生出自定义类：
@unique
class Weekday(Enum):
  Sun = 0
  Mon = 1
  Tue = 2
  Wed = 3
  Thu = 4
  Fri = 5
  Sat = 6

for name, member in Weekday.__members__.items():
  print('%s => %s:' % (name, member))

# practice: 把Student的gender属性改造为枚举类型，可以避免使用字符串：
@unique
class Gender(Enum):
  Female = 0
  Male = 1
  Intersex = 2

class Student(object):
  def __init__(self, name, gender):
    self.name = name
    self.gender = gender
  
# 测试:
bart = Student('Bart', Gender.Male)
if bart.gender == Gender.Male:
  print('测试通过!')
else:
  print('测试失败!')

# 元类

r'''
type()函数可以查看一个类型或变量的类型，Hello是一个class，它的类型就是type，而h是一个实例，它的类型就是class Hello。

type()函数既可以返回一个对象的类型，又可以创建出新的类型，

比如，我们可以通过type()函数创建出Hello类，而无需通过class Hello(object)...的定义

要创建一个class对象，type()函数依次传入3个参数：

1. class的名称；
2. 继承的父类集合，注意Python支持多重继承，如果只有一个父类，别忘了tuple的单元素写法；
3. class的方法名称与函数绑定，这里我们把函数fn绑定到方法名hello上。

Hello = type('Hello', (object,), dict(hello=fn)) # 创建Hello class

通过type()函数创建的类和直接写class是完全一样的，因为Python解释器遇到class定义时，仅仅是扫描一下class定义的语法，然后调用type()函数创建出class。

metaclass

除了使用type()动态创建类以外，要控制类的创建行为，还可以使用metaclass。

metaclass，直译为元类，简单的解释就是：

当我们定义了类以后，就可以根据这个类创建出实例，所以：先定义类，然后创建实例。

但是如果我们想创建出类呢？那就必须根据metaclass创建出类，所以：先定义metaclass，然后创建类。

连接起来就是：先定义metaclass，就可以创建类，最后创建实例。

metaclass允许你创建类或者修改类。换句话说，你可以把类看成是metaclass创建出来的“实例”。

定义ListMetaclass，按照默认习惯，metaclass的类名总是以Metaclass结尾，以便清楚地表示这是一个metaclass：

# metaclass是类的模板，所以必须从`type`类型派生：
class ListMetaclass(type):
    def __new__(cls, name, bases, attrs):
        attrs['add'] = lambda self, value: self.append(value)
        return type.__new__(cls, name, bases, attrs)
有了ListMetaclass，我们在定义类的时候还要指示使用ListMetaclass来定制类，传入关键字参数metaclass：

class MyList(list, metaclass=ListMetaclass):
    pass
当我们传入关键字参数metaclass时，魔术就生效了，它指示Python解释器在创建MyList时，要通过ListMetaclass.__new__()来创建，在此，我们可以修改类的定义，比如，加上新的方法，然后，返回修改后的定义。

__new__()方法接收到的参数依次是：

1. 当前准备创建的类的对象；

2. 类的名字；

3. 类继承的父类集合；

4. 类的方法集合。

测试一下MyList是否可以调用add()方法：

>>> L = MyList()
>>> L.add(1)
>> L
[1]
而普通的list没有add()方法：

>>> L2 = list()
>>> L2.add(1)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'list' object has no attribute 'add'
'''