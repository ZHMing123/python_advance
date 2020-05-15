# _*_ coding:utf-8 _*_
# 文件作者: ZHMing123
# 开发时间：2020/2/5 13:06
# 文件名称：bisect_test.py
# 开发工具：PyCharm
import bisect
from collections import deque       # 双端队列

# 用来维护已排序的序列，升序
# 二分查找
# inter_list = []         # 不一定是list，是序列便可以
inter_list = deque()
bisect.insort(inter_list, 3)
bisect.insort(inter_list, 5)
bisect.insort(inter_list, 2)
bisect.insort(inter_list, 1)
bisect.insort(inter_list, 7)

print(inter_list)

# 查看应该插入的位置
print(bisect.bisect(inter_list, 4.5))