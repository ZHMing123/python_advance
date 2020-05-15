# _*_ coding:utf-8 _*_
# 文件作者: ZHMing123
# 开发时间：2020/3/27 9:10
# 文件名称：web_server_demo.py
# 开发工具：PyCharm

# 不完善的web服务器示例

import socket


# 生产socket实例对象
sk = socket.socket()
# 设置端口复用，让程序退出端口立即被释放
# sk.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
# 绑定ip和端口号
sk.bind(('127.0.0.1', 8001))
# 监听,最大连接数是5
sk.listen()

# 写一个死循环，一直等待客户端的来连接
while 1:
    # 获取与客户端的连接:accept() -> (socket object, address info)
    conn, addr = sk.accept()
    print(conn, addr)
    # 接受客户端发来的消息
    data = conn.recv(2048)
    # print(data)

    # 将data(byte类型)转为str类型
    data_str = str(data, encoding='utf-8')
    print(data_str)

    # 给客户端会消息
    # conn.send(b'Hello, I am server!')

    # http响应格式
    conn.send(b'http/1.1 200 ok\r\ncontent-type:text/html; charset=utf-8\r\n\r\n')
    conn.send(b'Hello, I am server!')

    # 关闭
    conn.close()
    # sk.close()




