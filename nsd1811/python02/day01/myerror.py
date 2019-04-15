def set_age(name, age):
    if not 0 < age < 120:
        raise ValueError('年龄超出范围')
    print('%s is %s years old.' % (name, age))

def set_age2(name, age):
    assert 0 < age < 120, '年龄超出范围'  # 如果age不在此范围，一定发生AssertionError
    print('%s is %s years old.' % (name, age))

if __name__ == '__main__':
    set_age2('杨晨', 24)
