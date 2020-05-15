# _*_ coding:utf-8 _*_
# 文件作者: ZHMing123
# 开发时间：2020/3/31 8:19
# 文件名称：process_test.py
# 开发工具：PyCharm

"""
进程间通信：
    通过队列实现进程间通信，队列充当消息管道的作用（类似生产者消费者模型）
    这里通信一直存在，也就是这两个进程会一直存在，没有销毁释放。
"""
import time
import multiprocessing
from multiprocessing import Queue

class Put_news(multiprocessing.Process):
    def __init__(self, queue):
        super().__init__()
        self.queue = queue

    def run(self):
        for i in range(100):
            self.queue.put(i)
            print('传递消息：%s' %i)
            time.sleep(0.1)

class Get_news(multiprocessing.Process):
    def __init__(self, queue):
        super().__init__()
        self.queue = queue

    def run(self):
        while True:
            time.sleep(0.11)
            print('接收消息+++++++++++++++++++：%s' %(self.queue.get()))

if __name__ == '__main__':
    q = Queue()
    p = Put_news(q)
    g = Get_news(q)
    p.start()
    g.start()

    if not p.is_alive():
        g.terminate()





