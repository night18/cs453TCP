from socket import *
from threading import Thread

class ClientThread(Thread):
	"""docstring for ClientTread"""
	def __init__(self, ip, port, client_socket):
		Thread.__init__(self)
		self.ip = ip
		self.port = port
		self.client_socket =client_socket 
		print('New server socket connect to: {}:{}'.format(ip, port) )

	def run(self):
		while True:
			# Using case translator as an example
			data = self.client_socket.recv(2048).decode()
			
			if data == 'exit':
				print('{}:{} ends the server socket'.format(self.ip, self.port))
				break

			transfered_data = data.upper()
			self.client_socket.send(transfered_data.encode())

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