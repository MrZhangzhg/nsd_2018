class Date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    @classmethod
    def create(cls, str_date):   # cls -> Date
        '类中的方法，没有实例不能直接调用，需要将其定义为类方法'
        # str_list = str_date.split('-')
        # year = int(str_list[0])
        # month = int(str_list[1])
        # day = int(str_list[2])
        year, month, day = map(int, str_date.split('-'))
        instance = cls(year, month, day)  # Date(year, month, day)
        return instance

    @staticmethod
    def check_date(str_date):
        '相当于和类没有关系，只是把一个函数放到类中'
        year, month, day = map(int, str_date.split('-'))
        return year < 4000 and 1 <= month <= 12 and 1 <= day <= 31


if __name__ == '__main__':
    d1 = Date(2018, 12, 15)
    print(d1.year)
    d2 = Date.create('2018-12-10')
    print(d2)
    print(d2.month)
    print(Date.check_date('2018-12-10'))
    print(Date.check_date('2018-12-40'))
