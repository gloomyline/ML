# -*- coding: utf-8 -*-
# @Author: Administrator
# @Date:   2018-05-17 14:26:03
# @Last Modified by:   Administrator
# @Last Modified time: 2018-05-17 14:30:59
import json

obj = dict(name='小明', age=20)
s = json.dumps(obj, ensure_ascii=True)
print(s)