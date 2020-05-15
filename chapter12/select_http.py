# _*_ coding:utf-8 _*_
# 文件作者: ZHMing123
# 开发时间：2020/5/12 16:15
# 文件名称：select_http.py
# 开发工具：PyCharm

#  1.epoll并不代表一定比select好
#  在并发高的情况下，连接活跃度（如游戏中的保持连接）不是很高，epoll比select好
#  并发性不高，同时连接很活跃，select比epoll好

# 使用select完成http请求

import socket
import time
from urllib.parse import urlparse
# import select
from selectors import DefaultSelector, EVENT_READ, EVENT_WRITE


# selectors --> 是对select的进一步封装
# DefaultSelector --> 会根据平台（windows和linux)自动选择使用poll还是epoll


# requests --> urllib库 --> socket
# 使用select + 回调 + 事件循环 --> 完成http请求
# 并发性高
# 回调模式 --> 单线程 --> 没有线程切换的开销  --> 协程也是这种回调模式
selector = DefaultSelector()

# 解决方法 --> 列表为空时（即所有url处理完后），停止事件循环
urls = []
stop = False

class Fetcher:
    # 回调函数 --> 连接成功后要做的事情
    def connected(self, key):
        selector.unregister(key.fd)  # send前先注销掉我们监控这个事件,fd是注册事件时的返回值
        self.client.send("GET {} HTTP/1.1\r\nHost:{}\r\nConnection:close\r\n\r\n".format(self.path, self.host).encode("utf-8"))

        # 注册事件 --> 监听是否接收到数据
        selector.register(self.client.fileno(), EVENT_READ, self.readable)

    def readable(self, key):

        # 注意：变readable时，并不代表数据全部接收完成了，即还不能将数据从内核空间拷贝到应用空间
        # 因此，不需要使用while循环，只要是readable（可读状态），就会继续调用回调函数来读

        # data = b""  # bytes类型，用来保存接收到的数据
        # while True:
        #     buf = self.client.recv(1024)  # 每次读取1024个字节
        #     if buf:
        #         data += buf
        #     else:
        #         break  # 读取完后，退出循环

        buf = self.client.recv(1024)  # 每次读取1024个字节
        if buf:
            self.data += buf
        else:  # buf为空，说明数据已经读完
            selector.unregister(key.fd)  # send前先注销掉我们监控这个事件,fd是注册事件时的返回值
            data = self.data.decode("utf-8")  # 将bytes类型转为str类型

            # 去掉http响应信息，直接取正文部分
            html_data = data.split("\r\n\r\n")[1]
            print(html_data)
            self.client.close()

            urls.remove(self.spider_url)  # 将已经爬取的url从urls中删除
            if not urls:  # urls为空
                global stop
                stop = True

    def get_url(self, url):
        self.spider_url = url   # 当前爬取的url
        url = urlparse(url)  # 将URL分解为6个片段，返回一个元组，包括协议、基地址、相对地址等等
        self.host = url.netloc  # 获取地址
        self.path = url.path    # 相对地址
        self.data = b""         # 存放获取到的html数据
        if self.path == "":
            self.path = "/"

        # 建立socket连接
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # 将socket设置为非阻塞. 在创建socket对象后就进行该操作.设置为非阻塞，即不等操作(连接或者接受发送数据)成功，立即返回
        self.client.setblocking(False)

        try:
            self.client.connect((self.host, 80))
        except BlockingIOError as e:
            pass

        # 注册到selector中
        # register(self, fileobj, events, data=None)
        #    fileobj --> socket的文件描述符
        #    events  --> 要监听的事件（EVENT_READ，EVENT_WRITE）
        #    data    --> 回调函数

        # 连接建立好后是要发送数据（写数据） --> 所以要监听的事件是EVENT_WRITE（是否可以写）
        selector.register(self.client.fileno(), EVENT_WRITE, self.connected)


# 事件循环，不停地请求socket的状态并调用对应的回调函数
def loop():
    # select库
    # import select
    # select.select()  # select(rlist, wlist, xlist, timeout=None)

    # 1.select本身不支持register模式，selectors是封装了select，可以支持register
    # 2.socket状态变化以后的回调是由程序员完成的，并非是系统完成

    # selector.select() --> return ready(ready是一个list) --> ready.append((key, events & key.events))
    # 其中，key = SelectorKey(fileobj, self._fileobj_lookup(fileobj), events, data)
    # 而SelectorKey = namedtuple('SelectorKey', ['fileobj', 'fd', 'events', 'data'])

    # key, mask = selector.select()
    while not stop:
        ready = selector.select()
        for key, mask in ready:
            call_back = key.data  # 回调函数放在key.data中
            call_back(key)        # 回调函数connected和readable需要传入参数key

"""
异常 --> windows平台下，select()函数传入参数为空列表时，抛异常
Traceback (most recent call last):
  File "D:/pyCode/python_advance/chapter12/select_http.py", line 119, in <module>
    loop()  # 使用select + 回调 + 事件循环 --> 完成http请求
  File "D:/pyCode/python_advance/chapter12/select_http.py", line 110, in loop
    ready = selector.select()
  File "D:\Anaconda\lib\selectors.py", line 323, in select
    r, w, _ = self._select(self._readers, self._writers, [], timeout)
  File "D:\Anaconda\lib\selectors.py", line 314, in _select
    r, w, x = select.select(r, w, w, timeout)
OSError: [WinError 10022] 提供了一个无效的参数。

解决方法 --> 列表为空时（即所有url处理完后），停止事件循环
"""

if __name__ == '__main__':
    fetcher = Fetcher()
    # fetcher.get_url("https://www.baidu.com")
    start_time = time.time()
    for i in range(20):
        url = "http://shop.projectsedu.com/goods/{}/".format(i)
        urls.append(url)
        fetcher = Fetcher()
        fetcher.get_url(url)

    loop()  # 使用select + 回调 + 事件循环 --> 完成http请求
    print("const time:{}".format(time.time() - start_time))




