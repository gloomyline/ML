# -*- coding: utf-8 -*-
# @Author: Administrator
# @Date:   2018-05-10 11:16:20
# @Last Modified by:   Administrator
# @Last Modified time: 2018-05-10 11:33:27

# list
# list is an ordered set, the elements can be added and deleted whenever
class_mates = ['Alan', 'Ting', 'Lebron']
print(class_mates)
# => ['Alan', 'Ting', 'Lebron']

print(len(class_mates))
# => 3

class_mates.append('Pepa')
print(class_mates)
# =>　['Alan', 'Ting', 'Lebron', 'Pepa']

class_mates.insert(1, 'John')
print(class_mates)
# => ['Alan', 'John', 'Ting', 'Lebron', 'Pepa']

class_mates.pop()
print(class_mates)
# => ['Alan', 'John', 'Ting', 'Lebron']

class_mates.pop(1)
print(class_mates)
# => ['Alan', 'Ting', 'Lebron']

# tuple
# tuple和list非常类似，但是tuple一旦初始化就不能修改
# 只有1个元素的tuple定义时必须加一个逗号,，来消除歧义
# tuple所谓的“不变”是说，tuple的每个元素，指向永远不变
# 

# practice
# 请用索引取出下面list的指定元素：
L = [
    ['Apple', 'Google', 'Microsoft'],
    ['Java', 'Python', 'Ruby', 'PHP'],
    ['Adam', 'Bart', 'Lisa']
]
# 打印Apple:
print(L[0][0])

# 打印Python:
print(L[1][1])

# 打印Lisa:
print(L[2][2])