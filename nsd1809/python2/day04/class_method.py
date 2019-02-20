class Date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    @classmethod   # 声明成类方法，没有实例也可以调用
    def create_date(cls, str_date):  # cls表示类Date,不是实例
        """
        一般来说，需要先创建实例，再通过实例调用方法。没有实例就需要调用方法
        可以将方法声明为类方法。
        """
        date_list = str_date.split('-')
        y = int(date_list[0])
        m = int(date_list[1])
        d = int(date_list[2])
        return cls(y, m, d)

    @staticmethod  # 定义静态方法。相当于跟类没有任何关系，硬塞到类中的方法
    def is_date_valid(str_date):
        y, m, d = map(int, str_date.split('-'))
        return y < 4000 and 1 <= m <= 12 and 1 <= d <=31

if __name__ == '__main__':
    d1 = Date(2019, 2, 20)
    d2 = Date.create_date('2019-2-21')  # 通过类方法创建实例
    print(d2.year)
    print(Date.is_date_valid('2019-2-2'))
