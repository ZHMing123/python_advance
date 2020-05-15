# _*_ coding:utf-8 _*_
# 文件作者: ZHMing123
# 开发时间：2020/2/2 19:57
# 文件名称：4_1_duck_and_polymorphic.py
# 开发工具：PyCharm

# 4_1 鸭子类型和多态
# 若实现同一个方法，便可归为同一类型
class Cat(object):
    def say(self):
        print("I am a cat")


class Dog(object):
    def say(self):
        print("I am a dog")


class Duck(object):
    def say(self):
        print("I am a duck")


animal_list = [Cat, Dog, Duck]
for animal in animal_list:
    animal().say()