# _*_ coding:utf-8 _*_
# 文件作者: ZHMing123
# 开发时间：2020/5/8 16:58
# 文件名称：MyOrm.py
# 开发工具：PyCharm

# 通过元类实现简单的orm

# 需求
import numbers

class Field:
    pass


class IntField(Field):
    def __init__(self, db_column, min_value=None, max_value=None):
        self._value = None
        self.db_column = db_column
        self.min_value = min_value
        self.max_value = max_value
        if min_value is not None:  # 非空
            if not isinstance(min_value,numbers.Integral):
                raise ValueError("min_value must be int")
            elif min_value < 0:
                raise ValueError("min_value must be positive int")
            
        if max_value is not None:  # 非空
            if not isinstance(max_value,numbers.Integral):
                raise ValueError("max_value must be int")
            elif max_value < 0:
                raise ValueError("max_value must be positive int")

        if min_value is not None and max_value is not None:
            if min_value > max_value:
                raise ValueError("min_value must be smaller than or equal to max_value")

    # 属性描述符
    def __get__(self, instance, owner):
        return self._value

    def __set__(self, instance, value):
        if not isinstance(value, numbers.Integral):
            raise ValueError("int value need!")
        if value < self.min_value or value > self.max_value:
            raise ValueError("value must between min_value and max_value!")
        self._value = value


class CharField(Field):
    def __init__(self, db_column, max_length=None):
        self._value = None
        self.db_column = db_column
        self.max_length = max_length
        if max_length is None:
            raise ValueError("must spcify max_length for CharField!")

    # 属性描述符
    def __get__(self, instance, owner):
        return self._value

    def __set__(self, instance, value):
        if not isinstance(value, str):
            raise ValueError("str value need!")
        if len(value) > self.max_length :
            raise ValueError("value length excess max_length!")
        self._value = value


# 定义元类
class ModelMetaClass(type):
    def __new__(cls, name, bases, attrs, **kwargs): # name, bases, attrs --> User = type("User", (), {})
        if name == "BaseModel":
            return super().__new__(cls, name, bases, attrs, **kwargs)

        # 当name == "User"时
        fields = {} # 记录数据表中的所有列
        for key, value in attrs.items():
            if isinstance(value, Field):
                fields[key] = value
        attrs_meta = attrs.get("Meta", None)  # Meta里面有定义的db_table="user"
        _meta = {}
        db_table = name.lower() # 不写db_table则默认为了user(User类的小写)，name是类名
        if attrs_meta is not None:
            table = getattr(attrs_meta, "db_table", None)
            if table is not None:
                db_table = table  # Meta中有db_table
        _meta["db_table"] = db_table
        attrs["_meta"] = _meta
        attrs["fields"] = fields
        del attrs["Meta"]

        # 将处理过的参数attrs传给父类来创建对象，并返回
        return super().__new__(cls, name, bases, attrs, **kwargs)


class BaseModel(metaclass=ModelMetaClass):
    def __init__(self, *args, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)  # 初始化实例的属性值
        return super().__init__()

    def save(self):
        fields = []  # 要插入的列名
        values = []  # 每列对应的值
        for key, value in self.fields.items():
            db_column = value.db_column  # value是一个CharField对象
            if db_column is None:  # 列名为空
                db_column = key.lower()
            fields.append(db_column)  #
            value = getattr(self, key)
            values.append(str(value))  # 报错：sequence item 1: expected str instance, int found, .join的问题需要将value转为字符串类型
        sql = "insert {db_table}({fields}) value({values})".format(db_table=self._meta["db_table"], fields=",".join(fields), values=",".join(values))
        pass
    

class User(BaseModel):
    name = CharField(db_column="name", max_length=10)
    age = IntField(db_column="age", min_value=10, max_value=100)

    # 需要重写__init__方法，因为有user = User(name="zhming", age=23)这种实例化情况
    # 这部分交给父类BaseModel来做
    # def __init__(self, name, age):
    #     pass

    class Meta:
        db_table = "user"


if __name__ == '__main__':
    user = User(name="zhming", age=23)
    # user.name = "bobby"
    # user.age = 28
    user.save()

