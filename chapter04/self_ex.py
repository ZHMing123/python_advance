# _*_ coding:utf-8 _*_
# 文件作者: ZHMing123
# 开发时间：2020/2/4 20:50
# 文件名称：self_ex.py
# 开发工具：PyCharm

# python对象的自省机制
# 自省是通过一定的机制查询到对象的内部结构
from chapter04.static_class_instance_method import Date
class Person:
    """
    zhming
    """
    name = "Person"

class Student(Person):
    def __init__(self, school_name):
        self.school_name = school_name


if __name__ == '__main__':
    user = Student("广东工业大学")
    print(user.__dict__)
    print(user.name)
    print(dir(user))    # 比.__dict__功能更强大
    print(dir(Person))
    print(Person.__dict__)