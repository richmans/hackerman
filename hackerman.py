from console import Console
from kernel import Kernel
import sys
import socketserver

class Hackerman:
    def __init__(self):
        self.kernel = Kernel()
        self.console = Console(self.kernel, sys.stdin, sys.stdout)

    def main(self):
        self.kernel.start()
        self.console.start()
        try:
            self.kernel.join()
        except KeyboardInterrupt:
            self.kernel.shutdown()
            self.kernel.join(1.0)


class ThreadingTCPServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    pass


class HackermanTCPHandler(socketserver.BaseRequestHandler):
    class SocketWrapper:
        def __init__(self, sock):
            self.sock =sock

        def readline(self):
            pass
        def write(self, msg):
            self.sock.send(msg)

    def handle(self):
        self.kernel = Kernel()
        sock = self.request.makefile(mode='rw')
        self.console = Console(self.kernel, sock,sock)

        self.kernel.start()
        self.console.start()
        try:
            self.kernel.join()
        except KeyboardInterrupt:
            self.kernel.shutdown()
            self.kernel.join(1.0)
            self.console.join(1.0)


class HackerServer:
    def __init__(self, port):
        self.port = port

    def run(self):
        socketserver.TCPServer.allow_reuse_address = True
        HOST, PORT = "0.0.0.0", self.port
        print(self.port)
        with ThreadingTCPServer((HOST, PORT), HackermanTCPHandler) as server:
            server.serve_forever()

if __name__ == "__main__":
    if len(sys.argv) > 1:
        port = int(sys.argv[1])
        HackerServer(port).run()
    else:
        Hackerman().main()