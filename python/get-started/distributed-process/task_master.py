# -*- coding: utf-8 -*-
# @Author: Administrator
# @Date:   2018-05-23 15:38:21
# @Last Modified by:   1211071880@qq.com
# @Last Modified time: 2018-05-23 16:54:31
import random, time, queue
from multiprocessing.managers import BaseManager
from multiprocessing import freeze_support

# 创建任务队列:
task_queue = queue.Queue()
result_queue = queue.Queue()

def create_task_queue():
  global task_queue
  return task_queue

def create_result_queue():
  global result_queue
  return result_queue

# 从BaseManager继承的QueueManager:
class QueueManager(BaseManager):
    pass

def runf():
  # 把两个Queue都注册到网络上, callable参数关联了Queue对象:
  QueueManager.register('get_task_queue', callable=create_task_queue)
  QueueManager.register('get_result_queue', callable=create_result_queue)

  # 绑定端口3333, 设置验证码'abc':
  manager = QueueManager(address=('127.0.0.1', 3333), authkey=b'abc')
  # 启动Queue:
  manager.start()
  # 获得通过网络访问的Queue对象:
  task = manager.get_task_queue()
  result = manager.get_result_queue()
  # 放几个任务进去:
  for i in range(10):
    n = random.randint(0, 10000)
    print('Put task %d...' % n)
    task.put(n)
  # 从result队列读取结果:
  print('Try get results...')
  for i in range(10):
    r = result.get(timeout=100)
    print('Result: %s' % r)
  # 关闭:
  manager.shutdown()
  print('master exit.')

if __name__ == '__main__':
  freeze_support()
  runf()