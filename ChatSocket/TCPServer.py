import socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('localhost', 12345)
server_socket.bind(server_address)
server_socket.listen(1)
print("Đang chờ kết nối...")

client_socket, client_address = server_socket.accept()

print(f"Kết nối từ: {client_address}")
while True:
    message = client_socket.recv(1024).decode()
    modifiedMessage = message.upper()
    #server_socket.sendall(modifiedMessage.encode(), client_address)
    if message.lower() == 'bye':
        break
    response = modifiedMessage
    client_socket.sendall(response.encode())
# Đóng kết nối
client_socket.close()
server_socket.close()
