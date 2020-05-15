# _*_ coding:utf-8 _*_
# 文件作者: ZHMing123
# 开发时间：2020/1/15 22:42
# 文件名称：company.py
# 开发工具：PyCharm


class Company(object):
    def __init__(self, employee_list):
        self.employee = employee_list

    def __getitem__(self, item):
        return self.employee[item]

    # def __str__(self):
    #     return ','.join(self.employee)

    def __repr__(self):
        return ' '.join(self.employee)

company = Company(["zhming", "root"])

for item in company:
    print(item)

print(company)


class Nums(object):
    def __init__(self, num):
        self.num = num

    def __abs__(self):
        return abs(self.num)

my_num = Nums(-3)
print(abs(my_num))


class MyVector(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other_instance):
        re_vector = MyVector(self.x + other_instance.x, self.y + other_instance.y)
        return re_vector

    def __str__(self):
        return "x:{x} y:{y}".format(x=self.x, y=self.y)

first_vector = MyVector(1, 2)
second_vector = MyVector(3, 4)
print(first_vector + second_vector)