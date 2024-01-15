#Base Client

import socket 

HOST = "localhost"
PORT = 8888

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((HOST, PORT))

sock.send(b"Merhabalar")
print(sock.recv(1024))
sock.close()