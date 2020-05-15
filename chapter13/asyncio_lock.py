# _*_ coding:utf-8 _*_
# 文件作者: ZHMing123
# 开发时间：2020/5/14 21:51
# 文件名称：asyncio_lock.py
# 开发工具：PyCharm

# asyncio同步和通信

# import asyncio
#
#
# total = 0
#
# async def add():
#     global total
#     for i in range(1000000):
#         total += 1
#
#
# async def desc():
#     global total
#     for i in range(1000000):  # 由于不涉及io操作，所以协程也是运行完整段代码，再运行下一个协程
#         total -= 1
#
#
# if __name__ == '__main__':
#     tasks = [add(), desc()]
#     loop = asyncio.get_event_loop()
#     loop.run_until_complete(asyncio.wait(tasks))
#
#     print(total)

import asyncio
import aiohttp
from asyncio import Lock, Queue

# aiohttp --> 可以看成是requests的异步版本

cache = {}
lock = Lock()  # 这里的Lock()不是真正的锁，而是一个变量self._lock = True，因为协程是一个单线程


async def get_stuff(url):
    # await lock.acquire()  # lock.acquire()是一个协程，所以要用await
    # 实现了__enter__和__exit__方法 --> with await lock:
    #     asyncio语法：实现了__aenter__和__await__、__aexit__方法async with lock:
    # with await lock:
    async with lock:
        if url in cache:
            return cache[url]
        stuff = await aiohttp.request("GET", url)
        cache[url] = stuff
        return stuff


async def parse_stuff():
    stuff = await get_stuff()
    # do some parsing


async def use_stuff():
    stuff = await get_stuff()
    # use stuff to do something others


if __name__ == '__main__':
    # 两个协程都会调用的 get_stuff() --> 加锁同步
    tasks = [parse_stuff(), use_stuff()]

