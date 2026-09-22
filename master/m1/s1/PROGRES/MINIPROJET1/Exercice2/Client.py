from socket import *
from struct import *

relaiName = 'localhost'
relaiPort = 1236
clientSocket = socket(AF_INET,SOCK_STREAM)
clientSocket.connect((relaiName,relaiPort))
fich = 'bonjour.txt' 
message = "GET "+fich+ " HTTP/1.1\r\nHost: "+relaiName+"\r\n\r\n"

def recvall(sock, length):
    blocks = []
    while length:
        block = sock.recv(length)
        if not block:
            raise EOFError('socket closed with %d bytes left'' in this block'.format(length))
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

put_block(clientSocket, message.encode('utf-8'))
print("message envoyé au relai : ", message,"\n")
print("reponse du relai : ", get_block(clientSocket).decode('utf-8'))
clientSocket.close()