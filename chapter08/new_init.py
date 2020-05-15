# _*_ coding:utf-8 _*_
# 文件作者: ZHMing123
# 开发时间：2020/5/6 20:46
# 文件名称：new_init.py
# 开发工具：PyCharm

# __new__和__init__的区别

class User:
    def __new__(cls, *args, **kwargs):
        print("in __new__")
        return super().__new__(cls)  # 调用父类方法生成对象并返回
    def __init__(self, name):
        print("in __init__")
        self.name = name


# new是用来控制对象生成过程，在对象生成之前
# init是用来对new生成返回的对象进行初始化
# 如果new不返回生成的对象，则不会调用init函数
if __name__ == '__main__':
    user = User("zhming")

