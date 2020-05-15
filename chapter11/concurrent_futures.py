# _*_ coding:utf-8 _*_
# 文件作者: ZHMing123
# 开发时间：2020/5/11 17:17
# 文件名称：concurrent_futures.py
# 开发工具：PyCharm

# concurrent线程池编程

import time
from concurrent.futures import ThreadPoolExecutor, as_completed, wait
from concurrent.futures import Future


# 未来对象，task的返回容器


# 线程池，为什么要线程池
# 主线程中可以获取某一个线程的状态或者某一个任务的状态，以及返回值
# 当一个线程完成的时候，我们的主线程能立即知道
# futures可以让多线程和多进程的编码接口一致

def get_html(times):
    time.sleep(times)
    print("get page {} success".format(times))
    return times


if __name__ == '__main__':
    executor = ThreadPoolExecutor(max_workers=1)

    # # 1.通过submit函数提交要执行的函数到线程池中，返回一个future对象
    # # 注意：submit是非阻塞的，立即返回
    task1 = executor.submit(get_html, (3))
    # task2 = executor.submit(get_html, (2))
    #
    # # 2.done()方法用于判断某个任务是否已经完成
    # print(task1.done())
    # print(task2.done())
    # print(task2.cancel())
    #
    # # time.sleep(4)
    # # print(task1.done())
    # # print(task2.done())
    #
    # # 3.result()方法可以获取task的执行结果，这个方法是阻塞的
    # print(task1.result())
    # print(task1.done())
    # print(task2.done())
    #
    # # 4.cancel()方法：取消任务
    # # 注意：但任务处于执行状态或者执行完成了，cancel会失败
    # print(task2.cancel())

    # 5.获取已经成功的task的返回-->as_completed函数（生成器函数）--> yield已经完成的task --> future对象
    # 批量提交任务
    times_list = [3, 2, 4]
    all_task = [executor.submit(get_html, (times)) for times in times_list]
    # wait()方法：阻塞主线程（即等待某一事件发生后再往下执行代码）
    wait(all_task, return_when='FIRST_COMPLETED')  # return_when --> 等待时间
    print("this is main！")

    # for future in as_completed(all_task):
    #     data = future.result()
    #     print("get {} page finished".format(data))

    # # 6.通过executor.map获取已经完成的task
    # # 注意：executor.map --> yield的是future.result() 而不是 future对象
    # for data in executor.map(get_html, times_list):
    #     print("get {} page finished".format(data))
