# _*_ coding:utf-8 _*_
# 文件作者: ZHMing123
# 开发时间：2020/2/16 13:50
# 文件名称：generator.py
# 开发工具：PyCharm

# 生成器
# 生成器函数：含有yield关键字的函数就是生成器函数
#           yield关键字不能和return共用
#           执行后返回一个生成器
# 生成器表达式：

# 生成器函数
def generator():
    print(1)
    yield "zhming"
    print(2)
    yield "root"

g = generator()         # 返回一个生成器，代码还没有执行
# ret = g.__next__()      # 执行到第一个yield的地方，并返回去yield后面的值
# print(ret)
# ret = g.__next__()
# print(ret)

for item in g:          # 实际上也是调用g.__next__()
    print(item)

# 监听文件输入的例子
