# _*_ coding:utf-8 _*_
# 文件作者: ZHMing123
# 开发时间：2020/5/9 17:43
# 文件名称：socket_client.py
# 开发工具：PyCharm

import socket
# import sys


# print(sys.getdefaultencoding())


client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("127.0.0.1", 8001))  # 发起连接请求
# client.send("Hello I am client!".encode("utf8"))

while True:
    # 发送数据
    send_data = input()
    client.send(send_data.encode("utf8"))

    # 接收数据
    recv_data = client.recv(1024)
    print(recv_data.decode("utf8"))

    # client.close()
