import socket
from time import strftime

class TcpServer:
    def __init__(self, host='', port=12345):
        self.addr = (host, port)
        self.s = socket.socket()
        self.s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.s.bind(self.addr)
        self.s.listen(1)

    def chat(self, cli_sock):
        while True:
            data = cli_sock.recv(1024)
            if data.strip() == b'quit':
                break
            data = '[%s] %s' % (strftime('%H:%M:%S'), data.decode())
            cli_sock.send(data.encode())

    def run(self):
        while True:
            cli_sock, cli_addr = self.s.accept()
            self.chat(cli_sock)
            cli_sock.close()

        s.close()

if __name__ == '__main__':
    server = TcpServer()
    server.run()
