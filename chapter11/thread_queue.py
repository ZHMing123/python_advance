# _*_ coding:utf-8 _*_
# 文件作者: ZHMing123
# 开发时间：2020/5/10 7:42
# 文件名称：thread_queue.py
# 开发工具：PyCharm

# 线程间的通信

import time
import threading

# 1.线程通信方式-共享变量(全局变量)
detail_url_list = []

def get_detail_html(detail_url_list):
    # 爬取文章详情页
    # global detail_url_list

    while True:
        if len(detail_url_list):  # 判断当前队列是否为空
            url = detail_url_list.pop()  # 队列尾部弹出(不是线程安全的)
            # for url in detail_url_list:
            print("get detail html started:{url}!".format(url=url))
            time.sleep(1)
            print("get detail html ended!")

def get_detail_url(detail_url_list):
    # 爬取文章列表页
    # global detail_url_list
    while True:
        if len(detail_url_list) == 0:
            print("get detail url started!")
            time.sleep(2)
            for i in range(20):
                detail_url_list.append("http://www.baidu.com/{id}".format(id=i))
            print("get detail url ended!")

# 1.线程通信方式-共享变量


if __name__ == '__main__':
    thread_get_detail_url = threading.Thread(target=get_detail_url, args=(detail_url_list,))
    thread_get_detail_url.start()

    # 启动多个
    for i in range(5):
        thread_get_detail_html = threading.Thread(target=get_detail_html, args=(detail_url_list,))
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

    print("last time:{}".format(time.time() - start_time))
