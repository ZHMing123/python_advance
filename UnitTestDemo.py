# _*_ coding:utf-8 _*_
# 文件作者: ZHMing123
# 开发时间：2020/3/26 22:47
# 文件名称：UnitTestDemo.py
# 开发工具：PyCharm

import unittest

# Unittest类，必须继承于Case类
class UnitDemo(unittest.TestCase):
    # 前置条件
    def setUp(self):
        print('setUp function')

    # 后置条件
    def tearDown(self):
        print('tearDown function')


    # a测试用例
    def test_a(self):
        print('a')

    # b测试用例
    def test_b(self):
        print('b')


if __name__ == '__main__':
    # 用unittest.main启动
    unittest.main()