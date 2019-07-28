import socket

server = ''
port = 12345
addr = (server, port)
c = socket.socket(type=socket.SOCK_DGRAM)

c.sendto('你好\r\n'.encode(), addr)
# 一次最多接收1024字节数据，返回元组(数据，服务器地址信息)
result = c.recvfrom(1024)
print(result)

data = result[0]
print(data.decode())

c.close()
