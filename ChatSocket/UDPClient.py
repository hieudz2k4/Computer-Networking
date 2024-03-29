from socket import *

serverName = 'localhost'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_DGRAM)
clientSocket.settimeout(1)
while True:
    message = input('Type your message: ')
    clientSocket.sendto(message.encode(), (serverName, serverPort))
    if message.lower() == 'bye':
        print('SEE YOU LATER!')
        break
    try:
        modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
        print(modifiedMessage.decode())
    except:
        print('ERROR: Server not responding')
clientSocket.close()