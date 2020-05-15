# _*_ coding:utf-8 _*_
# 文件作者: ZHMing123
# 开发时间：2020/2/4 21:53
# 文件名称：sequence_test.py
# 开发工具：PyCharm

from collections import abc
from _collections_abc import __all__

a = [1, 2]
# 要同为list才能加
c = a + [3, 4]
print(c)

"""
  += 调用__iadd__方法， __iadd__封装了extend方法(extend的参数要求是可迭代对象),extend调用append
  for v in values:
    self.append(V)
"""
# 就地加
a += [3, 4]
print(a)
# 不一定要同为list才能加，只要是可迭代对象便可以
a += (5, 6)
print(a)
