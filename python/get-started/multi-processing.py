# -*- coding: utf-8 -*-
# @Author: Administrator
# @Date:   2018-05-17 14:47:36
# @Last Modified by:   Administrator
# @Last Modified time: 2018-05-17 16:18:50
import os, time, random
import subprocess
from multiprocessing import Process, Pool

# 子进程要执行的代码
def run_proc(name):
  print('Run child process %s (%s)...' % (name, os.getpid()))

r'''
if __name__=='__main__':
  print('Parent process %s.' % os.getpid())
  p = Process(target=run_proc, args=('test',))
  print('Child process will start.')
  p.start()
  p.join()
  print('Child process end.')
'''

r'''
创建子进程时，只需要传入一个执行函数和函数的参数，
创建一个Process实例，用start()方法启动，这样创建进程比fork()还要简单。

join()方法可以等待子进程结束后再继续往下运行，通常用于进程间的同步。
'''

# Pool
# 如果要启动大量的子进程，可以用进程池的方式批量创建子进程：

def long_time_task(name):
  print('Run task %s, pid is %s...' % (name, os.getpid()))
  start = time.time()
  time.sleep(random.random() * 5)
  end = time.time()
  print('Task %s runs %0.2f seconds' % (name, end - start))

r'''
if __name__ == '__main__':
  print('Process %s' % os.getpid())
  p = Pool(4)
  for x in range(5):
    p.apply_async(long_time_task, args=('test_' + str(x),))
  print('Waiting all subprocesses...')
  p.close()
  p.join()
  print('All subprocesses done')
'''

r'''
对Pool对象调用join()方法会等待所有子进程执行完毕，
调用join()之前必须先调用close()，调用close()之后就不能继续添加新的Process了。
'''

# 子进程
r'''
子进程并不是自身，而是一个外部进程。我们创建了子进程后，还需要控制子进程的输入和输出。

subprocess模块可以让我们非常方便地启动一个子进程，然后控制其输入和输出。
'''
# print('$ nslookup www.python.org')
# r = subprocess.call(['nslookup', 'www.python.org'])
# print('Exit code:', r)

# 运行结果
r'''
$ nslookup www.python.org
Non-authoritative answer:

Server:  FJ-DNS.xm.fj.cn
Address:  218.85.152.99

DNS request timed out.
    timeout was 2 seconds.
Name:    dualstack.python.map.fastly.net
Address:  151.101.228.223
Aliases:  www.python.org

Exit code: 0
'''

# 如果子进程还需要输入，则可以通过communicate()方法输入：
print('$ nslookup')
p = subprocess.Popen(['nslookup'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
output, err = p.communicate(b'set q=mx\npython.org\nexit\n')
print(output.decode('utf-8'))
print('Exit code:', p.returncode)