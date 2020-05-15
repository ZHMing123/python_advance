# _*_ coding:utf-8 _*_
# 文件作者: ZHMing123
# 开发时间：2020/2/4 19:44
# 文件名称：attr_mro.py
# 开发工具：PyCharm

class D:
    pass

# class E:
#     pass

class B(D):
    pass

class C(D):
    pass

class A(B, C):
    pass

print(A.__mro__)