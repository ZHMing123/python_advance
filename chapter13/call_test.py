# _*_ coding:utf-8 _*_
# 文件作者: ZHMing123
# 开发时间：2020/5/14 17:18
# 文件名称：call_test.py
# 开发工具：PyCharm

# call_soon、call_at、call_later、call_soon_threadsafe

import asyncio


def callback(sleep_times):
    print("sleep {} success".format(sleep_times))


def stoploop(loop):
    loop.stop()


def callback_looptime(sleep_times, loop):
    print("call time {}".format(loop.time()))
    print("sleep {} success".format(sleep_times))


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    # # 1.call_soon, 协程一运行就马上运行
    # loop.call_soon(callback, 2)       # 注册到loop中，还没开始运行
    #
    # # loop.call_soon(stoploop, loop)  # 当上面的callback运行完后，停止循环
    # loop.stop()                       # 要写这个，不然不会停止

    # # 2.call_later() --> 指定运行时间 --> 内部调用了call_at方法
    # loop.call_later(2, callback, 2)   # 2秒后运行
    # loop.call_later(1, callback, 1)   # 2秒后运行
    # loop.call_later(3, callback, 3)   # 2秒后运行
    # loop.call_later(0, callback, 4)   # 2秒后运行
    # loop.call_soon(callback, 5)       # call_soon的优先级比call_later更高

    # 3.call_at
    now = loop.time()  # 这里的时间是内部的时钟时间
    # loop.call_at(now + 2, callback, 2)
    # loop.call_at(now + 1, callback, 1)
    # loop.call_at(now + 3, callback, 3)

    loop.call_at(now + 2, callback_looptime, 2, loop)
    loop.call_at(now + 1, callback_looptime, 1, loop)
    loop.call_at(now + 3, callback_looptime, 3, loop)
    loop.call_soon(callback_looptime, 4, loop)

    # 4.call_soon_threadsafe  --> 在call_soon基础上加self._write_to_self()解决线程安全问题

    # run_forever() --> 在loop中找到函数callback,然后执行它 --> 循环不会停止
    loop.run_forever()  # callback函数不是协程，所以不能用run_until_complete()


