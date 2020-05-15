# _*_ coding:utf-8 _*_
# 文件作者: ZHMing123
# 开发时间：2020/4/13 8:46
# 文件名称：pymysql_dao.py
# 开发工具：PyCharm

import pymysql


db = pymysql.connect(
    host="localhost",
    port=3306,
    user="root",
    passwd="root",
    database="my_pymysql"
)

# cursor = db.cursor()
# 以字典的形式返回结果
cursor = db.cursor(cursor=pymysql.cursors.DictCursor)
print(cursor)

# 增
#
# 1、插入一条数据
# sql_insert = "insert into info(username, password) values (%s, %s)"
# try:
#     # 执行SQL语句
#     cursor.execute(sql_insert, ["hello", ])
#     # 一定要提交事务(写操作)
#     db.commit()
#     # 获取提交后刚插入的数据的ID(关联操作时)
#     last_id = cursor.lastrowid
# except Exception as e:
#     print("插入数据失败：" + str(e))
#     db.rollback()   # 回滚

# # 2、批量插入操作
# sql_insert_many = "insert into info(username, password) values (%s, %s)"
# try:
#     insert_data = [("shehui", "shehuiren"), ("hello", "world"), ("who", "am i")]
#     cursor.executemany(sql_insert_many, insert_data)
#     db.commit()     # 注意：提交一次
# except Exception as e:
#     print("插入数据失败：" + str(e))
#     db.rollback()   # 回滚

# # 删
# sql_delete = "delete from info where username=%s"
# cursor.execute(sql_delete, "zhming")

# # 改
# sql_update = "update info set password=%s where username=%s"
# ret = cursor.execute(sql_update, ["root@@", "root@"])
# print(ret)

# 查
sql_query = "select * from info"
# ret = cursor.execute(sql_query)     # 受影响的行数
# print("{} rows in set".format(ret))
cursor.execute(sql_query)
ret = cursor.fetchall()     # 返回所有数据
print(ret)

# 光标（游标）移动
cursor.scroll(0, mode="absolute")       # 从第一条数据开始
ret = cursor.fetchone()
print(ret)

cursor.scroll(-1, mode="relative")       # 从第一条数据开始
ret = cursor.fetchmany(3)
print(ret)


# 断开连接
db.commit()
cursor.close()
db.close()