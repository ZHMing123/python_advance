# _*_ coding:utf-8 _*_
# 文件作者: ZHMing123
# 开发时间：2020/2/16 13:43
# 文件名称：iterable_and_iterator.py
# 开发工具：PyCharm

# 可迭代： __iter__
# 迭代器：__iter__和__next__
print(dir([]))      # dir():列出所拥有的所有丰富

# 注意：一个列表执行了__iter__()后的返回值就是一个迭代器
print([].__iter__())

# 迭代器的好处：
#   节省内存
print(range(100))
print(list(range(100)))