import socket

server = '127.0.0.1'
port = 12345
addr = (server, port)
c = socket.socket()
c.connect(addr)
while True:
    data = input('> ') + '\r\n'
    c.send(data.encode())
    if data == 'quit':
        break
    data = c.recv(1024)
    print(data.decode())

c.close()

