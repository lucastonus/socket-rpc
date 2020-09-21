# coding: utf-

from xmlrpc.server import SimpleXMLRPCServer
from functions import Functions

class RpcServer:

	connection = None

	def __init__(self):
		try:
			host, port = input('Digite o servidor e a porta [127.0.0.1:8888]: ').split(':')
			self.init(host, port)
		except (ValueError):
			print('\nFormato inválido utilize [127.0.0.1:8888]')
		except (KeyboardInterrupt):
			print('')

	def init(self, host: str, port: str):
		try:
			print('\nServidor iniciado, aguardando conexões...')
			self.connection = SimpleXMLRPCServer((host, int(port)))
			self.connection.register_function(self.testConnection, 'testConnection')
			self.connection.register_function(Functions().execute, 'execute')
			self.connection.serve_forever()
		except (Exception) as error:
			print(f'\nErro ao iniciar servidor: {error}\n')
			self.connection = None

	def testConnection(self):
		return True

	def execute(self, data: str) -> str:
		return Functions().execute(data)