# _*_ coding:utf-8 _*_
# 文件作者: ZHMing123
# 开发时间：2020/5/12 21:43
# 文件名称：yield_from_test.py
# 开发工具：PyCharm

# python3.3新加了yield from语法
from itertools import chain


my_list = [1, 3, 5, 6]
my_dict = {
    "root1": "root",
    "ubuntu1": "ubuntu"
}

def my_chain(*args, **kwargs):
    for my_iterable in args:
        for value in my_iterable:
            yield value


def my_chain_yield_from(*args, **kwargs):
    for my_iterable in args:
        yield from my_iterable  # 返回时，逐一返回可迭代对象的值

def gen_1(iterable_obj):
    yield iterable_obj

def gen_2(iterable_obj):
    yield  from iterable_obj

# yield from最重要的特性
def gen1(gen):
    yield from gen

def main():
    g = gen1()
    g.send(None)

# main：调用方法， g1：委托生成器，gen:子生成器
# 1.yield from 会直接在调用方(main)和子生成器(gen)直接建立一个双向通道
#

if __name__ == '__main__':
    # # 1.chain() --> 逐一返回每个可迭代对象的值，dict只是返回key
    # for value in chain(my_list, my_dict, range(5, 10)):
    #     print(value)
    #

    # 2.用yield实现chain方法
    # for value in my_chain(my_list, my_dict, range(5, 10)):
    #     print(value)

    # 3.用yield from实现chain方法
    # for value in my_chain_yield_from(my_list, my_dict, range(5, 10)):
    #     print(value)

    # 4.yield 和 yield from的区别
    for value in gen_1(range(10)):
        print(value)               # 打印结果 --> range(0, 10)

    for value in gen_2(range(10)):
        print(value)