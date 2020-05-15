# _*_ coding:utf-8 _*_
# 文件作者: ZHMing123
# 开发时间：2020/5/9 12:29
# 文件名称：how_generator_work.py
# 开发工具：PyCharm

# python中函数的工作原理
import dis
import inspect

frame = None


def foo():
    bar()

def bar():
    global frame
    frame = inspect.currentframe()  # 获取栈帧


# python.exe(python解释器)会用一个叫做PyEval_EvalFrameEx(C语言写的函数)去执行foo函数
# 首先会创建一个栈帧(stack frame)
"""
python中一切皆对象，栈帧是对象，字节码(编译后得到字节码)也是对象
当foo调用了子函数bar，又会创建一个新的栈帧
所有栈帧都是分配在堆内存上（不释放会一直存在于内存中），这就决定了栈帧可以独立于调用者存在
    即foo()不存在了或退出执行了，仍然可以通过执行bar的栈帧来控制bar的执行
"""

def gen_func():
    yield 1
    name = "zhming"
    yield 2
    age = 23

    # 注意：在早期版本中，yield不能和return同时出现
    return "root"

if __name__ == '__main__':
    # print(dis.dis(foo))
    foo()
    print(frame.f_code.co_name)  # f_code是bar的字节码
    caller_frame = frame.f_back  # f_back：获取调用者foo的栈帧
    print(caller_frame.f_code.co_name)

    gen = gen_func()  # 返回一个生成器对象，但还没开始执行函数
    print(dis.dis(gen))

    print("*" * 30)
    print(gen.gi_frame.f_lasti)
    print(gen.gi_frame.f_locals)

    print("*" * 30)
    next(gen)  # 执行函数到第一个yield
    print(gen.gi_frame.f_lasti)
    print(gen.gi_frame.f_locals)

    print("*" * 30)
    next(gen)  # 执行函数到第二个yield
    print(gen.gi_frame.f_lasti)
    print(gen.gi_frame.f_locals)

    # for data in gen:  # 注意：return返回的值不在gen中
    #     print(data)


    from collections import UserList
