# _*_ coding:utf-8 _*_
# 文件作者: ZHMing123
# 开发时间：2020/2/5 21:24
# 文件名称：dict_subclass.py
# 开发工具：PyCharm

# dict的子类
# 不建议直接继承dict或者list
class Mydict(dict):
    def __setitem__(self, key, value):
        super().__setitem__(key, value*2)

my_dict = Mydict()
# print(my_dict)      # 结果为{'one': 1}， 即没有调用到super().__setitem__
my_dict["one"] = 1
print(my_dict)      # 结果为{'one':2}， 调用到super().__setitem__

# 若确实是需要，继承Userdict
from collections import UserDict
class Mydict(UserDict):
    def __setitem__(self, key, value):
        super().__setitem__(key, value*2)

my_dict = Mydict(one=1)
print(my_dict)      # 结果为{'one': 2}， 调用到super().__setitem__


# defaultdict: __missing__方法
from collections import defaultdict
my_dict = defaultdict(dict)
my_value = my_dict["zhming"]
print(my_value)         # 没有key值zhming，但由于调用了__missing__,不报错KeyError，返回默认值{}
