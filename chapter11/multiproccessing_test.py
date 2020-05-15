# _*_ coding:utf-8 _*_
# 文件作者: ZHMing123
# 开发时间：2020/5/11 19:50
# 文件名称：multiproccessing_test.py
# 开发工具：PyCharm

import os
import time
from concurrent.futures import ProcessPoolExecutor
import multiprocessing


# ProcessPoolExecutor是对multiproccessing的封装
# 多进程编程
def get_html(seconds):
    time.sleep(seconds)
    print("sub_proccess end!")
    return seconds

class GetHtml(multiprocessing.Process):
    def __init__(self, proccess_name, seconds):
        super().__init__(name=proccess_name)
        self.seconds = seconds

    def run(self):
        time.sleep(self.seconds)
        print("sub_proccess end!")
        return

if __name__ == '__main__':
    # # fork只能用于linux或者unix中
    # pid = os.fork()  # 注意：子进程会拷贝父进程的所有数据和代码运行（fork()之后的代码，所以会打印两次zhming）
    # print("zhming")
    # if pid == 0:
    #     print("子进程 {}，父进程：{}".format(os.getpid(), os.getppid()))  # ppid：父进程的id
    # else:
    #     print("我是父进程：{}".format(pid))
    #
    # # 不使用sleep()，父进程运行完后退出，但子进程仍在运行，所以打印在下一个命令行，而不是接着打印
    # # 而且运行代码后，子进程也不会退出
    # time.sleep(2)  # 等待子进程运行完，那么父进程退出时，子进程也会退出

    # # 1.通过multiproccessing.Proccess实例化 --> 和threading.Thread用法类似
    # proccess = multiprocessing.Process(target=get_html, args=(2,))
    # # 进程的pid --> start()之前，pid为None
    # print(proccess.pid)
    # proccess.start()
    # print(proccess.pid)
    # proccess.join()

    # # 2.继承multiproccess.Proccess类，重写run方法
    # proccess = GetHtml("get_html", seconds=2)
    # print(proccess.pid)
    # proccess.start()
    # print(proccess.pid)
    # proccess.join()
    #
    # print("main proccess end!")

    # 3.使用线程池
    proccess_pool = multiprocessing.Pool(multiprocessing.cpu_count())  # cpu_count()：电脑cpu数量
    # # apply_async-->异步提交任务，返回一个ApplyResult对象（类似于Future对象）
    # result = proccess_pool.apply_async(get_html, args=(2,))
    #
    # # join() --> 等待所有任务完成
    # # 注意：在调用join()之前，要先调用close()或者terminate()关闭进程池，这样是因为
    # #      被终止的进程需要被其父进程调用wait（join等价于wait），否则进程会成为僵尸进程
    # proccess_pool.close()
    # proccess_pool.join()
    #
    # # get()-->获取任务函数返回结果
    # print(result.get())

    # imap()方法 --> 和线程池中的map方法类似 --> 打印顺序与列表中[1, 5, 3]顺序一致
    # for result in proccess_pool.imap(get_html, [1, 5, 3]):
    #     print("{} sleep success!".format(result))

    # imap_unordered()方法 --> 先完成的先打印
    for result in proccess_pool.imap_unordered(get_html, [1, 5, 3]):
        print("{} sleep success!".format(result))


