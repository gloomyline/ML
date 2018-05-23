# -*- coding: utf-8 -*-
# @Author: 1211071880@qq.com
# @Date:   2018-05-23 15:51:03
# @Last Modified by:   1211071880@qq.com
# @Last Modified time: 2018-05-23 16:56:01
import time, sys, queue
from multiprocessing.managers import BaseManager

# 创建类似的 QueueManager
class QueueManager(BaseManager):
  pass

# 由于这个 QueueManager 是从网络上获取的，所以注册时只需提供名字
QueueManager.register('get_task_queue')
QueueManager.register('get_result_queue')

# 链接到服务器，也就是运行 task_master.py 的机器
server_addr = '127.0.0.1'
print('Connect to server %s' % server_addr)

# 端口和验证码注意保持与 task_master.py 设置的完全一致：
m = QueueManager(address=(server_addr, 3333), authkey=b'abc')

# 从网络连接
m.connect()

# 获取 Queue 对象
task_queue = m.get_task_queue()
result_queue = m.get_result_queue()

# 从 task 队列取任务，并把结果写入 result 队列
for i in range(10):
  try:
    n = task_queue.get(timeout=1)
    print('run task %d * %d...' % (n, n))
    r = '%d * %d = %d' % (n, n, n * n)
    time.sleep(1)
    result_queue.put(r)
  except queue.Empty:
    print('task queue is empty.')
# 结束
print('worker exit.')