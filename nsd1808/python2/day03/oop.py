class Date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    @classmethod
    def create_date(cls, date_str):
        # tlist = date_str.split('-')
        # year = int(tlist[0])
        # month = int(tlist[1])
        # day = int(tlist[2])
        year, month, day = map(int, date_str.split('-'))
        return cls(year, month, day)

    @staticmethod
    def is_date_valid(date_str):
        year, month, day = map(int, date_str.split('-'))
        return year < 4000 and 1 <= month <= 12 and 1 <= day <= 31

if __name__ == '__main__':
    d1 = Date(2019, 1, 20)
    print(d1.month)
    d2 = Date.create_date('2019-1-21')
    print(d2.year)
    print(Date.is_date_valid('2019-13-21'))
