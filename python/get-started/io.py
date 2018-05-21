# -*- coding: utf-8 -*-
# @Author: Administrator
# @Date:   2018-05-17 11:24:16
# @Last Modified by:   Administrator
# @Last Modified time: 2018-05-17 14:22:33

# 读文件
'''
要以读文件的模式打开一个文件对象，使用Python内置的open()函数，传入文件名和标示符
>>> f = open('/Users/Alan/test.txt', 'r')
标示符'r'表示读，这样，我们就成功地打开了一个文件。
'''

# 写文件
# 写文件和读文件是一样的，唯一区别是调用open()函数时，
# 传入标识符'w'或者'wb'表示写文本文件或写二进制文件：
# >>> f = open('/Users/Alan/test.txt', 'w')

# StringIO
# StringIO顾名思义就是在内存中读写str。
r'''
要把str写入StringIO，我们需要先创建一个StringIO，然后，像文件一样写入即可
>>> from io import StringIO
>>> f = StringIO()
>>> f.write('hello')
5
>>> f.write(' ')
1
>>> f.write('world!')
6
>>> print(f.getvalue())
hello world!

getvalue()方法用于获得写入后的str。

要读取StringIO，可以用一个str初始化StringIO，然后，像读文件一样读取：

>>> from io import StringIO
>>> f = StringIO('Hello!\nHi!\nGoodbye!')
>>> while True:
...     s = f.readline()
...     if s == '':
...         break
...     print(s.strip())
...
Hello!
Hi!
Goodbye!
'''

# BytesIO
r'''
StringIO操作的只能是str，如果要操作二进制数据，就需要使用BytesIO。

BytesIO实现了在内存中读写bytes，我们创建一个BytesIO，然后写入一些bytes：

>>> from io import BytesIO
>>> f = BytesIO()
>>> f.write('中文'.encode('utf-8'))
6
>>> print(f.getvalue())
b'\xe4\xb8\xad\xe6\x96\x87'

注意，写入的不是str，而是经过UTF-8编码的bytes。

和StringIO类似，可以用一个bytes初始化BytesIO，然后，像读文件一样读取：

>>> from io import BytesIO
>>> f = BytesIO(b'\xe4\xb8\xad\xe6\x96\x87')
>>> f.read()
b'\xe4\xb8\xad\xe6\x96\x87'
'''

# 操作文件和目录
r'''
操作文件和目录的函数一部分放在os模块中，一部分放在os.path模块中，这一点要注意一下

# 查看当前目录的绝对路径:
>>> os.path.abspath('.')
'/Users/michael'
# 在某个目录下创建一个新目录，首先把新目录的完整路径表示出来:
>>> os.path.join('/Users/michael', 'testdir')
'/Users/michael/testdir'
# 然后创建一个目录:
>>> os.mkdir('/Users/michael/testdir')
# 删掉一个目录:
>>> os.rmdir('/Users/michael/testdir')

把两个路径合成一个时，不要直接拼字符串，
而要通过os.path.join()函数，这样可以正确处理不同操作系统的路径分隔符

同样的道理，要拆分路径时，也不要直接去拆字符串，
而要通过os.path.split()函数，这样可以把一个路径拆分为两部分，后一部分总是最后级别的目录或文件名：

os.path.splitext()可以直接让你得到文件扩展名，很多时候非常方便：

shutil模块提供了copyfile()的函数，你还可以在shutil模块中找到很多实用函数，它们可以看做是os模块的补充

最后看看如何利用Python的特性来过滤文件。比如我们要列出当前目录下的所有目录，只需要一行代码
>>> [x for x in os.listdir('.') if os.path.isdir(x)]
['.lein', '.local', '.m2', '.npm', '.ssh', '.Trash', '.vim', 'Applications', 'Desktop', ...]

要列出所有的.py文件，也只需一行代码：
>>> [x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1] == '.py']
'''

# 序列化

r'''
在程序运行的过程中，所有的变量都是在内存中，比如，定义一个dict：

d = dict(name='Bob', age=20, score=88)

可以随时修改变量，比如把name改成'Bill'，但是一旦程序结束，变量所占用的内存就被操作系统全部回收

如果没有把修改后的'Bill'存储到磁盘上，下次重新运行程序，变量又被初始化为'Bob'。

我们把变量从内存中变成可存储或传输的过程称之为序列化，在Python中叫pickling，
在其他语言中也被称之为serialization，marshalling，flattening等等，都是一个意思。

反过来，把变量内容从序列化的对象重新读到内存里称之为反序列化，即unpickling。

Python提供了pickle模块来实现序列化。

首先，我们尝试把一个dict序列化并写入文件

>>> import pickle
>>> d = dict(name='CTT', age=26, gender='female')
>>> pickle.dumps(d)
b'\x80\x03}q\x00(X\x04\x00\x00\x00nameq\x01X\x03\x00\x00\x00CTTq\x02X\x03\x00\x0
0\x00ageq\x03K\x1aX\x06\x00\x00\x00genderq\x04X\x06\x00\x00\x00femaleq\x05u.'

pickle.dumps()方法把任意对象序列化成一个bytes，然后，就可以把这个bytes写入文件。
或者用另一个方法pickle.dump()直接把对象序列化后写入一个file-like Object：

>>> with open('/Users/CTT/dump.txt', 'wb') as f:
...   pickle.dump(d, f)

当我们要把对象从磁盘读到内存时，可以先把内容读到一个bytes，然后用pickle.loads()方法反序列化出对象，
也可以直接用pickle.load()方法从一个file-like Object中直接反序列化出对象

>>> with open('/Users/CTT/dump.txt', 'rb') as f:
...   d1 = pickle.load(f)
...
>>> d1
{'name': 'CTT', 'age': 26, 'gender': 'female'}

变量的内容又回来了！

当然，这个变量和原来的变量是完全不相干的对象，它们只是内容相同而已。

# 注意：Pickle的问题和所有其他编程语言特有的序列化问题一样，
就是它只能用于Python，并且可能不同版本的Python彼此都不兼容，
因此，只能用Pickle保存那些不重要的数据，不能成功地反序列化也没关系。
'''

# JSON
r'''
如果我们要在不同的编程语言之间传递对象，就必须把对象序列化为标准格式，比如XML，
但更好的方法是序列化为JSON，因为JSON表示出来就是一个字符串，
可以被所有语言读取，也可以方便地存储到磁盘或者通过网络传输。
JSON不仅是标准格式，并且比XML更快，而且可以直接在Web页面中读取，非常方便。

JSON表示的对象就是标准的JavaScript语言的对象，JSON和Python内置的数据类型对应如下：

JSON类型      Python类型
{}            dict
[]            list
"string"      str
1234.56       int或float
true/false    True/False
null          None

Python内置的json模块提供了非常完善的Python对象到JSON格式的转换。我们先看看如何把Python对象变成一个JSON
'''
import json
d = dict(name='CTT', age=26, gender='female')
jd = json.dumps(d)
print('json化后str: %s' % jd)

r'''
dumps()方法返回一个str，内容就是标准的JSON。类似的，dump()方法可以直接把JSON写入一个file-like Object。

要把JSON反序列化为Python对象，用loads()或者对应的load()方法，
前者把JSON的字符串反序列化，后者从file-like Object中读取字符串并反序列化

由于JSON标准规定JSON编码是UTF-8，所以我们总是能正确地在Python的str与JSON的字符串之间转换。
'''
print('反json化后：%s' % json.loads(jd))

# JSON进阶
r'''

'''