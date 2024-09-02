import socket

cliente_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cliente_socket.connect(('127.0.0.1', 12345))

cliente_socket.sendall(b"Hello, Server!")
data = cliente_socket.recv(1024)
print(f"Recebido> {data.decode('utf-8')}")
cliente_socket.close()