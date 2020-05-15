# _*_ coding:utf-8 _*_
# 文件作者: ZHMing123
# 开发时间：2020/5/11 19:27
# 文件名称：python_process.py
# 开发工具：PyCharm

import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from concurrent.futures import ProcessPoolExecutor

# 多进程编程
# 耗cpu操作（计算，图像）--> 用多进程
# 对于io操作 --> 使用多线程
# 进程切换的代价要高于线程


# 1.耗cpu操作--> 多进程优于多线程
def fib(num):
    if num <= 2:
        return 1
    return fib(num-1) + fib(num-2)

# 2.io操作--> 多线程优于多进程
def random_sleep(seconds):
    time.sleep(seconds)
    return seconds

if __name__ == '__main__':
    # # 1.耗cpu操作
    # # 多线程
    # with ThreadPoolExecutor(3) as executor:
    #     all_task = [executor.submit(fib, (num)) for num in range(25, 35)]
    #     start_time = time.time()
    #     for future in as_completed(all_task):
    #         data = future.result()
    #         print("exe result:{}".format(data))
    #
    #     print("cost time is:{}".format(time.time() - start_time))

    # 多进程
    # with ProcessPoolExecutor(3) as executor:
    #     all_task = [executor.submit(fib, (num)) for num in range(25, 35)]
    #     start_time = time.time()
    #     for future in as_completed(all_task):
    #         data = future.result()
    #         print("exe result:{}".format(data))
    #
    #     print("cost time is:{}".format(time.time() - start_time))

    # # 2.io操作
    # # 多线程
    # with ThreadPoolExecutor(3) as executor:
    #     all_task = [executor.submit(random_sleep, (seconds)) for seconds in [2]*30]
    #     start_time = time.time()
    #     for future in as_completed(all_task):
    #         data = future.result()
    #         print("exe result:{}".format(data))
    #
    #     print("cost time is:{}".format(time.time() - start_time))

    # 多进程
    with ProcessPoolExecutor(3) as executor:
        all_task = [executor.submit(random_sleep, (seconds)) for seconds in [2]*30]
        start_time = time.time()
        for future in as_completed(all_task):
            data = future.result()
            print("exe result:{}".format(data))

        print("cost time is:{}".format(time.time() - start_time))

