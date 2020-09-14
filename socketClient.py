# coding: utf-

import socket

class SocketClient():

	conection = None

	def __init__(self):
		host, port = input('Digite o servidor e a porta [127.0.0.1:8888]: ').split(':')
		self.init(host, port)

	def init(self, host: str, port: str):
		self.conection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

		try:
			self.conection.connect((host, int(port)))
		except socket.error as msg:
			print(f'\nErro ao conectar: {msg}\n')
			self.conection = None

	def getConn(self):
		return self.conection