import socket

# HOST = "127.0.0.1"  # The server's hostname or IP address
# PORT = 65432  # The port used by the server
#
# with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
#     s.connect((HOST, PORT))
#     s.sendall(b"Hello, world")
#     data = s.recv(1024)
#
# print(f"Received {data!r}")

import socket
import threading

def snd_msg(name: str):
    sock = socket.socket()
    addr = ("127.0.0.1", 65432)
    sock.connect(addr)

    sock.send(name.encode('utf8'))

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        while True:
            sock.sendall((input('MSG: ').encode(encoding='utf8')))
            print(sock.recv(256).decode('utf8'))

name_lst = ['Seva', 'Misha', 'Petya']




thrd = threading.Thread(target=snd_msg(name_lst[0]))

thrd.start()
