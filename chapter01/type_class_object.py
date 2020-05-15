# _*_ coding:utf-8 _*_
# 文件作者: ZHMing123
# 开发时间：2020/1/15 21:20
# 文件名称：type_class_object.py
# 开发工具：PyCharm

"""
type、class和object的关系:
    （1）type->class->obj         （class类是由type生成的， 实例obj是由class类生成的）
    （2）object是最顶层的基类
    （3）type是一个类，同时也是一个对象
"""

# （1）type->class->obj
a = 1
b = 'abc'
print(type(a))
print(type(int))
print(type(b))
print(type(str))


class Student:
    pass


stu = Student
print(type(stu))
print(type(Student))

# （2）object是最顶层的基类
print(int.__bases__)            # object
print(str.__bases__)            # object
print(Student.__bases__)        # object
print(type.__bases__)           # object
print(object.__bases__)         # ()


class Mystudent(Student):
    pass


print(Mystudent.__bases__)      # Student
print(type(object))             # type