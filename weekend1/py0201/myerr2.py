def set_info(name, age):
    if not 0 < age < 120:
        raise ValueError('年龄超过范围')
    print('%s is %s years old' % (name, age))

def set_info2(name, age):
    assert 0 < age < 120, '年龄超过范围'
    print('%s is %s years old' % (name, age))


if __name__ == '__main__':
    set_info('tom', 20)
    set_info2('tom', 200)

