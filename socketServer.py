# coding: utf-

import socket
import json
import threading
from db import DB

class SocketServer:

	dbConection = None

	def __init__(self):
		host, port = input('Digite o servidor e a porta [127.0.0.1:8888]: ').split(':')
		self.init(host, port)

	def init(self, host: str, port: str):
		self.connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

		try:
			print('\nServidor iniciado, aguardando conexões.')
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
				break
		self.connection.close()

	def newClient(self, client, connection):
		print(f'Conexão estabelecida: {connection}')
		while True:
			data = client.recv(4096).decode('utf-8')
			if (data):
				data = json.loads(data)
				result = self.execute(data)
				client.sendall(bytes(str(result), 'utf-8'))
			else:
				break

		print(f'Conexão encerrada: {connection}.')
		client.close()

	def execute(self, data) -> str:
		if (data['action'] == 'createBook'):
			code = int(data['code'])
			title = str(data['title'])
			return self.createBook(code, title)
		elif (data['action'] == 'searchBook'):
			author = str(data['author'])
			title = str(data['title'])
			return self.searchBook(author, title)
		elif (data['action'] == 'searchByYearAndEdition'):
			year = int(data['year'])
			edition = str(data['edition'])
			return self.searchByYearAndEdition(year, edition)
		elif (data['action'] == 'deleteBook'):
			title = data['title']
			return self.deleteBook(title)
		elif (data['action'] == 'updateBook'):
			return self.updateBook()

	def createBook(self, code: int, title: str) -> str:
		query = ''' INSERT INTO livros VALUES (%s, %s) '''
		return DB().query(query, (code, title))

	def searchBook(self, author: str, title: str) -> str:
		return ''

	def searchByYearAndEdition(self, year: int, edition: str) -> str:
		return ''

	def deleteBook(self, title: str) -> str:
		return ''

	def updateBook(self) -> str: # Rever funcionamento
		return ''