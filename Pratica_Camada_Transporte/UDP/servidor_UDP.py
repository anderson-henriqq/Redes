import socket
#Comunicação inter processual, com método SOCKET
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) #UDP
server_socket.bind(('127.0.0.1', 12345)) 

print("Servidor UDP pronto e aguardando conexão")
while True:
    data, addr = server_socket.recvfrom(1024)
    print(f"Recebido de {addr}: {data.decode('utf-8')}")
    response = b"Mensagem recebida"
    server_socket.sendto(response, addr)