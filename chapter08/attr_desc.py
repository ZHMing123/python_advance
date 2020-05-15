# _*_ coding:utf-8 _*_
# 文件作者: ZHMing123
# 开发时间：2020/2/25 7:55
# 文件名称：attr_desc.py
# 开发工具：PyCharm

# 属性描述符和属性查找过程
# 属性描述符：一个对象只要实现__get__、__set__或者__delete__就是一个属性描述符对象

import numbers


# 数据参数类型检查
class IntField:
    # 数据描述符
    def __get__(self, instance, owner):  # instance是传进来的user实例（print(user.age)）
        return self.value

    # 实例赋值时，调用__set__方法
    def __set__(self, instance, value):  # instance是传进来的user实例（user.age=30）
        if not isinstance(value, numbers.Integral):
            raise ValueError("int value need!")
        if value < 0:
            raise ValueError("positive value need!")
        # self.value = value: 将数据保存在IntField类中，因此在实例instance.__dict__是找不到的
        self.value = value
        # # 保存到实例对象的__dict__中
        # instance.__dict__[self.value] = value

    def __delete__(self, instance):
        pass


class NonDataIntField:
    # 非数据属性描述符
    def __get__(self, instance, owner):
        return self.value


class User:
    # age = 1
    age = IntField()
    # age = NonDataIntField()    # age本来是一个对象，放在类里当作了User类的属性

"""
user.age的查找顺序
如果user是某个类的实例，那么user.age（以及等价的getattr(user,’age’)）
首先调用__getattribute__，如果在__getattribute__找不到属性就会引发AttributeError
如果类定义了__getattr__方法，在抛出AttributeError的时候就会调用到__getattr__
而对于__get__所谓的调用，则是发生在__getattribute__内部的。
"""

"""
user = User（），那么user.age依次如下：

    1、如果“ age”是出现在用户所属的类（User）或其基类的__dict__中(即类变量)，并且age是数据描述符，那么调用其__get__方法
    2、如果“ age”出现在user（对象）的__dict__中，那么直接返回obj.__dict__[‘age’]
    3、如果“ age”出现在User（类）或基基类的__dict__中
        （1）如果age是非数据描述符，那么调用其__get__方法    # 例如 age = NonDataIntField()
        （2）返回__dict__[‘age’]                        # 例如 age = 1
    4、如果User有__getattr__方法，调用__getattr__方法，否则
    5、抛出AttributeError
    类的静态函数，类函数，普通函数，变量以及一些内置的属性都是放置类__dict__里的
    对象.__ dict__中存储了一些self.xxx的一些东西
"""

if __name__ == '__main__':
    user = User()
    user.age = 30                 # 会进入IntField的__set__中，没有进入到user实例对象的__dict__中
    print(user.age)                 # 进入数据描述符的__get__
    # setattr(user, 'age', 18)      # 进入数据描述符的__set__
    user.__dict__["age"]= "abc"     #
    print(user.__dict__)            # 直接操作__dict__属性，与.的属性访问方式走的路径不同
    print(user.__dict__["age"])     # 直接操作__dict__属性，与.的属性访问方式走的路径不同
    # print(user.age)               # age没有进入到user实例对象的__dict__中.所以不能使用.来访问

    # user是某个类的实例，那么user.age（以及等价的getattr(user,’age’)）
    # print(getattr(user, "age"))

