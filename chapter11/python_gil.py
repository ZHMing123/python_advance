# _*_ coding:utf-8 _*_
# 文件作者: ZHMing123
# 开发时间：2020/5/9 22:47
# 文件名称：python_gil.py
# 开发工具：PyCharm

# python中的GIL(global interpreter lock)全局解释器锁 --> cpython
# python中的一个线程对应于c语言中的一个线程
# GIL使得同一时刻只能有一个线程在某-个cpu上执行字节码，无法将多个线程映射到多个CPU上

# GIL会根据执行的字节码行数（100行）以及时间片（0.5秒）释放GIL, 或者在遇到io操作时主动释放

import dis
import threading

# def add(a):
#     a += 1
#     return a
#
# print(dis.dis(add))


total = 0

def add():
    global total
    for i in range(1000000):
        total += 1


def desc():
    global total
    for i in range(1000000):
        total -= 1


if __name__ == '__main__':
    thread1 = threading.Thread(target=add)
    thread2 = threading.Thread(target=desc)

    thread1.start()
    thread2.start()

    # 等待线程thread1和thread2执行完毕
    thread1.join()
    thread2.join()

    print(total)

