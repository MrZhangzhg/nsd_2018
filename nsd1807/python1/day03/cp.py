# f1 = open('/bin/ls', 'rb')
# f2 = open('/tmp/ls', 'wb')
#
# data = f1.read()
# f2.write(data)
#
# f1.close()
# f2.close()
##########################
#
# src_fname = '/bin/ls'
# dst_fname = '/tmp/list'
#
# src_fobj = open(src_fname, 'rb')
# dst_fobj = open(dst_fname, 'wb')
#
# while True:
#     data = src_fobj.read(4096)
#     # if len(data) == 0:
#     if not data:   # 读不到数据，意味着已经读完了
#         break
#     dst_fobj.write(data)   # 读到数据，则写入目标文件
#
# src_fobj.close()
# dst_fobj.close()
#
#############################
#
src_fname = '/bin/ls'
dst_fname = '/tmp/list'

with open(src_fname, 'rb') as src_fobj:
    with open(dst_fname, 'wb') as dst_fobj:
        while True:
            data = src_fobj.read(4096)
            if not data:
                break
            dst_fobj.write(data)



