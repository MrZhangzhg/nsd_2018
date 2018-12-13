def file_block(fobj):
    content = []
    for line in fobj:
        content.append(line)
        if len(content) == 10:
            yield content
            content.clear()

    if content:
        yield content


if __name__ == '__main__':
    fname = '/etc/passwd'
    fobj = open(fname)
    for block in file_block(fobj):
        print(block)

    fobj.close()
