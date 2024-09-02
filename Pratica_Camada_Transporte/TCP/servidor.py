import socket

# AF_INET:     IPv4
# SOCK_DGRAM:  UDP
# SOCK_STREAM: TCP

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # TCP

# Como vincular uma aplicação específica em um ip?

# Vinculando um processo (através da porta), com um endereço IP
server_socket.bind(("127.0.0.1", 12345)) # Portas de 0 à 65535 (16 bits)
server_socket.listen()               # escutar na porta

print("Servidor pronto e aguardando conexão")

conn, addr = server_socket.accept() # aceitar conexão

print(f"Conectado IP {addr}")

data = conn.recv(1024)

print(f"Recebido: {data.decode('utf-8')}")

conn.sendall(b"Mensagem recebida!")
conn.close()