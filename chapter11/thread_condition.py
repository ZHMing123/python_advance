# _*_ coding:utf-8 _*_
# 文件作者: ZHMing123
# 开发时间：2020/5/10 21:25
# 文件名称：thread_condition.py
# 开发工具：PyCharm

# Condition--> 条件变量，用于复杂的线程间同步
import threading


# class XiaoAi(threading.Thread):
#     def __init__(self, lock):
#         super().__init__(name="小爱")
#         self.lock = lock
#
#     def run(self):
#         self.lock.acquire()
#         print("{}: 在".format(self.name))
#         self.lock.release()
#
#
# class TianMao(threading.Thread):
#     def __init__(self, lock):
#         super().__init__(name="天猫精灵")
#         self.lock = lock
#
#     def run(self):
#         self.lock.acquire()
#         print("{}: 小爱同学".format(self.name))
#         self.lock.release()


# 通过Condition完成协同读诗
"""
1.Condtion类内部实现了__enter__（调用了acquire）方法和__exit__（调用了release）方法
2.wait()方法使得线程进入等待池等待通知，同时释放锁
3.notify()方法是从等待池中挑一个线程通知，收到通知的线程从wait状态唤醒去尝试获取锁并往下执行
注意：notify不会主动释放锁
"""
# from threading import Condition
class XiaoAi(threading.Thread):
    def __init__(self, condition):
        super().__init__(name="小爱")
        self.condition = condition

    def run(self):
        with self.condition:
            self.condition.wait()  # 先进人wait状态，会主动释放锁
            print("{}: 在".format(self.name))
            self.condition.notify()  # 唤醒处于wait状态的其他线程

            self.condition.wait()
            print("{}: 好啊".format(self.name))
            self.condition.notify()

            self.condition.wait()
            print("{}: 君住长江尾".format(self.name))
            self.condition.notify()

            self.condition.wait()
            print("{}: 共饮长江水".format(self.name))
            self.condition.notify()

            self.condition.wait()
            print("{}: 此恨何时已".format(self.name))
            self.condition.notify()

            self.condition.wait()
            print("{}: 定不负相思意".format(self.name))
            self.condition.notify()


class TianMao(threading.Thread):
    def __init__(self, condition):
        super().__init__(name="天猫精灵")
        self.condition = condition

    def run(self):
        with self.condition:
            print("{}: 小爱同学".format(self.name))
            self.condition.notify()
            self.condition.wait()  # 进入wait状态

            print("{}: 我们来对古诗吧".format(self.name))
            self.condition.notify()
            self.condition.wait()

            print("{}: 我住长江头".format(self.name))
            self.condition.notify()
            self.condition.wait()

            print("{}: 日日思君不见君".format(self.name))
            self.condition.notify()
            self.condition.wait()

            print("{}: 此水几时休".format(self.name))
            self.condition.notify()
            self.condition.wait()

            print("{}: 只愿君心似我心".format(self.name))
            self.condition.notify()
            self.condition.wait()


if __name__ == '__main__':
    # lock = threading.Lock()
    condition = threading.Condition()  # 默认是RLock

    xiaoai = XiaoAi(condition)
    tianmao = TianMao(condition)

    # 注意：启动顺序很重要，要先启动先调用condition.wait()方法的哪个
    # 否则，notify()时找不到wait对象
    # 在调用with condition后才能调用wait或者notify方法（即需要先acquire获取锁）
    # condition有两层锁：一把底层锁会在线程调用了wait方法时释放（否则其他线程获取不了锁）
    #   上面的锁会在每次调用wait的时候分配一把并放入到condition的等待队列中，等待notify方法的唤醒
    xiaoai.start()
    tianmao.start()

