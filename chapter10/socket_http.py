# _*_ coding:utf-8 _*_
# 文件作者: ZHMing123
# 开发时间：2020/5/9 22:16
# 文件名称：socket_http.py
# 开发工具：PyCharm

# socket模拟http请求
# requests --> urlib库 --> socket

import socket
from urllib.parse import urlparse


def get_url(url):
    # 通过socket请求html
    url = urlparse(url)  # 将URL分解为6个片段，返回一个元组，包括协议、基地址、相对地址等等
    host = url.netloc  # 地址（域名）
    path = url.path   # 相对路径
    if path == "":
        path = "/"

    # 建立socket连接
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((host, 80))  # http默认是80端口

    # http请求格式：
    # 请求行： 请求方法 空格 url 空格 协议版本 回车 换行
    # 请求头： key-value  回车 换行
    #         回车 换行
    # 请求数据：
    client.send("GET {} HTTP/1.1\r\nHost:{}\r\nConnection:close\r\n\r\n".format(path, host).encode("utf-8"))

    data = b""  # bytes类型
    while True:
        d = client.recv(1024)
        if d:
            data += d
        else:
            break

    data = data.decode("utf-8")
    # 去掉http响应信息，直接取正文部分
    html_data = data.split("\r\n\r\n")[1]
    print(html_data)

    client.close()


if __name__ == '__main__':
    import time
    start_time = time.time()
    for i in range(20):
        url = "http://shop.projectsedu.com/goods/{}/".format(i)
        get_url(url)

    print("const time:{}".format(time.time() - start_time))
