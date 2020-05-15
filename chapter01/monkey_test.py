# _*_ coding:utf-8 _*_
# 文件作者: ZHMing123
# 开发时间：2020/1/15 22:37
# 文件名称：monkey_test.py
# 开发工具：PyCharm


"""
猴子补丁仅指在运行时动态改变类或模块，为的是将第三方代码打补丁在不按预期运行的bug或者feature上 。
在运行时动态修改模块、类或函数，通常是添加功能或修正缺陷。猴子补丁在代码运行时内存中发挥作用，不会修改源码，
因此只对当前运行的程序实例有效。因为猴子补丁破坏了封装，而且容易导致程序与补丁代码的实现细节紧密耦合，
所以被视为临时的变通方案，不是集成代码的推荐方式。
"""
class Student:
    def say(self):
        print("I am zhming!")


def say_teacher():
    print("I am a teacher!")


stu = Student()
stu.say = say_teacher

stu.say()