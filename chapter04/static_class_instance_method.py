# _*_ coding:utf-8 _*_
# 文件作者: ZHMing123
# 开发时间：2020/2/4 20:12
# 文件名称：static_class_instance_method.py
# 开发工具：PyCharm

class Date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    @staticmethod
    def date_parse_from_string(date_str):
        year, month, day = tuple(date_str.split("-"))
        return Date(int(year), int(month), int(day))

    @staticmethod
    def valid_str(date_str):
        year, month, day = tuple(date_str.split("-"))
        if int(year)>0 and (int(month)>0 and int(month)<=12) and int(day)>0 and int(day)<=31:
            return True
        else:
            return False

    @classmethod
    def parse_from_string(cls, date_str):
        year, month, day = tuple(date_str.split("-"))
        return cls(int(year), int(month), int(day))

    def __str__(self):
        return "{year}/{month}/{day}".format(year=self.year, month=self.month, day=self.day)



if __name__ == "__main__":
    new_day = Date(2020, 2, 4)
    print(new_day)

    # 2020-2-4
    date_str = "2020-2-32"
    year, month, day = tuple(date_str.split("-"))
    new_day = Date(int(year), int(month), int(day))
    print(new_day)

    # 用staticmethod完成初始化
    new_day = Date.date_parse_from_string(date_str)
    print(new_day)

    # 用classmethod完成初始化
    new_day = Date.parse_from_string(date_str)
    print(new_day)

    print(Date.valid_str(date_str))