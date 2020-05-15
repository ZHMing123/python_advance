# _*_ coding:utf-8 _*_
# 文件作者: ZHMing123
# 开发时间：2020/4/13 9:50
# 文件名称：remove_list_qiantao.py
# 开发工具：PyCharm

# my_list = [11, [22, 3], [4, ], [9, [10, [11, [12, [33]]]]]]
# 去除多余嵌套的列表，得到[11, 22, 3, 4, 9, 10, 11, 12, 33]

def func(input_list):
    ret = []        # 保存结果
    for i in input_list:
        if isinstance(i, list):     # 判断是不是列表
            for k in func(i):       # 是列表，递归调用
                ret.append(k)
        else:                       # 不是列表
            ret.append(i)
    return ret


if __name__ == '__main__':
    my_list = [11, [22, 3], [4, ], [9, [10, [11, [12, [33, [44, [55, 66, [77]]]]]]]]]
    ret = func(my_list)
    print(ret)

