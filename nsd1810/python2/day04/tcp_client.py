import socket

server = '127.0.0.1'
port = 12345
addr = (server, port)
c = socket.socket()
c.connect(addr)

while True:
    data = input('(quit to stop)> ') + '\r\n'
    c.send(data.encode())
    rdata = c.recv(1024)
    print(rdata.decode())
    if data.strip() == 'quit':
        break

c.close()
