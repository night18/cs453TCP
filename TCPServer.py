from socket import *
from threading import Thread
import random

class ClientThread(Thread):
	"""docstring for ClientTread"""
	def __init__(self, ip, port, client_socket):
		Thread.__init__(self)
		self.ip = ip
		self.port = port
		self.client_socket =client_socket
		self.index = 0
		print('New server socket connect to: {}:{}'.format(ip, port) )

	def questionString(self):
		ops = ['+', '-', '*']
		rand1 = random.randint(1,10)
		rand2 = random.randint(1,10)
		operation = random.choice(ops)
		answer = eval(str(rand1)+operation+str(rand2))
		question = str(rand1)+operation+str(rand2)
		encode_question = question.encode()

		return encode_question, answer


	def run(self):
		while self.index < 100:
			encode_question, self.answer = self.questionString()
			self.client_socket.send(encode_question)

			student_answer = int(self.client_socket.recv(2048).decode())
			if self.answer == student_answer:
				self.index += 1
			else:
				self.client_socket.send("wrong\n".encode())

		self.client_socket.send("correct".encode())
		print(self.ip,"pass")


def main():
	host = ''
	server_port = 12000
	thread_count = 1

	server_socket = socket(AF_INET, SOCK_STREAM)
	server_socket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
	server_socket.bind((host,server_port))
	print('The server is ready to receive')

	while True:
		server_socket.listen()
		print('Start new thread ', thread_count, ': Waiting for connections from TCP clients')

		(connection_socket, (ip, port)) = server_socket.accept()
		new_thread = ClientThread(ip, port, connection_socket)
		new_thread.start()
		thread_count = thread_count + 1 

if __name__ == '__main__':
	main()