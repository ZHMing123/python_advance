# _*_ coding:utf-8 _*_
# 文件作者: ZHMing123
# 开发时间：2020/2/13 23:01
# 文件名称：delete.py
# 开发工具：PyCharm

# del语句和垃圾回收
# python的垃圾回收机制是：引用计数
# 注意：区分del语句和垃圾回收
#     c++中： del var是直接将对象回收
#     python中： del var只是删除变量，并将变量指向的对象的引用计数减一

a = object()
b = a

del a

print(b)
print(a)