from socket import *
from struct import *

relaiName = 'localhost'
relaiPort = 1235
clientSocket = socket(AF_INET,SOCK_STREAM)
clientSocket.connect((relaiName,relaiPort))

message = "abc"

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

clientSocket.send(message.encode('utf-8')) #envoi au relai
print("message envoyé au relai : ",message)
reponse = clientSocket.recv(2048) #reponse du relai
print("reponse : ",reponse.decode('utf-8')) 

put_block(clientSocket, message.encode('utf-8'))
print(get_block(clientSocket).decode('utf-8'))
clientSocket.close()

clientSocket.close()