import socket
import threading
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
        cli_sock.close()

    def run(self):
        while True:
            try:
                cli_sock, cli_addr = self.s.accept()
            except KeyboardInterrupt:
                print()
                break
            t = threading.Thread(target=self.chat, args=(cli_sock,))
            t.start()

        self.s.close()

if __name__ == '__main__':
    server = TcpServer()
    server.run()
