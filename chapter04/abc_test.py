# _*_ coding:utf-8 _*_
# 文件作者: ZHMing123
# 开发时间：2020/2/2 20:18
# 文件名称：abc_test.py
# 开发工具：PyCharm

# 抽象基类（abc模块）
class Company(object):
    def __init__(self, employee_list):
        self.employee = employee_list

    def __len__(self):
        return len(self.employee)


com = Company(["bobby1", "bobby2"])
print(hasattr(com, "__len__"))

# 1、在某些情况下希望判定某个对象的类型
from collections.abc import Sized
print(isinstance(com, Sized))


# 2、需要强制某些子类必须实现某些方法
# 实现了Web框架，集成Cache(redis，cache)
# 设计一个抽象基类，指定子类必须实现某些方法

# 如何模拟一个抽象基类
import abc

class CacheBase(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def get(self, key):
        pass

    @abc.abstractmethod
    def set(self, key, value):
        pass


# 继承CacheBase,如果没有重写get()和set()方法，则在实例化的时候回报错
class RedisCache(CacheBase):
    pass

redis_cache = RedisCache()