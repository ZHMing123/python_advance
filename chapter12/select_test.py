# _*_ coding:utf-8 _*_
# 文件作者: ZHMing123
# 开发时间：2020/5/12 15:45
# 文件名称：select_test.py
# 开发工具：PyCharm

#  1.epoll并不代表一定比select好
#  在并发高的情况下，连接活跃度（如游戏中的保持连接）不是很高，epoll比select好
#  并发性不高，同时连接很活跃，select比epoll好

# 使用非阻塞io完成http请求

import socket
from urllib.parse import urlparse


# requests --> urllib库 --> socket
# 使用非阻塞io完成http请求
def get_url(url):
    # 通过socket请求html
    url = urlparse(url)  # 将URL分解为6个片段，返回一个元组，包括协议、基地址、相对地址等等
    host = url.netloc  # 获取地址
    path = url.path
    if path == "":
        path = "/"

    # 建立socket连接
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.setblocking(False)  # 将socket设置为非阻塞. 在创建socket对象后就进行该操作.设置为非阻塞，即不等操作(连接或者接受发送数据)成功，立即返回
    try:
        client.connect((host, 80))  # connect方法本身是阻塞的，阻塞过程不会消耗cpu
    except BlockingIOError as e:
        pass  # 不等连接成功，直接往下执行代码

    # 不停地询问连接是否建立好，需要while循环不停地去检查连接状态
    # 做计算任务或者再次发起其他连接请求

    # http请求格式：
    # 请求行： 请求方法 空格 url 空格 协议版本 回车 换行
    # 请求头： key-value  回车 换行
    #         回车 换行
    # 请求数据：

    # 发送数据的前提是要连接成功，因此需要不断询问是否连接成功，成功后发送数据
    while True:
        try:
            client.send("GET {} HTTP/1.1\r\nHost:{}\r\nConnection:close\r\n\r\n".format(path, host).encode("utf-8"))
            break  # 发送数据成功则退出循环
        except OSError as e:
            pass  # 异常，则继续尝试发送，直到成功为止

    data = b""  # bytes类型，用来保存接收到的数据
    while True:
        try:  # 接受数据成功
            buf = client.recv(1024)  # 每次读取1024个字节
        except BlockingIOError as e:
            continue  # 异常，则退出次数循环，继续进行下一次询问，直到成功为止
        if buf:
            data += buf
        else:
            break  # 读取完后，退出循环

    data = data.decode("utf-8")  # 将bytes类型转为str类型

    # 去掉http响应信息，直接取正文部分
    html_data = data.split("\r\n\r\n")[1]
    print(html_data)

    client.close()


if __name__ == '__main__':
    get_url("https://www.baidu.com")


