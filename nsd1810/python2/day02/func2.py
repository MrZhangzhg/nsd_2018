def add(x, y):
    return x + y

def get_age(name, age):
    print('%s is %s years old' % (name, age))

if __name__ == '__main__':
    nums = [10, 20]
    print(add(nums[0], nums[1]))
    print(add(*nums))  # *表示把nums拆开
    adict = {'age': 20, 'name': 'bob'}
    get_age(**adict)   # 拆成age=20, name=bob传给get_age
