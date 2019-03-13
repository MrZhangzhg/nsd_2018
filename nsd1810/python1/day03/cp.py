f1 = open('/bin/ls', 'rb')
f2 = open('/tmp/ls', 'wb')

data = f1.read()   # 读出来的是bytes类型
f2.write(data)

f1.close()
f2.close()

# md5sum /bin/ls /tmp/ls
