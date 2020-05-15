# _*_ coding:utf-8 _*_
# 文件作者: ZHMing123
# 开发时间：2020/5/14 17:50
# 文件名称：thread_asyncio.py
# 开发工具：PyCharm

# ThreadPoolExecutor+asyncio
# 协程中不能使用阻塞io， 要使用阻塞io接口时 --> 在协程中使用多线程 --> 协程中集成阻塞io

import time
import socket

import asyncio

from concurrent.futures import ThreadPoolExecutor
from urllib.parse import urlparse


# 阻塞socket接口
def get_url(url):
    # 通过socket请求html
    url = urlparse(url)
    host = url.netloc
    path = url.path
    if path == "":
        path = "/"

    # 建立socket连接
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # client.setblocking(False)  # 设置为非阻塞
    client.connect((host, 80))

    # 非阻塞模式时，不停地询问连接是否已经建立好，需要while循环不停地检查连接状态

    client.send("GET {} HTTP/1.1\r\nHost:{}\r\nConnection:close\r\n\r\n".format(path,host).encode("utf-8"))

    data = b""
    while True:
        buf = client.recv(1024)
        if buf:
            data += buf
        else:
            break  # 读完数据后，退出循环

    data = data.decode("utf-8")
    html_data = data.split("\r\n\r\n")[1]  # 去掉响应头
    print(html_data)
    client.close()


if __name__ == '__main__':
    start_time = time.time()

    loop = asyncio.get_event_loop()
    executor = ThreadPoolExecutor(3)  # 线程池
    tasks = []
    for i in range(20):
        url = "http://shop.projectsedu.com/goods/{}/".format(i)
        # run_in_executor(线程池, 接口, 参数)
        task = loop.run_in_executor(executor, get_url, url)  # 将阻塞io接口放到loop中运行,立即返回
        tasks.append(task)

    loop.run_until_complete(asyncio.wait(tasks))

    print("cost time:{}".format(time.time() - start_time))
