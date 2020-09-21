# coding: utf-

import xmlrpc.client as xmlRpc

class RpcClient:
	connection = None

	def __init__(self):
		try:
			host, port = input('Digite o servidor e a porta [127.0.0.1:8888]: ').split(':')
			self.init(host, port)
		except (Exception) as error:
			print(f'\nFormato inválido utilize: [127.0.0.1:8888] {error}')

	def init(self, host: str, port: str):
		self.connection = xmlRpc.ServerProxy(f'http://{host}:{port}/')
		try:
			self.connection.testConnection()
		except (ConnectionRefusedError, Exception) as error:
			print(f'\nErro ao conectar: {error}\n')
			self.connection = None

	def send(self, data: str) -> str:
		return self.connection.execute(data)