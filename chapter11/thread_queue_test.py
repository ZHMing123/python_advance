# _*_ coding:utf-8 _*_
# 文件作者: ZHMing123
# 开发时间：2020/5/10 8:02
# 文件名称：thread_queue_test.py
# 开发工具：PyCharm

# 共享变量的方式不是线程安全的
# 通过queue的方式实现线程间的同步

# 线程间的通信

import time
import threading
from queue import Queue

def get_detail_html(queue):
    # 爬取文章详情页
    # global detail_url_list

    while True:
        # 队首出队（先进先出）
        url = queue.get()  # get()方法是个阻塞的方法，当队列为空时会阻塞在这里
        print("get detail html started:{url}!".format(url=url))
        time.sleep(1)
        print("get detail html ended!")

def get_detail_url(queue):
    # 爬取文章列表页
    while True:
        print("get detail url started!")
        time.sleep(2)
        for i in range(20):
            queue.put("http://www.baidu.com/{id}".format(id=i))
        print("get detail url ended!")


if __name__ == '__main__':
    # Queue -->调用了queue -->调用了deque（deque是线程安全的）
    detail_url_queue = Queue(maxsize=1000)  # Queue是线程安全的

    thread_get_detail_url = threading.Thread(target=get_detail_url, args=(detail_url_queue,))
    thread_get_detail_url.start()

    # 启动多个
    for i in range(5):
        thread_get_detail_html = threading.Thread(target=get_detail_html, args=(detail_url_queue,))
        thread_get_detail_html.start()

    start_time = time.time()

    # # 当主线程退出时，子线程kill掉(设置为守护线程)
    # thread1.setDaemon(True)
    # thread2.setDaemon(True)

    # thread1.start()
    # thread2.start()
    #
    # # 阻塞等待子线程执行完后，再执行主线程中下面的代码
    # thread1.join()
    # thread2.join()

    # # 阻塞队列直到队列为空
    # # Blocks until all items in the Queue have been gotten and processed.
    # detail_url_queue.join()
    #
    # # 退出队列阻塞
    # detail_url_queue.task_done()

    print("last time:{}".format(time.time() - start_time))

