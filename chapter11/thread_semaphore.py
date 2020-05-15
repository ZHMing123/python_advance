# _*_ coding:utf-8 _*_
# 文件作者: ZHMing123
# 开发时间：2020/5/10 22:44
# 文件名称：thread_semaphore.py
# 开发工具：PyCharm

# Semaphore(信号量) --> 用于控制进入数量的锁
# Semaphore(信号量) --> 内部调用了Condition
# Queue --> 线程安全的(内部调用了Condition)
import time
import threading


# 模拟爬虫
class HtmlSpider(threading.Thread):
    def __init__(self, url, semaphore):
        super().__init__()
        self.url = url
        self.semaphore = semaphore

    def run(self):
        time.sleep(2)
        print("got html text success!")
        self.semaphore.release()  # 释放锁


class UrlProducer(threading.Thread):
    def __init__(self, semaphore):
        super().__init__()
        self.semaphore = semaphore

    def run(self):
        for i in range(20):
            self.semaphore.acquire()  # 获取锁
            html_thead = HtmlSpider("https://www.baidu.com/{}".format(i), self.semaphore)
            html_thead.start()


if __name__ == '__main__':
    semaphore = threading.Semaphore(3)  # 调用acquire()计数减1，调用realese()计数加1

    url_producer = UrlProducer(semaphore)
    url_producer.start()



