# _*_ coding:utf-8 _*_
# 文件作者: ZHMing123
# 开发时间：2020/3/28 7:41
# 文件名称：sqlalchemy_01.py
# 开发工具：PyCharm

# import sqlalchemy
#
# print(sqlalchemy.__version__)

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey


# python内置的sqlite3
# engine = create_engine('sqlite:///foo.db', echo=True)

# mysql
"""1、通过sql语句创建表格"""
# sql = '''create table student(
#     id int not null primary key,
#     name varchar(50),
#     age int,
#     address varchar(100));
# '''
#
# engine = create_engine('mysql+pymysql://root:root@127.0.0.1:3306/sqlalchemy', echo=True)
# conn = engine.connect()
# print(conn)
# conn.execute(sql)
# course = engine.connect()         # 表示获取到数据库连接。类似我们在MySQLdb中游标course的作用。
# print(course)
# # metadata = MetaData(engine)

"""2、通过ORM方式创建表格"""
# engine = create_engine('mysql+pymysql://root:root@127.0.0.1:3306/sqlalchemy', echo=True)
# metadata = MetaData(engine)         # 在创建MetaData时绑定引擎
#
# student_orm = Table('student1', metadata,
#                     Column('id', Integer, primary_key=True),
#                     Column('name', String(50),),
#                     Column('age', Integer),
#                     Column('address', String(100),),
#             )
#
# metadata.create_all(engine)

engine = create_engine('mysql+pymysql://root:root@127.0.0.1:3306/sqlalchemy')
# DBSession = sessionmaker(bind=engine)
# session = DBSession()               # ORM通过session与数据库建立连接进行通信

# 声明性基类
Base = declarative_base()

class UserType(Base):
    __tablename__ = 'usertype'
    id = Column(Integer, primary_key=True, autoincrement=True)

    # nullable是否可为null，默认值为True
    # index是否是索引，默认值是True
    title = Column(String(32), nullable=True, index=True)


class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(30), nullable=True, index=True)
    age = Column(Integer)
    # email = Column(String(16), unique=True)     # unique默认值是False
    address = Column(String(100))
    # user_id = Column(Integer, ForeignKey('usertype.id'))


def create_db():
    engine = create_engine('mysql+pymysql://root:root@127.0.0.1:3306/sqlalchemy', echo=True)
    Base.metadata.create_all(engine)


def drop_db():
    engine = create_engine('mysql+pymysql://root:root@127.0.0.1:3306/sqlalchemy', echo=True)
    Base.metadata.drop_all(engine)


# user1 = User(id=1001, name="zhming", age=23, address='gdut')
# user2 = User(id=1002, name="root", age=23, address='gdut')
# session.add_all([user1, user2])
# session.commit()
# session.close()

if __name__ == '__main__':
    # create_db()

    DBSession = sessionmaker(bind=engine)
    session = DBSession()  # ORM通过session与数据库建立连接进行通信

    # 增
    # user1 = User(id=1001, name="zhming", age=23, address='gdut')
    # user2 = User(id=1002, name="root", age=23, address='gdut')
    # session.add_all([user1, user2])

    # 查
    # print(session.query(User))      # 自动转成sql语句
    # ret = session.query(User).all()
    # print(type(ret))                  # 列表
    # for row in ret:
    #     print(row.id, row.name, row.age, row.address)
    #
    # # 删
    # session.query(User).filter(User.name=='zhming').delete()

    # 改
    session.query(User.id, User.name).filter(User.id==1002).update({'name': 'root@'})

    session.commit()
    session.close()




