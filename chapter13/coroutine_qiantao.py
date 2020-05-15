# _*_ coding:utf-8 _*_
# 文件作者: ZHMing123
# 开发时间：2020/5/13 21:41
# 文件名称：coroutine_qiantao.py
# 开发工具：PyCharm

import time
import asyncio


# 协程嵌套

# run_until_complete()函数
# loop = asyncio.get_event_loop()
# loop.run_until_complete()  # Run until the Future is done --> 调用add_done_callback --> 回调函数调用futures._get_loop(fut).stop()
# loop.run_forever()  # Run until stop() is called


# 1.loop会被放到future中
# 2.取消future(task)

async def get_html(sleep_times):
    print("waiting")
    await asyncio.sleep(sleep_times)
    print("done after {}s".format(sleep_times))

# 协程嵌套
async def compute(x, y):
    print("Compute %s + %s..." %(x, y))
    await asyncio.sleep(1.0)
    return x + y  # 协程运行完后，会抛异常StopIteration，同时返回x+y的值

async def print_sum(x, y):
    result = await compute(x, y)  # await相当于yield from，所以Task和compute直接建立双向通道，print_sum类似于委托生成器
    print("%s + %s = %s" %(x, y, result))


if __name__ == '__main__':
    # task1 = get_html(2)
    # task2 = get_html(3)
    # task3 = get_html(3)
    #
    # tasks = [task1, task2, task3]
    #
    # loop = asyncio.get_event_loop()
    #
    # try:
    #     loop.run_until_complete(asyncio.wait(tasks))
    # except KeyboardInterrupt as e:  # ctrl + c
    #     # all_tasks() --> 调用了loop = events.get_event_loop()来获取当前的事件循环loop
    #     all_tasks = asyncio.Task.all_tasks()  # 获取所有task
    #     for task in all_tasks:
    #         print("cancel task")
    #         print(task.cancel())
    #     loop.stop()
    #     loop.run_forever()  # cancel后要调用loop.run_forever()，否则将抛异常
    # finally:
    #     loop.close()


    # 协程中嵌套协程
    loop = asyncio.get_event_loop()
    loop.run_until_complete(print_sum(1, 2))
    loop.close()


