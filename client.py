# coding: utf-

import json
import ast
from socketClient import SocketClient
from rpcClient import RpcClient

class Client:

	clientConnection = None

	def __init__(self, connectionType: str):
		self.clientConnection = self.getClientConnection(connectionType)
		if (self.clientConnection.connection != None):
			self.menu()

	def getClientConnection(self, connectionType: str):
		clientConnection = None

		if (connectionType == 'socket'):
			return SocketClient()
		elif (connectionType == 'rpc'):
			return RpcClient()
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

		if (isinstance(self.clientConnection, SocketClient)):
			self.clientConnection.connection.close()

	def menuOption(self):
		option = -1

		while (option < 0) or (option > 5):
			option = inputInt('Digite uma opção: ')

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

		if (isinstance(self.clientConnection, SocketClient)):
			self.clientConnection.send(data)
			response = json.loads(self.clientConnection.read())
		else:
			response = json.loads(self.clientConnection.send(data))

		print(f'\nLinhas afetadas: {response["rowCount"]}')
		for row in ast.literal_eval(response['data']):
			print(f'Código: {row[0].strip()}, Título: {row[1].strip()}')
		if (response['error']):
			print(f'Erro: {response["error"]}')

	def createBook(self):
		return json.dumps({
			'action': 'createBook',
			'code': str(inputInt('Digite o código do livro: ')),
			'title': input('Digite o título do livro: '),
			'number': str(inputInt('Digite o número da edição: ')),
			'year': str(inputInt('Digite o ano da edição: ')),
			'authorCode': str(inputInt('Digite o código de um autor existente: '))
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
			'year': str(inputInt('Digite o ano da edição: ')),
			'edition': str(inputInt('Digite o número da edição: '))
		})

	def deleteBook(self):
		return json.dumps({
			'action': 'deleteBook',
			'code': str(inputInt('Digite o código do livro: '))
		})

	def updateBook(self):
		return json.dumps({
			'action': 'updateBook',
			'author': input('Digite o nome do autor do livro: '),
			'title': input('Digite o título do livro: '),
			'number': str(inputInt('Digite o número da edição: ')),
			'year': str(inputInt('Digite o ano da edição: '))
		})

def inputInt(question: str) -> int:
	number = -1

	try:
		number = int(input(question))
	except ValueError:
		print('\nDigite um número válido.')

	return number

if __name__ == '__main__':
	try:
		option = -1

		while (option < 0) or (option > 2):
			print('\n┌──────────────────────────────────────┐')
			print('│      Escolha o tipo de conexão       │')
			print('├───┬──────────────────────────────────┤')
			print('│ 1 │ Sockets                          │')
			print('│ 2 │ RPC                              │')
			print('│ 0 │ Sair                             │')
			print('└───┴──────────────────────────────────┘')
			option = inputInt('Digite uma opção: ')

			if (option < 0) or (option > 2):
				print('\nDigite uma opção entre 1 e 2.')

		if (option == 1):
			Client('socket')
		elif (option == 2):
			Client('rpc')
	except KeyboardInterrupt:
		print('\nOperação encerrada.')