class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return '《%s》' % self.title

    def __call__(self):
        print('《%s》 is written by %s' % (self.title, self.author))

if __name__ == '__main__':
    corepy = Book('Python核心编程', 'Wesley')  # 调用__init__方法
    # print('《%s》' % corepy.title)
    print(corepy)  # 打印实例时，自动调用__str__方法
    corepy()   # 自动调用__call__方法，使实例像函数一样，可以调用
