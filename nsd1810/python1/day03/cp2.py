src_fname = '/bin/touch'
dst_fname = '/tmp/touch'
src_fobj = open(src_fname, 'rb')
dst_fobj = open(dst_fname, 'wb')

while True:
    data = src_fobj.read(4096)
    # if data == b'':   # 如果文件已经全部读完，再读取将会得到空串，退出循环
    # if len(data) == 0:
    if not data:  # 空串为False，取反为True
        break
    dst_fobj.write(data)

src_fobj.close()
dst_fobj.close()
