 # _*_ coding:utf-8 _*_
# 文件作者: ZHMing123
# 开发时间：2020/2/13 23:27
# 文件名称：property_test.py
# 开发工具：PyCharm

# property动态属性
# 1. get和set的方法名称都要一样（age）
# 2. set方法返回的属性前面加个"_"
# 3. @property是针对get方法
# 4. @age.setter是针对set方法，是@property本身又创建了另一个装饰器
# 5. 直接可以这样stu.age=10对象名.方法名进行赋值，
# 6. 只定义getter方法，不定义setter方法是一个只读属性
class Student:
    def __init__(self, name):
        self.name = name
        self._age = 0

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        if isinstance(age, int):
            if 0 < age < 120:
                self._age = age
        else:
            print("请输入合法年龄！")


if __name__ == '__main__':
    stu = Student("zhming")
    print(stu.age)
    print(stu._age)
    stu.age = 10
    stu._age = 11   # stu.age和stu._age 操作的都是同一个变量
    print(stu.age)
    print(stu._age)

    print(stu.age is stu._age)
