# _*_ coding:utf-8 _*_
# 文件作者: ZHMing123
# 开发时间：2020/2/5 19:35
# 文件名称：list_gen_dict.py
# 开发工具：PyCharm

# 列表生成式（列表推导式）
# 1、1~20之间的奇数
odd_list = []
for i in range(1, 21):
    if i % 2 == 1:
        odd_list.append(i)
print(odd_list)

odd_list = [i for i in range(1, 21) if i % 2 == 1]
print(odd_list)

# 2、复杂的逻辑
def handle_item(item):
    return item * item

odd_list = [handle_item(i) for i in range(1, 21) if i % 2 == 1]     # 类似于map函数的功能
print(odd_list)

# 生成器表达式
odd_list = (i for i in range(1, 21) if i % 2 == 1)
print(odd_list)
print(type(odd_list))
for i in odd_list:
    print(i, end=' ')
# 转换为list
print(type(list(odd_list)))

# 字典推导式
my_dict = {"zhming":22, "root":33, "gudt":44}
reversed_dict = {value:key for key, value in my_dict.items()}
print(reversed_dict)

# 集合推导式
# my_set = set(my_dict.keys())
# print(my_set)
my_set = {key for key, value in my_dict.items()}
print(type(my_set))
print(my_set)