def file_block(fobj):
    content = []
    for line in fobj:
        content.append(line)
        if len(content) == 10:   # 10行生成一次
            yield content
            content.clear()      # 生成数据交给使用者后清空，以便存下10行

    if content:    # 如果循环结束后还有数据，生成最后不到10行的内容
        yield content


if __name__ == '__main__':
    fname = '/etc/passwd'
    fobj = open(fname)
    for block in file_block(fobj):
        print(block)

    fobj.close()
