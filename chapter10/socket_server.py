# _*_ coding:utf-8 _*_
# 文件作者: ZHMing123
# 开发时间：2020/5/9 17:43
# 文件名称：socket_server.py
# 开发工具：PyCharm

# socket编程
import socket
import threading


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # AF_INET:IPv4, SOCK_STREAM:TCP
server.bind(("0.0.0.0", 8001))
server.listen()
# sock_sever, addr = server.accept()  # accept() -> (socket object, address info)

# 用多线程的方式实现多用户连接
def hand_sock(sock, addr):
    while True:
        # 获取从客户端发送的数据，一次获取1024个字节（1K=1024B）的数据
        recv_data = sock.recv(1024)  # 返回的是bytes类型
        print(recv_data.decode("utf8"))

        # 判断是否是断开连接的请求
        if recv_data.decode("utf8") == "exit":
            break

        # 发送数据
        send_data = input()
        sock.send(send_data.encode("utf8"))

    # 关闭当前连接
    sock.close()


while True:
    sock, addr = server.accept()

    # 用线程去处理新接收的连接(用户)
    client_thread = threading.Thread(target=hand_sock, args=(sock, addr))
    print(client_thread)
    client_thread.start()  # 启动线程

    # server.close()
    # sock_sever.close()
