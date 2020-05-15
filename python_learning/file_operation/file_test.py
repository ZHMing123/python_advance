# _*_ coding:utf-8 _*_
# 文件作者: ZHMing123
# 开发时间：2020/2/15 20:49
# 文件名称：file_test.py
# 开发工具：PyCharm

# f = open("test.txt", mode="r", encoding="utf-8")
# content = f.read()
# print(content)
# f.close()

# f = open("test.txt", mode="r+", encoding="utf-8")
# content = f.read()
# print(content, type(content))
# f.write("hello")
# # 当前光标的位置
# print(f.tell())
# # 将光标重置会行首
# f.seek(0)
# print(f.tell())
# content = f.read()
# print(f.tell())
# print(content)
# f.close()

# f = open("test.txt", mode="a", encoding="utf-8")
# f.write("ubuntu")
# f.close()

# 闭包：嵌套函数，内部函数调用外部函数的变量
import requests


# def outer():
#     a = 1
#     def inner():
#         print(a)
#     return inner
#     # print(inner.__closure__)
#
# inn = outer()
# inn()
# print(outer.__closure__)


class A(object):
    name = "zhming"
    __age = 12

    def run(self):
        print("this is A run!", self.__age)

class B(A):
    pass

a = A()
print(a._A__age)
b = B()
print(b.name)
