import socket

HOST = '192.168.50.188'
PORT = 65432             

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))

message = "Witaj, serwerze!"
client_socket.sendall(message.encode('utf-8'))

data = client_socket.recv(1024)
print(f"Otrzymano od serwera: {data.decode('utf-8')}")

client_socket.close()

