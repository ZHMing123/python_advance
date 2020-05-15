# _*_ coding:utf-8 _*_
# 文件作者: ZHMing123
# 开发时间：2020/2/4 21:15
# 文件名称：super_test.py
# 开发工具：PyCharm

# super真的是调用父类的构造函数吗
# 准确来说，调用的是mro查找顺序的下一个类的构造函数

class A:
    def __init__(self):
        print("A")

class B(A):
    def __init__(self):
        print("B")
        super().__init__()

class C(A):
    def __init__(self):
        print("C")
        super().__init__()

class D(B, C):
    def __init__(self):
        print("D")
        super(D, self).__init__()


if __name__ == '__main__':
    d = D()
    print(D.__mro__)