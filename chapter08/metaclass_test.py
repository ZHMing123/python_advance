# _*_ coding:utf-8 _*_
# 文件作者: ZHMing123
# 开发时间：2020/5/6 22:01
# 文件名称：metaclass_test.py
# 开发工具：PyCharm

# from collections.abc import *
from _collections_abc import __all__

# 自定义元类
# 类也是对象，type创建类的类

def create_class(name):
    if name == "user":
        class User:
            def __str__(self):
                return "user"
        return User # 返回类这个对象
    elif name == "company":
        class Company:
            def __str__(self):
                return "company"
        return Company


# type动态创建类
# type(object_or_name, bases, dict)
# User = type("User", (), {})

# 函数
def say(self):
    return "i am {}".format(self.name)


class BaseClass:
    def answer(self):
        return "i am BaseClass!"


# 什么是元类？ 元类是创建类的类， 对象<-class(也是对象)<-type
class MetaClass(type):  # 继承type的类就是元类
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls, *args, **kwargs)


class User(metaclass=MetaClass):  # 指定元类MetaClass，用于控制User实例化的过程
    def __init__(self, name):  # 将创建对象的过程委托给元类MetaClass来做
        self.name = name

    def __str__(self):
        return "user"

# python中类的实例化过程，会首先找metaclass，通过metaclass去创建user类对象
# 若没有指定metaclass(所继承的父类中也没有)，则调用type去创建user类对象




if __name__ == '__main__':
    # MyClass = create_class("user")
    # my_obj = MyClass()
    # print(type(my_obj))

    # User = type("User", (), {})
    # my_obj = User()
    # print(my_obj)

    # # 添加类变量name和实例方法say
    # User = type("User", (), {"name":"user", "say":say})  # 属性name="user"
    # my_obj = User()
    # print(my_obj.name)
    # print(my_obj.say()) # 调用say()方法

    # # 继承基类BaseClass
    # User = type("User", (BaseClass, ), {"name": "user", "say": say})  # 属性name="user"
    # my_obj = User()
    # print(my_obj.name)
    # print(my_obj.answer()) # 调用父类的answer()方法

    # python中类的实例化过程，会首先找metaclass，通过metaclass去创建user类对象
    # 若没有指定metaclass(所继承的父类中也没有)，则调用type去创建user类对象
    my_obj = User(name="root")
    print(my_obj)
