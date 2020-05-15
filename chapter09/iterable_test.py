# _*_ coding:utf-8 _*_
# 文件作者: ZHMing123
# 开发时间：2020/5/9 6:41
# 文件名称：iterable_test.py
# 开发工具：PyCharm

# 什么是迭代协议
# 迭代器是什么？ 迭代器是访问集合内元素的一种方式，一般用来遍历数据
# 迭代器和以下标访问数据方式不同(下标原理是__getitem__)，迭代器是不能返回的
# 迭代器提供了一种惰性的数据访问方式

# 可迭代对象 list, tuple, dict, str等 --> 实现了__iter__方法
# 迭代器Iterator --> 继承Iterable --> 实现了__iter__和__next__方法

# from collections.abc import Iterable, Iterator
from _collections_abc import Iterable, Iterator


class Company:
    def __init__(self, employee_list):
        self.employee = employee_list

    def __iter__(self):
        return MyIterator(self.employee)  # 返回一个迭代器

    # def __getitem__(self, item):
    #     print("item-->", item)  # item记录索引值，从0开始
    #     return self.employee[item]

    # def __len__(self):
    #     return len(self.employee)


# 自定义迭代器
class MyIterator:
    def __init__(self, employee_list):
        self.iter_list = employee_list
        self.index = 0  # 需要维护一个index

    def __iter__(self):
        return self

    def __next__(self):
        # 真正返回迭代值的逻辑
        try:
            word = self.iter_list[self.index]
        except IndexError:
            raise StopIteration
        self.index += 1
        return word


if __name__ == '__main__':
    # iter()方法 --> 将迭代对象(实现了__iter__方法) 或者
    #       实现了序列访问协议的对象(实现了__getitem__方法) 转换成迭代器并返回
    a = [1, 2]
    iterator_a = iter(a)
    print(isinstance(a, Iterator))
    print(isinstance(iterator_a, Iterator))

    company = Company(["zhming", "ubuntu", "root", "user"])
    # # 调用for com in company时，系统会尝试调用iter(company)--> 去找__iter__方法
    # #       如果类没有实现__iter__方法，则找__getitem__方法，还没有则报错
    # for com in company:
    #     print(com)

    iterator_company = iter(company)
    # 这段代码作用与for语句相同
    # while True:
    #     try:
    #         print(next(iterator_company))  # next会调用 __next__方法
    #     except StopIteration:
    #         pass

    # for语句：系统会尝试调用iter(company)--> 去找__iter__方法
    for com in iterator_company:
        print(com)

