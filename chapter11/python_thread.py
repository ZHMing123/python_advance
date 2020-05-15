# _*_ coding:utf-8 _*_
# 文件作者: ZHMing123
# 开发时间：2020/5/10 7:13
# 文件名称：python_thread.py
# 开发工具：PyCharm

# 对于io操作来说，多线程和多线程性能差别不大

import time
import threading

# 1.通过Thread类实例化
def get_detail_html(url):
    print("get detail html started!")
    time.sleep(2)
    print("get detail html ended!")

def get_detail_url(url):
    print("get detail url started!")
    time.sleep(2)
    print("get detail url ended!")


# 2.通过继承Thread类来实现多线程，需要重写run方法
class GetDetailHtml(threading.Thread):
    def __init__(self, thread_name):
        super().__init__(name=thread_name)  # 调用父类的__init__方法

    def run(self):
        print("get detail html started!")
        time.sleep(2)
        print("get detail html ended!")


class GetDetailUrl(threading.Thread):
    def __init__(self, thread_name):
        super().__init__(name=thread_name)  # 调用父类的__init__方法

    def run(self):
        print("get detail url started!")
        time.sleep(4)
        print("get detail url ended!")


if __name__ == '__main__':
    # 1.通过Thread类实例化
    # thread1 = threading.Thread(target=get_detail_html, args=("",))
    # thread2 = threading.Thread(target=get_detail_url, args=("",))

    # 2.通过继承Thread类来实现多线程，需要重写run方法
    thread1 = GetDetailHtml("get_detail_html")
    thread2 = GetDetailUrl("get_detail_url")

    start_time = time.time()

    # # 当主线程退出时，子线程kill掉(设置为守护线程)
    # thread1.setDaemon(True)
    # thread2.setDaemon(True)

    thread1.start()
    thread2.start()

    # 阻塞等待子线程执行完后，再执行主线程中下面的代码
    thread1.join()
    thread2.join()

    print("last time:{}".format(time.time() - start_time))
