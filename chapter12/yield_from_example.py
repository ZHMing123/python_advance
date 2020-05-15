# _*_ coding:utf-8 _*_
# 文件作者: ZHMing123
# 开发时间：2020/5/12 22:03
# 文件名称：yield_from_example.py
# 开发工具：PyCharm

final_result = {}

def sales_sum(pro_name):
    total = 0
    nums = []
    while True:
        x = yield
        print(pro_name + "销量：", x)
        if not x:
            break
        total += x
        nums.append(x)
    return total, nums

def middle(key):
    while True:
        final_result[key] = yield from sales_sum(key)
        print(key + "销量统计完成！")

def main():
    data_sets = {
        "zhming牌面膜": [1200, 1500, 3000],
        "zhming牌手机": [28, 55, 98, 108],
        "zhming牌大衣": [280, 560, 778, 70]
    }

    for key, data_set in data_sets.items():
        print("start key:", key)
        m = middle(key)
        m.send(None)  # 预激middle协程,启动协程执行到yield from，建立main函数和sales_sum的双向通道
        for value in data_set:
            m.send(value)  # 给协程传递每一个值
        m.send(None)  # 退出循环，x=None --> break
    print("final_result:", final_result)


if __name__ == '__main__':
    main()
