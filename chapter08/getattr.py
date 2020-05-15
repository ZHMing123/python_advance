# _*_ coding:utf-8 _*_
# 文件作者: ZHMing123
# 开发时间：2020/2/24 22:45
# 文件名称：getattr.py
# 开发工具：PyCharm

# __getattr__ 和 __getattribute__
# __getattr__: 在查找不到属性的时候调用
# __getattribute__： 所有属性查找的入口，无条件调用，优先调用(对__getattr__的封装）

from datetime import date

class User(object):
    def __init__(self, info={}):
        self.info = info

    def __getattr__(self, item):
        return self.info[item]

    def __getattribute__(self, item):
        return "无条件调用，优先调用！"


if __name__ == '__main__':
    user = User(info={"name":"zhming", "age":22, "company":"gdut"})
    print(user.name)
    print(user.no)
