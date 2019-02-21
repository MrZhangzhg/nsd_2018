import socket

host = ''   # 0.0.0.0
port = 12345
addr = (host, port)
s = socket.socket()  # 默认创建TCP套接字
s.bind(addr)   # 将地址绑定到套接字
s.listen(1)  # 启动监听，1表示允许的客户端数目，必须提供，但是没有太大意义
cli_sock, cli_addr = s.accept()  # 接收客户端的连接请求，返回元组(客户机套接字, 客户机地址)
data = cli_sock.recv(1024)  # 一次最多接收1024字节，类似于文件的read
print(data)
print(data.decode())  # 将bytes类型转换成utf8字符
sdata = '吃了吗？\r\n'  # 网络发送数据一般结尾是回车换行
# sdata是UTF8编码，发送的时候，用encode把UTF8编码转成bytes类型
cli_sock.send(sdata.encode())  # 网络发送数据要求是bytes类型
cli_sock.close()  # 关闭客机户机套接字
s.close()  # 关闭服务器套接字

# yum install -y telnet; telnet 127.0.0.1 12345