# _*_ coding:utf-8 _*_
# 文件作者: ZHMing123
# 开发时间：2020/5/9 12:11
# 文件名称：generator_func.py
# 开发工具：PyCharm

# 生成器函数 --> 函数中包含yield关键字 --> 返回一个生成器对象
def generator_func():
    yield 1
    yield 2
    yield 3

# 惰性求值，延迟求值提供了可能
# 斐波拉契 1 1 2 3 5 8
def fib(n):
    if n <= 0:
        raise ValueError("n must be positive int!")
    elif n <= 2:
        return 1
    else:
        return fib(n-1) + fib(n-2)

def fib_2(n):
    if n <= 0:
        raise ValueError("n must be positive int!")
    result_list = []
    index, a, b = 0, 0, 1
    while index < n:
        result_list.append(b)
        a, b = b, a + b
        index += 1
    return result_list

def generator_fib(n):
    if n <= 0:
        raise ValueError("n must be positive int!")
    index, a, b = 0, 0, 1
    while index < n:
        yield b
        a, b = b, a + b
        index += 1

def func():
    return 1


if __name__ == '__main__':
    # 生成器对象，python编译字节码的时候就产生了
    gen = generator_func()
    res = func()
    print(fib(10))
    print(fib_2(10))

    for data in generator_fib(10):
        print(data)
