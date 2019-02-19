def blocks(fobj):
    content = []
    counter = 0
    for line in fobj:
        content.append(line)    # 向列表追加数据
        counter += 1
        if counter == 10:   # 如果已经向列表追加了10行，则生成
            yield content   # 遇到yield，返回数据，暂停执行，直到再向生成器取数据时才继续向下执行
            content = []    # 生成完数据后，再把列表清空
            counter = 0     # 计数器清0
    if content:
        yield content   # 如果最后不足10行，也要把它返回

if __name__ == '__main__':
    fname = '/etc/passwd'
    with open(fname) as fobj:
        for lines in blocks(fobj):  # blocks是一个生成器，每次返回10行
            print(lines)
            print('*' * 20)
