import socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('localhost', 12345)
client_socket.connect(server_address)
while True:
    message = input("Nhập tin nhắn: ")
    client_socket.sendall(message.encode())

    if message.lower() == 'bye':
        break
    response = client_socket.recv(1024).decode()
    print(f"Phản hồi từ server: {response}")

client_socket.close()