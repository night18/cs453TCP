from socket import *
import time

# serverName = '52.207.55.32' #Remeber to check Server IP by using ifconfig
serverName = '10.0.2.15'
serverPort = 12000

clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))
print('Connect to the TCP server')

# message = input('input lowercase sentence (type \"exit\", when you want to exit):\n')
# clientSocket.send(message.encode())

text_from_server = clientSocket.recv(2048)
decoded_text = text_from_server.decode()
print(decoded_text)
while decoded_text != "correct":
	message = str(eval(decoded_text))
	# message = input()
	clientSocket.send(message.encode())

	response_from_server = clientSocket.recv(2048)
	decoded_text = response_from_server.decode()
	print(decoded_text)
	time.sleep(0.3)


clientSocket.close()
