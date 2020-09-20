# coding: utf-

import json
import ast

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
			print('\n┌──────────────────────────────────────────┐')
			print('│      SISTEMA DE CONTROLE DE LIVROS       │')
			print('├───┬──────────────────────────────────────┤')
			print('│ 1 │ Criar livro                          │')
			print('│ 2 │ Consultar por autor e título         │')
			print('│ 3 │ Consultar por ano e número da edição │')
			print('│ 4 │ Remover livro                        │')
			print('│ 5 │ Alterar número e ano da edição       │')
			print('│ 0 │ Sair                                 │')
			print('└───┴──────────────────────────────────────┘')

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
			data = self.searchBook()
		elif (option == 3):
			data = self.searchByYearAndEdition()
		elif (option == 4):
			data = self.deleteBook()
		elif (option == 5):
			data = self.updateBook()

		self.clientConnection.getConnection().send(bytes(data, 'utf-8'))
		response = json.loads(self.clientConnection.read())

		print(f'\nLinhas afetadas: {response["rowCount"]}')
		for row in ast.literal_eval(response['data']):
			print(f'Código: {row[0].strip()}, Título: {row[1].strip()}')
		if (response['error']):
			print(f'Erro: {response["error"]}')

	def createBook(self):
		return json.dumps({
			'action': 'createBook',
			'code': str(self.inputInt('Digite o código do livro: ')),
			'title': input('Digite o título do livro: '),
			'number': str(self.inputInt('Digite o número da edição: ')),
			'year': str(self.inputInt('Digite o ano da edição: ')),
			'authorCode': str(self.inputInt('Digite o código de um autor existente: '))
		})

	def searchBook(self):
		return json.dumps({
			'action': 'searchBook',
			'author': input('Digite o nome do autor do livro: '),
			'title': input('Digite o título do livro: ')
		})

	def searchByYearAndEdition(self):
		return json.dumps({
			'action': 'searchByYearAndEdition',
			'year': str(self.inputInt('Digite o ano da edição: ')),
			'edition': str(self.inputInt('Digite o número da edição: '))
		})

	def deleteBook(self):
		return json.dumps({
			'action': 'deleteBook',
			'code': str(self.inputInt('Digite o código do livro: '))
		})

	def updateBook(self):
		return json.dumps({
			'action': 'updateBook',
			'author': input('Digite o nome do autor do livro: '),
			'title': input('Digite o título do livro: '),
			'number': str(self.inputInt('Digite o número da edição: ')),
			'year': str(self.inputInt('Digite o ano da edição: '))
		})

if __name__ == '__main__':
	Client('socket')