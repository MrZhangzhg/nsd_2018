f1 = open('/bin/ls', 'rb')
f2 = open('/tmp/ls', 'wb')

data = f1.read()
f2.write(data)

f1.close()
f2.close()
# md5sum /bin/ls /tmp/ls
# open中的内容是字符串，建议用变量
# f1/f2不能体现这两个变量的作用
# 如果文件很大，read将会把所有数据读入内存
