import socket

cliente_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

message = b"Hello, server"

cliente_socket.sendto(message, ('127.0.0.1', 12345))

data, addr = cliente_socket.recvfrom(1024)
print(f"Recebido de {addr}: {data.decode('utf-8')}")
cliente_socket.close()