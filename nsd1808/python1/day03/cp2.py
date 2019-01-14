src_fname = '/bin/ls'
dst_fname = '/tmp/list'

with open(src_fname, 'rb') as src_fobj:
    with open(dst_fname, 'wb') as dst_fobj:
        while True:
            data = src_fobj.read(4096)   # 读取4096字节
            # if len(data) == 0:    # 判断读入的数据长度是否为0
            # if data == b'':       # 判断读入的数据是否是空串
            if not data:            # 判断读入的数据是否是空串
                break
            dst_fobj.write(data)


