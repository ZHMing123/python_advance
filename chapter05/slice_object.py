# _*_ coding:utf-8 _*_
# 文件作者: ZHMing123
# 开发时间：2020/2/4 22:27
# 文件名称：slice_object.py
# 开发工具：PyCharm

import numbers
from _collections_abc import __all__

# 实现可切片对象
class Group:
    # 支持切片操作
    def __init__(self, group_name, company_name, staffs):
        self.group_name = group_name
        self.company_name = company_name
        self.staffs = staffs

    def __reversed__(self):
        return self.staffs.reverse()

    def __getitem__(self, item):
        # 切片后为list
        # return self.staffs[item]

        # 希望切片后仍是group, 而不是list
        # 两种情况：slice：group[:2] 和 int：group[0]
        cls = type(self)        # 获取当前self的class
        if isinstance(item, slice):
            return cls(group_name=self.group_name, company_name=self.company_name, staffs=self.staffs[item])
        elif isinstance(item, numbers.Integral):
            return cls(group_name=self.group_name, company_name=self.company_name, staffs=[self.staffs[item]])



    def __len__(self):
        return len(self.staffs)

    def __iter__(self):
        return iter(self.staffs)

    def __contains__(self, item):
        if item in self.staffs:
            return True
        else:
            return False

if __name__ == '__main__':
    staffs = ["zhming1", "zhming2", "zhming3"]
    group = Group(group_name="class3", company_name="gdut", staffs=staffs)
    # __getitem__
    sub_group = group[:2]
    sub_group = group[0]

    # __len__
    print(len(group))

    # __contain__
    if "zhming1" in group:
        print("yes")

    # __iter__
    for user in group:
        print(user)

    # __reversed__
    reversed(group)
    for user in group:
        print(user)



