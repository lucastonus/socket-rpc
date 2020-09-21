# coding: utf-

from socketServer import SocketServer
from rpcServer import RpcServer

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
			SocketServer()
		elif (option == 2):
			RpcServer()
	except KeyboardInterrupt:
		print('\nOperação encerrada.')