# _*_ coding:utf-8 _*_
# 文件作者: ZHMing123
# 开发时间：2020/2/4 22:14
# 文件名称：slice_test.py
# 开发工具：PyCharm

# 模式：[start, end, step]
# 切片操作返回一个新的列表
aList = [1, 3, 5, 7]
print(aList[0:100])
print(aList[100:])
aList[2:2] = [10]
print(aList)