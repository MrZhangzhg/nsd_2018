def gen_block(fobj):
    '用于每次返回10行数据'
    content = []
    for line in fobj:
        content.append(line)
        if len(content) == 10:
            yield content   # 遇到yield，返回数据，生成器停在此处不继续向下执行
            content = []

    if content:    # 最后不够10行的内容也要返回一次
        yield content

if __name__ == '__main__':
    fname = '/etc/passwd'
    fobj = open(fname)
    mygen = gen_block(fobj)
    for block in mygen:  # 因为生成器每次返回10行，这里的block也就是10行内容
        print(block)
        print('*' * 30)

    fobj.close()
