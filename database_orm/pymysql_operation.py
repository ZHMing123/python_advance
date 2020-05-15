# _*_ coding:utf-8 _*_
# 文件作者: ZHMing123
# 开发时间：2020/4/12 23:26
# 文件名称：pymysql_operation.py
# 开发工具：PyCharm

import pymysql

# 获取用户输入
username = input("输入用户名：")
pwd = input("输入密码：")

# 连接数据库
# 参数一：host=localhost, mysql服务所在主机的IP
# 参数二：port=3306,端口
# 参数三：user="root",用户名
# 参数四：password="root",密码
# 参数五：db="my_pymsql"，要连接的数据库名

db = pymysql.connect(
        host="localhost",
        port=3306,
        user="root",
        passwd="root",
        database="my_pymysql",
        # charset="utf8"          # 千万记得没有-
    )

# 创建游标对象（获取输入SQL语句的光标对象）
cursor = db.cursor()
print(cursor)

# sql_show_table = "show tables"
# # 1、sql语句拼接(SQL注入问题）
# sql = "select * from info where username='%s' and password='%s';" %(username, pwd)
# print(sql)
# print("============================")
# # 执行sql语句
# ret = cursor.execute(sql)               # 返回影响的行的数量
# # print(ret)

# 规避SQL注入问题
sql = "select * from info where username=%s and password=%s;"       # 不用加单引号
print(sql)
print("============================")
# 执行sql语句时传入字符串，让pymysql帮我们拼接，它会做校验
ret = cursor.execute(sql, [username, pwd])               # 返回影响的行的数量
# print(ret)

if ret:
    print("登录成功！")
else:
    print("登录失败！")

# # 获取返回的信息
# data = cursor.fetchone()
# print(data)

# 断开并关闭连接
cursor.close()
db.close()