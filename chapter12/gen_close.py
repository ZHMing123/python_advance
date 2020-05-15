# _*_ coding:utf-8 _*_
# 文件作者: ZHMing123
# 开发时间：2020/5/12 21:08
# 文件名称：gen_close.py
# 开发工具：PyCharm


# 生成器-send、close和throw方法
def gen_func():
    # 1.可以产出值， 2.可以接收值（调用send()方法传递值进来）
    try:
        yield "http://www.baidu.com/"
    except GeneratorExit:  # 捕获异常，在close()处抛出异常,close()下面的代码将不会执行
        pass               # 如果没有捕获异常，在close()处不会抛出异常，但执行下面的next()抛异常StopIteration
    yield 2                # 注意：GeneratorExit继承自BaseException,所以Exception捕获不了它
    yield 3                # BaseExcetion 类是一切异常类的基类
    return "This is return"


if __name__ == '__main__':
    gen = gen_func()
    # 启动生成器的方式有两种：next()和send()， send --> 先赋值，再执行next()
    # 在调用send发送非None值之前，我们必须启动一次生成器，方式有两种：next(gen)或者gen.send(None)
    url = next(gen) # 注意：刚开始启动生成器时，只能用send(None)，不能用send非None值

    # 关闭生成器
    gen.close()
    # 捕获异常，在close()处抛出异常,close()下面的代码将不会执行
    print("zhming")
    # 如果没有捕获异常，在close()处不会抛出异常，但执行下面的next()抛异常StopIteration
    print(next(gen))  # 执行到第一个yield, 返回http://www.baidu.com/，由于没有通过send赋值，所以html=None
    print(next(gen))
    print(next(gen))

