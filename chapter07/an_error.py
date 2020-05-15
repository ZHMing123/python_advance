# _*_ coding:utf-8 _*_
# 文件作者: ZHMing123
# 开发时间：2020/2/13 23:12
# 文件名称：an_error.py
# 开发工具：PyCharm

# 可变参数传递的问题
class Company:
    def __init__(self, name, staffs=[]):
        self.name = name
        self.staffs = staffs

    def add(self, staff_name):
        self.staffs.append(staff_name)

    def remove(self, staff_name):
        self.staffs.remove(staff_name)


if __name__ == '__main__':
    com1 = Company("com1", ["zhming1", "zhming2"])
    com1.add("zhming3")
    com1.remove("zhming1")
    print(com1.staffs)

    print("com2 default:")
    print(Company.__init__.__defaults__)
    com2 = Company("com2")
    com2.add("zhming")
    print(com2.staffs)

    print("com3 default:")
    print(Company.__init__.__defaults__)
    com3 = Company("com3")
    com3.add("zhming5")
    print(com2.staffs)
    print(com3.staffs)
    print(com2.staffs is com3.staffs)