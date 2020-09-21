# coding: utf-

import socket
import threading
from functions import Functions

class SocketServer:

	connection = None

	def __init__(self):
		try:
			host, port = input('Digite o servidor e a porta [127.0.0.1:8888]: ').split(':')
			self.init(host, port)
		except:
			print('\nFormato inválido utilize [127.0.0.1:8888]')

	def init(self, host: str, port: str):
		self.connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

		try:
			print('\nServidor iniciado, aguardando conexões...')
			self.connection.bind((host, int(port)))
			self.connection.listen(5)
			self.loop()
		except socket.error as msg:
			print(f'\nErro ao iniciar servidor: {msg}\n')
			self.connection = None

	def loop(self):
		while True:
			try:
				client, address = self.connection.accept()
				threading._start_new_thread(self.newClient, (client, address))
			except KeyboardInterrupt:
				print('')
				break
		self.connection.close()

	def newClient(self, client, connection):
		print(f'Conexão estabelecida: {connection}')
		while True:
			data = client.recv(4096).decode('utf-8')
			if (data):
				result = Functions().execute(data)
				client.sendall(bytes(str(result), 'utf-8'))
			else:
				break

		print(f'Conexão encerrada: {connection}')
		client.close()