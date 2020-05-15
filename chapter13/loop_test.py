# _*_ coding:utf-8 _*_
# 文件作者: ZHMing123
# 开发时间：2020/5/13 7:13
# 文件名称：loop_test.py
# 开发工具：PyCharm

# 事件循环 + 回调（在协程中就是驱动生成器）+ epoll（IO多路复用）
# asyncio是python用于解决异步编程的一整套解决方案
# tarnado、gevent、twisted(scrapy、django channels)
# torando(实现web服务器), django+flask(uwsgi,gunicorn+nginx)
# torando可以直接部署，nginx+tornado

# 使用asyncio
import time
import asyncio
from functools import partial


# partial 函数的功能就是：把一个函数的某些参数给固定住，返回一个新的函数

async def get_html(url):
    print("start get url")
    # await time.sleep()  # 不要用time.sleep() --> 因为这是同步阻塞的接口，不能使用在协程中
    await asyncio.sleep(2)  # 异步，返回一个future对象，继续往下执行
    # time.sleep(2)  # 同步任务，执行完这行代码在继续往下执行，10任务要20秒
    print("end get url")
    return "zhming@"

def callback(url, future):
    print("url:{}".format(url))
    print("send email to zhming@qq.com")

if __name__ == '__main__':
    start_time = time.time()

    # 1.获取一个事件循环
    loop = asyncio.get_event_loop()

    # tasks = [get_html("http://www.baidu.com") for i in range(50)]
    # loop.run_until_complete(asyncio.wait(tasks))

    # 2.获取事件结果
    # 两种创建Task实例的方式，asyncio.ensure_future和loop.create_task(python3.7以后的版本支持asyncio.create_task)。

    # 方式一：asyncio.ensure_future --> 调用了task = loop.create_task(coro_or_future)
    # get_future = asyncio.ensure_future(get_html("http://www.baidu.com"))
    # loop.run_until_complete(get_future)
    # print(get_future.result())

    # 方式二：loop.create_task
    # Task是Future的一个子类，asyncio.ensure_future和loop.create_task两者功能和用法类似
    # task = loop.create_task(get_html("http://www.baidu.com"))
    # loop.run_until_complete(task)
    # print(task.result())

    # # 3.添加回调函数
    # # task.add_done_callback(callback)  # 调用时会将task（future对象）传递到回调函数中
    # task.add_done_callback(partial(callback, "http://www.baidu.com"))  # partial:返回一个函数
    # loop.run_until_complete(task)
    # print(task.result())

    # 4.wait和gather
    # tasks = [get_html("http://www.baidu.com") for i in range(20)]
    # # wait是一个协程 --> async def wait(fs, *, loop=None, timeout=None, return_when=ALL_COMPLETED):
    # loop.run_until_complete(asyncio.wait(tasks))

    # tasks = [get_html("http://www.baidu.com") for i in range(50)]
    # # gather --> def gather(*coros_or_futures, loop=None, return_exceptions=False):
    # loop.run_until_complete(asyncio.gather(*tasks))

    # wait和gather的区别：
    # gather更加高级
    # gather可以分组 --> 实现批量操作
    group1 = [get_html("http://www.baidu.com") for i in range(2)]
    group2 = [get_html("http://www.baidu.com") for i in range(2)]
    group1 = asyncio.gather(*group1)
    group2 = asyncio.gather(*group2)

    # group2.cancel()  # 批量取消任务
    loop.run_until_complete(asyncio.gather(group1, group2))


    print("cost time:{}".format(time.time() - start_time))

