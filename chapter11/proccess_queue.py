# _*_ coding:utf-8 _*_
# 文件作者: ZHMing123
# 开发时间：2020/5/11 21:00
# 文件名称：proccess_queue.py
# 开发工具：PyCharm

import time
from multiprocessing import Process, Queue, Pool, Manager, Pipe


# 进程间的通信(Queue、Pipe、Manager)

# 注意：在多进程编程中，不能使用from queue import Queue中的Queue
#      而应该使用 from multiprocessing import Queue中的Queue
# 1.进程通信 -- Queue
def producer(queue):
    queue.put("a")
    time.sleep(2)

def consumer(queue):
    time.sleep(2)
    data = queue.get()
    print(data)

# 2.进程通信 -- 共享全局变量 --> 共享全局变量不适用于多进程编程，可以适用于多线程编程
#          每个进程的数据是独立的
def producer_1(a):
    a += 100
    time.sleep(2)

def consumer_1(a):
    time.sleep(2)
    print(a)

# 5.进程间通信 --> Pipe(简化版的Queue) --> 只能适用于两个进程间通信
def producer_2(pipe):
    pipe.send("zhming")

def consumer_2(pipe):
    print(pipe.recv())

# 6.使用Manager().dict()来实现进程内存共享 --> 实现数据的同步
def add_data(process_dict, key, value):
    process_dict[key] = value


if __name__ == '__main__':
    # 1.进程通信 -- Queue
    # queue = Queue(10)
    # my_producer = Process(target=producer, args=(queue,))
    # my_consumer = Process(target=consumer, args=(queue,))
    # my_producer.start()
    # my_consumer.start()
    # my_producer.join()
    # my_consumer.join()

    # 2.进程通信 -- 共享全局变量
    # a = 1
    # my_producer = Process(target=producer_1, args=(a,))
    # my_consumer = Process(target=consumer_1, args=(a,))
    #
    # my_producer.start()
    # my_consumer.start()
    # my_producer.join()
    # my_consumer.join()

    # 3.multiprocessing中的Queue不能用于pool进程池的通信
    # queue = Queue(10)
    # process_pool = Pool(2)
    # process_pool.apply_async(producer, args=(queue,))
    # process_pool.apply_async(consumer, args=(queue,))
    #
    # process_pool.close()
    # process_pool.join()

    # 4.pool进程池的通信 --> multiprocessing中Manager().Queue()
    #   Manager() --> 调用multiprocessing.SyncManager()
    # queue = Manager().Queue(10)
    # process_pool = Pool(2)
    # process_pool.apply_async(producer, args=(queue,))
    # process_pool.apply_async(consumer, args=(queue,))
    #
    # process_pool.close()
    # process_pool.join()

    # 5.进程间通信 --> Pipe(简化版的Queue) --> 只能适用于两个进程间通信 --> Pipe性能高于Queue
    # Pipe() --> return Connection(), Connection()
    # recevie_pipe, send_pipe = Pipe()
    # my_producer = Process(target=producer_2, args=(send_pipe,))
    # my_consumer = Process(target=consumer_2, args=(recevie_pipe,))
    #
    # my_producer.start()
    # my_consumer.start()
    # my_producer.join()
    # my_consumer.join()

    # 6.使用Manager().dict()来实现进程内存共享 --> 实现数据的同步
    process_dict = Manager().dict()
    first_process = Process(target=add_data, args=(process_dict, "root", 11))
    second_process = Process(target=add_data, args=(process_dict, "ubuntu", 99))

    first_process.start()
    second_process.start()
    first_process.join()
    second_process.join()

    print(process_dict)



