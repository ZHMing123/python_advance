# _*_ coding:utf-8 _*_
# 文件作者: ZHMing123
# 开发时间：2020/2/5 20:01
# 文件名称：dict_abc.py
# 开发工具：PyCharm

from collections.abc import Mapping, MutableMapping
from _collections_abc import __all__

# dict属于mappig类型
a = {}
print(isinstance(a, Mapping))