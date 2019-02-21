import socket

server = '127.0.0.1'
port = 12345
addr = (server, port)
c = socket.socket()
c.connect(addr)

while True:
    data = input('> ') + '\r\n'
    c.send(data.encode())
    if data.strip() == 'quit':
        break
    rdata = c.recv(1024)
    print(rdata.decode())

c.close()
