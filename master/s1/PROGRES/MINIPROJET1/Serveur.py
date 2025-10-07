from threading import *
from socket import *
from struct import *

serverPort = 1234
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(5)

print('server ready')

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

def handle_client(connectionSocket):
    message = get_block(connectionSocket).decode('utf-8')     
    print("message : ", message)

    reponse = message.upper()
    print("réponse envoyée au relai : ", reponse)

    put_block(connectionSocket, (reponse).encode('utf-8'))
    connectionSocket.close()

while True:
    connectionSocket, relaiAddress = serverSocket.accept()
    Thread(target=handle_client, args=(connectionSocket,)).start()