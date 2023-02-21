import socket
import threading


def snd_msg(name1: str):
    sock = socket.socket()

    addr = ("127.0.0.1", 65432)

    sock.connect(addr)

    sock.send(name1.encode('utf8'))

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        while True:
            sock.sendall((input(f'{name1} MSG: ').encode(encoding='utf8')))
            print(sock.recv(1024).decode('utf8'))





name_lst = ['Seva', 'Misha', 'Petya']

thrd = threading.Thread(target=snd_msg(name_lst[0]))
thrd.start()
