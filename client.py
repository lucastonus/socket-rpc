# coding: utf-

class Client:

	def __init__(self, connType: str):
		self.conn = self.getConn(connType)
		if (self.conn != None):
			self.menu()

	def menu(self):
		option = -1

		while (option != 0):
			print('\n-- SISTEMA DE CONTROLE DE LIVROS --')
			print('1- Criar livro')
			print('2- Consultar livro')
			print('3- Consultar por ano e número da edição')
			print('4- Remover livro')
			print('5- Alterar livro')
			print('0- Sair')
			print('-------------------------------------')

			option = self.menuOption()
			self.menuAction(option)

	def inputInt(self, question: str) -> int:
		number = -1

		try:
			number = int(input(question))
		except ValueError:
			print('\nDigite um número válido.')

		return number

	def menuOption(self):
		option = -1

		while (option < 0) or (option > 5):
			option = self.inputInt('Digite uma opção: ')

			if (option < 0) or (option > 5):
				print('\nDigite uma opção entre 0 e 5.\n')

		return option

	def menuAction(self, option: int):
		print(f'Opção escolhida: {option}')

	def getConn(self, connType: str):
		conn = None

		if (connType == 'socket'):
			from socketClient import SocketClient
			conn = SocketClient()
			return conn.getConn()
		elif (connType == 'rpc'):
			pass
		else:
			print('\nTipo de conexão inválida.\n')

		return conn