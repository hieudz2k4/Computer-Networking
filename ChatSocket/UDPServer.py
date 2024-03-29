# Description: This is a simple UDP server that receives a message from a client,
# converts the message to uppercase, and sends the modified message back to the client.

from socket import *
serverPort = 12000
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('', serverPort))
print('The server is ready to receive messages')

while True:
    message, clientAddress = serverSocket.recvfrom(2048)
    modifiedMessage = message.decode().upper()
    serverSocket.sendto(modifiedMessage.encode(), clientAddress)
    if message.decode().lower() == 'bye':
        break
serverSocket.close()

# The server waits for a message from the client and then converts the message to uppercase.
# The server then sends the modified message back to the client. The server will continue to
# run until it is manually stopped.
# Note: The server does not need to listen for connections, since UDP is connectionless.
# The server simply waits for a message from the client.