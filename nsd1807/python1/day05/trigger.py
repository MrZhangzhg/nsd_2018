def set_age(name, age):
    if not 0 < age < 150:
        raise ValueError('年龄超过范围了(1-150)')
    print('%s现在是%s岁了' % (name, age))

def set_age2(name, age):
    assert 0 < age < 150, '年龄超过范围了(1-150)'
    print('%s现在是%s岁了' % (name, age))

if __name__ == '__main__':
    set_age('樊志明', 25)
    set_age2('樊志明', 255)
