# _*_ coding:utf-8 _*_
# 文件作者: ZHMing123
# 开发时间：2020/2/2 20:49
# 文件名称：type_isinstance.py
# 开发工具：PyCharm

class A:
    pass

class B(A):
    pass

b = B()

print(isinstance(b, A))
print(isinstance(b, B))

print(type(B))

print(type(b) is B)
print(type(b) is A)