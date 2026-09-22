from socket import *
from struct import *

clientSocket = socket(AF_INET, SOCK_STREAM)
ipServeur = gethostname()  
serverPort = 1234              
fich = 'bonjour.txt' 

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

clientSocket.connect((ipServeur, serverPort))
print("IP Server : ",ipServeur,", Port : ",serverPort)

message = "GET "+fich+ " HTTP/1.1\r\nHost: "+ipServeur+"\r\n\r\n"
put_block(clientSocket, message.encode('utf-8'))
print(get_block(clientSocket).decode('utf-8'))
clientSocket.close()