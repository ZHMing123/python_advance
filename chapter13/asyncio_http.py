# _*_ coding:utf-8 _*_
# 文件作者: ZHMing123
# 开发时间：2020/5/14 18:23
# 文件名称：asyncio_http.py
# 开发工具：PyCharm

import socket
import time
import asyncio
from urllib.parse import urlparse


# 回调模式 --> 编程复杂度高，同步编程的并发性不高，多线程编程间同步需要用到lock
# 需要一个可以暂停的函数，并且可以在适当的时候恢复该函数的继续执行
#    这样，我们就可以通过同步的方式去编写异步的代码，并且是在单线程内去切换任务
# --> 出现了协程：可以暂停的函数（可以先暂停的地方传入值）
# --> 生成器函数是可以暂停的

# asyncio没有提供http协议的接口 --> aiohttp提供相关功能(基于asyncio实现)
# asyncio模拟http请求


async def get_url(url):
    url = urlparse(url)
    host = url.netloc
    path = url.path
    if path == "":
        path = "/"
    # print(host, path)

    # 1.建立socket连接
    # client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # client.connect((host, 80))
    # open_connection是一个协程，return reader, writer --> StreamReader和StreamWriter
    reader, writer = await asyncio.open_connection(host, 80)  # 调用了await loop.create_connection()

    # 2.写数据（发送数据）
    # client.send("GET {} HTTP/1.1\r\nHost:{}\r\nConnection:close\r\n\r\n".format(path, host).encode("utf-8"))
    # write方法 --> 内部会调用send()
    writer.write("GET {} HTTP/1.1\r\nHost:{}\r\nConnection:close\r\n\r\n".format(path, host).encode("utf-8"))


    # 3.读数据
    # data = ""
    # while True:
    #     buf = client.recv(1024)
    #     if buf:
    #         data += buf
    #     else:
    #         break
    #
    # data = data.decode("utf-8")
    # html_data = data.split("\r\n\r\n")[1]
    # print(html_data)
    # client.close()

    all_lines = []
    # print(all_lines)
    async for raw_line in reader:  # reader --> 实现了__anext__方法，调用了yield from
        data = raw_line.decode("utf-8")
        all_lines.append(data)
    html = "\n".join(all_lines)
    # print(html)
    return html


async def main():
    tasks = []
    for i in range(20):
        url = "http://shop.projectsedu.com/goods/{}/".format(i)
        # tasks.append(asyncio.ensure_future(get_url(url)))
        tasks.append(get_url(url))

    for task in asyncio.as_completed(tasks):  # as_completed --> yield _wait_for_one()返回的是一个协程
        result = await task  # task 是一个协程，所以要用await
        print(result)

if __name__ == '__main__':
    start_time = time.time()

    loop = asyncio.get_event_loop()
    # for i in range(20):
    #     url = "http://shop.projectsedu.com/goods/{}/".format(i)
    # #     tasks.append(asyncio.ensure_future(get_url(url)))
    #     tasks.append(get_url(url))
    # loop.run_until_complete(asyncio.wait(tasks))
    # for task in tasks:
    #     print(task.result)

    loop.run_until_complete(main())

    print("cost time:{}".format(time.time() - start_time))
