# -*- coding: utf-8 -*-
# @Author: Administrator
# @Date:   2018-05-17 15:29:32
# @Last Modified by:   Administrator
# @Last Modified time: 2018-05-17 15:41:05
import os, time, random
from multiprocessing import Pool

# tasks excute in child processes
def long_time_task(name):
  print('Run task %s, pid is %s' % (name, os.getpid()))
  start = time.time()
  # simulate doing some things here
  time.sleep(random.random() * 3)
  end = time.time()
  print('Task %s runs %0.2f seconds' % (name, end - start))

if __name__ == '__main__':
  print('Parent process %s' % os.getpid())
  p = Pool(4)
  for x in range(5):
    p.apply_async(long_time_task, args=(x,))
  print('Waiting for all subprocesses done...')
  p.close()
  p.join()
  print('All subprocesses done')