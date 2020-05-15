# _*_ coding:utf-8 _*_
# 文件作者: ZHMing123
# 开发时间：2020/5/13 6:23
# 文件名称：async_await.py
# 开发工具：PyCharm

# python为了将语义变得更加明确，在3.5引入了async和await关键字用于定义原生的协程

import types
# from collections import Awaitable
from _collections_abc import Awaitable


# 实现了__await__方法 --> Awaitable

@types.coroutine  # 装饰器 --> 使用_GeneratorWrapper包装 --> 封装了__await__方法
def downloader_yield(url):
    yield "zhming"

async def downloader(url):
    return "zhming"

async def download_url(url):
    # dosomethings
    html = await downloader(url)
    # html = await downloader_yield(url)
    return html


if __name__ == '__main__':
    my_coroutine = download_url("https://www.baidu.com")
    # next(my_coroutine)  # 注意：async定义的协程不能使用next()来调用
    my_coroutine.send(None)