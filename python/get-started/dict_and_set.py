# -*- coding: utf-8 -*-
# @Author: Administrator
# @Date:   2018-05-10 14:17:55
# @Last Modified by:   Administrator
# @Last Modified time: 2018-05-10 14:30:57

# dict
d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
print(d['Michael'])
# => 95

# 如果key不存在，dict就会报错：
# 要避免key不存在的错误，有两种办法，一是通过in判断key是否存在：
'Alan' in d
# => false

# 二是通过dict提供的get()方法，如果key不存在，可以返回None，或者自己指定的value：
d.get('CTT')
# => None
# 注意：返回None的时候Python的交互环境不显示结果。
print(d.get('CTT', -1))
# => -1

# set
# set和dict类似，也是一组key的集合，但不存储value。由于key不能重复，所以，在set中，没有重复的key。
# 要创建一个set，需要提供一个list作为输入集合：
s = set([1, 2, 3])
print(s)

# 重复元素在set中自动被过滤：
s1 = set([1, 1, 2, 2, 3, 3])
print(s1)
# => {1, 2, 3}

# 通过add(key)方法可以添加元素到set中
s.add(4)

# 通过remove(key)方法可以删除元素
s.remove(4)

# set可以看成数学意义上的无序和无重复元素的集合，因此，两个set可以做数学意义上的交集、并集等操作：
s2 = set([1, 2, 3])
s3 = set([2, 3, 4])
s2 & s3
# => {2, 3}
s2 | s3
# => {1, 2, 3, 4}