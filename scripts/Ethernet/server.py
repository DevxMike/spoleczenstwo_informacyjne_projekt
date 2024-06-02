import socket

HOST = '0.0.0.0'
PORT = 65432    

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen()

print(f"Serwer nasłuchuje na {HOST}:{PORT}")

while True:
    conn, addr = server_socket.accept()
    print(f"Połączono z {addr}")
    data = conn.recv(1024)
    if not data:
        break
    print(f"Otrzymano: {data.decode('utf-8')}")
    conn.sendall(data)  # echo received data back to the client

conn.close()

