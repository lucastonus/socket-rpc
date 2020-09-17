# coding: utf-

import json

class Client:

	clientConnection = None

	def __init__(self, connectionType: str):
		self.clientConnection = self.getClientConnection(connectionType)
		if (self.clientConnection.getConnection() != None):
			self.menu()

	def getClientConnection(self, connectionType: str):
		clientConnection = None

		if (connectionType == 'socket'):
			from socketClient import SocketClient
			return SocketClient()
		elif (connectionType == 'rpc'):
			pass
		else:
			print('\nTipo de conexão inválida.\n')

		return clientConnection.connection.close()

	def menu(self):
		option = -1

		while (option != 0):
			print('\n-- SISTEMA DE CONTROLE DE LIVROS --')
			print('1 - Criar livro')
			print('2 - Consultar livro')
			print('3 - Consultar por ano e número da edição')
			print('4 - Remover livro')
			print('5 - Alterar livro')
			print('0 - Sair')
			print('-------------------------------------')

			option = self.menuOption()

			if (option != 0):
				self.menuAction(option)

		self.clientConnection.conection.close()

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
		if (option == 1):
			data = self.createBook()
		elif (option == 2):
			pass
			# data = self.searchBook()
		elif (option == 3):
			pass
			# data = self.searchByYearAndEdition()
		elif (option == 4):
			pass
			# data = self.deleteBook()
		elif (option == 5):
			pass
			# data = self.updateBook()

		self.clientConnection.getConnection().send(bytes(data, 'utf-8'))
		response = json.loads(self.clientConnection.read())

		if (response['error']):
			print(f'Erro: {response["error"]}')
		else:
			print('Sucesso na operação')

	def createBook(self):
		return json.dumps({
			'action': 'createBook',
			'code': self.inputInt('Digite o código do livro: '),
			'title': input('Digite o título do livro: ')
		})

	def searchBook(self):
		return json.dumps({
			'action': 'searchBook',
			'author': self.inputInt('Digite o nome do autor do livro: '),
			'title': input('Digite o título do livro: ')
		})

	def searchByYearAndEdition(self):
		pass
		# year: int, edition: str
		#return json.dumps(data)

	def deleteBook(self):
		pass
		# title: str
		#return json.dumps(data)

	def updateBook(self):
		pass
		#return json.dumps(data)

if __name__ == '__main__':
	Client('socket')