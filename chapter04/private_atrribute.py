# _*_ coding:utf-8 _*_
# 文件作者: ZHMing123
# 开发时间：2020/2/4 20:39
# 文件名称：private_atrribute.py
# 开发工具：PyCharm

# 私有属性
from chapter04.static_class_instance_method import Date

class User():
    def __init__(self, birthday):
        self.__birthday = birthday

    def get_age(self):
        return 2020 - self.__birthday.year


if __name__ == '__main__':
    user = User(Date(1997, 9, 25))
    print(user.get_age())

    # 子类和实例无法直接通过实例名.__属性名访问私有属性
    # 可通过实例名._类名__属性名访问
    print(user._User__birthday)