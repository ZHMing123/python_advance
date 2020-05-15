# _*_ coding:utf-8 _*_
# 文件作者: ZHMing123
# 开发时间：2020/5/13 6:49
# 文件名称：gen_to_coroutine.py
# 开发工具：PyCharm

import inspect


# 生成器实现协程
# 生成器是可以暂停的函数 --> 生成器是有状态的

def gen_func():
    # 1.返回值给调用方， 2.调用方通过send方式传递值给生成器
    name = yield "zhming"  # yield from
    return "root"

# 1.用同步的方式编写异步代码，在适当的时候暂停函数并在适当的时候启动函数
# 协程的调度模式 --> 事件循环 + 协程模式， 而且是单线程
def downloader(url):
    pass

def download_html(url):
    html = yield from downloader(url)

if __name__ == '__main__':
    gen = gen_func()
    # 获取生成器的状态
    print(inspect.getgeneratorstate(gen))  # GEN_CREATED
    next(gen)
    print(inspect.getgeneratorstate(gen))  # GEN_SUSPENDED(暂停)
    try:
        next(gen)
    except StopIteration:
        pass
    print(inspect.getgeneratorstate(gen))  # GEN_CLOSED
    # next(gen)
