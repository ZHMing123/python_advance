# _*_ coding:utf-8 _*_
# 文件作者: ZHMing123
# 开发时间：2020/2/15 23:02
# 文件名称：decorate_advance.py
# 开发工具：PyCharm

from functools import wraps

def wrapper(func):
    @wraps(func)
    def inner(*args, **kwargs):
        ret = func(*args, **kwargs)
        return ret
    return inner

@wrapper            # holiday = wrapper(holiday)
def holiday(day):
    print("holiday is %s"%day)
    return "happy"

print(holiday(4))
ret = holiday(3)    # inner(3)
print(ret)
print(holiday.__name__)

# 编写装饰器，为多个函数加上记录调用功能，要求每次调用函数都将被调用的函数名称写入文件
def log(func):
    def inner(*args, **kwargs):
        with open("log.txt", mode="a", encoding="utf-8") as f:
            f.write(func.__name__+"\n")
        ret = func(*args, **kwargs)
        return ret
    return inner

@log
def shoplist_add():
    print("增加一件商品")

@log
def shoplist_del():
    print("删除一件商品")

shoplist_add()
shoplist_del()
shoplist_del()

# 网页缓存
import os
from urllib.request import urlopen

def cache(func):
    def inner(*args, **kwargs):
        # 文件内有内容，就优先从文件读取，否则就去下载
        if os.path.getsize("web_cache"):        # 判断文件中是否有内容
            with open("web_cache", "rb") as f:
                return f.read()
        ret = func(*args, **kwargs)             # get() 请求网页的函数
        with open("web_cache", "wb") as f:      # 将请求结果写入文件中
            f.write(b'zhming' + ret)
        return ret
    return inner

@cache
def get(url):
    code = urlopen(url).read()
    return code

ret = get("http://www.baidu.com")
print(ret)
ret = get("http://www.baidu.com")
print(ret)
ret = get("http://www.baidu.com")
print(ret)

# 带参数的装饰器
# 500个函数
import time

FLAG = True
def timmer_out(flag=False):
    def timmer(func):
        def inner(*args, **kwargs):
            if flag:
                start = time.time()
                ret = func(*args, **kwargs)
                end = time.time()
                print(end - start)
                return ret
            else:
                ret = func(*args, **kwargs)
                return ret
        return inner
    return timmer

# timmer = timmer_out(FLAG)
# @timmer
@timmer_out(FLAG)   # 先调用timmer(FLAG)返回 timmer， 然后@timmer, 相当于wahaha=timmer(wahaha)
def wahaha():
    time.sleep(0.01)
    print("wahaha")

@timmer_out(FLAG)
def erguotou():
    time.sleep(0.01)
    print("erguotuo")

wahaha()
erguotou()


# 多个装饰器装饰同一个函数
def wrapper1(func): # func --> f
    def inner1(*args, **kwargs):
        print("wrapper1, before func")
        ret = func()      # func --> f
        print("wrapper1, after func")
        return ret
    return inner1

def wrapper2(func): # func --> inner1
    def inner2(*args, **kwargs):
        print("wrapper2, before func")
        ret = func()      # func --> inner1
        print("wrapper2, after func")
        return ret
    return inner2

@wrapper2   # 2、f = wrapper1(f) --> wrapper1(innner1) = inner2
@wrapper1   # 1、f = wrapper1(f) = inner1
def f():
    print("in f")
    return "zhming"

print(f())         # 注意：3、调用的不是inner1(), 而是inner2()