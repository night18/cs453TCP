from socket import *

serverName = '10.0.2.15' #Remeber to check Server IP by using ifconfig
serverPort = 12000

clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))
print('Connect to the TCP server')
message = ''

while message != 'exit':

	message = input('input lowercase sentence (type \"exit\", when you want to exit):\n')
	clientSocket.send(message.encode())

	modifiedSentence = clientSocket.recv(1024)
	print('From server: ', modifiedSentence.decode())

clientSocket.close()
