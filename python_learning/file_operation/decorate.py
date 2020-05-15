# _*_ coding:utf-8 _*_
# 文件作者: ZHMing123
# 开发时间：2020/2/15 21:50
# 文件名称：decorate.py
# 开发工具：PyCharm

# 装饰器
# 装饰器的作用：在不改变原函数调用方式的情况下，在函数的前后添加功能
# 原则：开放封闭原则
#     开放：对扩展是开放的
#     封闭：对修改是封闭的
# 装饰器的固定模式

# def decorate_func(f):       # 装饰器函数
#     def inner():
#         ret = f()                 # 被装饰的函数
#         return ret                # 若f()有返回值，用ret返回
#     return inner
#
# @decorate_func
# def func():
#     print("hello world!")
#     return "zhming"
#
# # @decorate_func装饰后，不需要func = decorate_func(func)这句
# # func = decorate_func(func)  # 返回inner的内存地址
# # print(func)
# ret = func()                    # 相当于调用innner()
# print(ret)

# 装饰带参数函数的装饰器
def decorate_func(f):       # 装饰器函数
    def inner(*args, **kwargs):
        ret = f(*args, **kwargs)                 # 被装饰的函数
        return ret                # 若f()有返回值，用ret返回
    return inner

@decorate_func
def func(name, age):
    print("hello world!", name, age)
    return "zhming"

@decorate_func
def func1(name):
    print("hello world!", name)
    return "zhming"


# @decorate_func装饰后，不需要func = decorate_func(func)这句
# func = decorate_func(func)  # 返回inner的内存地址
# print(func)
ret = func("张三", 18)                    # 相当于调用innner()
ret1 = func1("ubuntu")                    # 相当于调用innner()
print(ret)
print(ret1)

# 装饰器的固定模式
def wrapper(func):
    def inner(*args, **kwargs):
        ret = func(*args, **kwargs)
        return ret
    return inner

@wrapper        # qqxing = wrapper(qqxing)
def qqxing():
    print("zhming")

ret = qqxing()        # inner