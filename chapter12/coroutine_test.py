# _*_ coding:utf-8 _*_
# 文件作者: ZHMing123
# 开发时间：2020/5/12 20:38
# 文件名称：coroutine_test.py
# 开发工具：PyCharm

# 协程

# 回调模式 --> 编程复杂度高，同步编程的并发性不高，多线程编程间同步需要用到lock
# 需要一个可以暂停的函数，并且可以在适当的时候恢复该函数的继续执行
#    这样，我们就可以通过同步的方式去编写异步的代码，并且是在单线程内去切换任务
# --> 出现了协程：可以暂停的函数（可以先暂停的地方传入值）
# --> 生成器函数是可以暂停的

# 生成器-send、close和throw方法
def gen_func():
    # 1.可以产出值， 2.可以接收值（调用send()方法传递值进来）
    html = yield "http://www.baidu.com/"
    print(html)
    yield 2
    yield 3
    return "This is return"


if __name__ == '__main__':
    gen = gen_func()
    # 启动生成器的方式有两种：next()和send()， send --> 先赋值，再执行next()
    # 在调用send发送非None值之前，我们必须启动一次生成器，方式有两种：next(gen)或者gen.send(None)
    # url = next(gen) # 注意：刚开始启动生成器时，只能用send(None)，不能用send非None值
    print(next(gen))  # 执行到第一个yield, 返回http://www.baidu.com/，由于没有通过send赋值，所以html=None
    print(next(gen))
    print(next(gen))
    print(next(gen))