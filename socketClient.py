# coding: utf-

import socket

class SocketClient():

	connection = None

	def __init__(self):
		try:
			host, port = input('Digite o servidor e a porta [127.0.0.1:8888]: ').split(':')
			self.init(host, port)
		except:
			print('\nFormato inválido utilize: [127.0.0.1:8888]')

	def init(self, host: str, port: str):
		self.connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

		try:
			self.connection.connect((host, int(port)))
		except socket.error as error:
			print(f'\nErro ao conectar: {error}\n')
			self.connection = None

	def read(self) -> str:
		return self.connection.recv(4096).decode('utf-8')

	def send(self, data: str):
		self.connection.send(bytes(data, 'utf-8'))