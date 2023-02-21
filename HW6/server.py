import socket
import selectors


HOST = "127.0.0.1"  # Standard loopback interface address (localhost)
PORT = 65432  # Port to listen on (non-privileged ports are > 1023)


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


s.bind((HOST, PORT))


s.listen(4)
conn, addr = s.accept()




print(f"Connected by {addr}")
name = conn.recv(256).decode('utf8')

while True:

    data = conn.recv(1024).decode('utf8')
    conn.sendall((f'{name}: {data}').encode(encoding='utf8'))

