#Base Server

import socket 

host = "localhost"
port = 8888

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    sock.bind((host, port))
    sock.listen()
    count = 0

    while True:   
        conn, addr = sock.accept()
        count = count + 1
        conn.sendall(b"Hello Everyone ")
        print(f"{count}: Message from {addr}")
        
    
    
