from socket import *
from threading import *
from struct import *


relaiPort = 1235

serverPort = int(input("Entrer le port du serveur : "))
serverName = str(input("Entrer l'adresse IP du serveur : "))

serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', relaiPort))
serverSocket.listen(5)
print('relai ready')

def recvall(sock, length):
    blocks = []
    while length:
        block = sock.recv(length)
        if not block:
            raise EOFError('socket closed with %d bytes left''in this block'.format(length))
        length -= len(block)
        blocks.append(block)
    return b''.join(blocks)

header_struct = Struct("!I")
def put_block(sock, message):
    block_length = len(message)
    sock.sendall(header_struct.pack(block_length))
    sock.sendall(message)

def get_block(sock):
    data = recvall(sock, header_struct.size)
    (block_length,) = header_struct.unpack(data)
    return recvall(sock, block_length)

def handle_client(clientConnection):
    clientSocket = socket(AF_INET, SOCK_STREAM)
    clientSocket.connect((serverName, serverPort))
    
    message = get_block(clientConnection)
    print("message du client :", message.decode('utf-8'))

    put_block(clientSocket,message)
    print("message envoyé au serveur")
    
    reponse = get_block(clientSocket)
    print("réponse du serveur :", reponse.decode('utf-8'))

    put_block(clientConnection,reponse)
    print("réponse envoyée au client")
    
    clientConnection.close()
    clientSocket.close()

while True:
    clientConnection, address = serverSocket.accept()
    print("connexion client acceptée")
    Thread(target=handle_client, args=(clientConnection,)).start()
