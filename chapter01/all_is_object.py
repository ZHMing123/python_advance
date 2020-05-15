# _*_ coding:utf-8 _*_
# 文件作者: ZHMing123
# 开发时间：2020/1/14 23:00
# 文件名称：all_is_object.py
# 开发工具：PyCharm

"""
python中一切皆是对象(函数和类也是对象，属于python的一等公民)
一等公民的特性：
    1、可以赋值给一个变量
    2、可以添加到集合对象中
    3、可以作为参数传递给函数
    4、可以作为函数的返回值

"""

# 1、可以赋值给一个变量
def ask(name="zhming"):
    print(name)

my_func = ask
my_func()           # 对my_func的操作相当于对ask的操作
print("*"*30)

class Person:
    def __init__(self):
        print("zhming@")

my_class = Person
my_class()
print("*"*30)

# 2、可以添加到集合对象中
obj_list = []
obj_list.append(ask)
obj_list.append(Person)
for item in obj_list:
    print(item())
print("*"*30)

# 3、可以作为参数传递给函数


# 4、可以作为函数的返回值
def decorate_func():
    print("decorate start")
    return ask

my_ask = decorate_func()        # 返回ask函数
my_ask()                        # 调用ask