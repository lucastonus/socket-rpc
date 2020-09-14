# coding: utf-

import socket

class SocketServer:

	conection = None

	def __init__(self):
		host, port = input('Digite o servidor e a porta [127.0.0.1:8888]: ').split(':')
		self.init(host, port)

	def init(self, host: str, port: str):
		self.conection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

		try:
			self.conection.bind((host, int(port)))
			self.conection.listen(5)
			self.loop()
		except socket.error as msg:
			print(f'\nErro ao iniciar servidor: {msg}\n')
			self.conection = None

	def loop(self):
		print('Servidor iniciado, aguardando conexões.')

		while True:
			client, address = self.conection.accept()
			print(f'Conexão estabelecida com {address}')

			data = client.recv(1024)
			data = data.decode('utf-8')

			# client.send(bytes('message', 'utf-8'))

			client.close()

if __name__ == '__main__':
	SocketServer()