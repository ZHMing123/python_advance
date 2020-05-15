# _*_ coding:utf-8 _*_
# 文件作者: ZHMing123
# 开发时间：2020/5/10 20:55
# 文件名称：thread_sync.py
# 开发工具：PyCharm

# 线程同步(Lock、RLock、Semaphores、Conditon)

# python中的GIL(global interpreter lock)全局解释器锁 --> cpython
# python中的一个线程对应于c语言中的一个线程
# GIL使得同一时刻只能有一个线程在某-个cpu上执行字节码，无法将多个线程映射到多个CPU上

# GIL会根据执行的字节码行数（100行）以及时间片（0.5秒）释放GIL, 或者在遇到io操作时主动释放

import dis
import threading
from threading import Lock, RLock

# def add(a):
#     a += 1
#     return a
#
# print(dis.dis(add))


total = 0
# lock = Lock()

# RLock-->可重入锁，在同一个线程里面，可以多次acquire()，但release()次数要与acquire()相同
lock = RLock()

def add():
    global total
    for i in range(1000000):
        lock.acquire()  # 获取锁
        lock.acquire()
        total += 1
        lock.release()  # 释放锁
        lock.release()  # 释放锁


def desc():
    global total
    for i in range(1000000):
        lock.acquire()  # 获取锁
        total -= 1
        lock.release()  # 释放锁


def add1(a):
    a += 1

def desc1(a):
    a -= 1

"""
分为4步：(并非是原子操作，所以可能在这4步中的某一步出现GIL释放和线程切换问题)
    1. load a
    2. load 1
    3. 执行+操作
    4. 赋值给a
"""

# import dis
# print(dis.dis(add1))
# print(dis.dis(desc1))

# 用锁会影响性能，锁的获取和释放需要花费时间
# 锁会引起死锁，例如连续两次 lock.acquire()：
#         lock.acquire()  # 获取锁
#         lock.acquire()  # 获取锁


if __name__ == '__main__':
    thread1 = threading.Thread(target=add)
    thread2 = threading.Thread(target=desc)

    thread1.start()
    thread2.start()

    # 等待线程thread1和thread2执行完毕
    thread1.join()
    thread2.join()

    print(total)

