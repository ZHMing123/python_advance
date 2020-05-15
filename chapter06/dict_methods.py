# _*_ coding:utf-8 _*_
# 文件作者: ZHMing123
# 开发时间：2020/2/5 20:12
# 文件名称：dict_methods.py
# 开发工具：PyCharm

my_dict = {"zhming":22, "root":{"zhming":"root"}}

# clear() 清空dict
# print(my_dict)
# my_dict.clear()
# print(my_dict)

# copy, 返回浅拷贝
# new_dict = my_dict.copy()
# new_dict["root"]["zhming"] = 44
# print(my_dict)

# 深拷贝
import copy

new_dict = copy.deepcopy(my_dict)
new_dict["root"]["zhming"] = 44
print(my_dict)

# fromkeys(key_list, deafult_value)
# new_list = ["ubuntu", "python"]
# new_dict = dict.fromkeys(new_list, "defaul-value")
# print(new_dict)

# get(key, deafult_value) : 当key不存在时， 返回defualt_value
default_value = new_dict.get("root1", "deafult")
print(default_value)

# items()
for key, value in new_dict.items():
    print("{key}:{value}".format(key=key, value=value))

# setdefault(key, deafult=None):当key不存在时， 返回defualt_value, 同时将key,value更新到原dict中
default_value = new_dict.setdefault("root1", "root1")
print(default_value)
print(new_dict)

# update() 相同key值的值更新
new_dict.update({"root2":"root2"})
new_dict.update(root5="root5", root3="root3")
new_dict.update([("root3","root4")])
pass