# coding: utf-

# https://pynative.com/python-postgresql-tutorial/
import psycopg2 as pgSQL
import json

class DB:

	connection = None
	cursor = None

	def __init__(self):
		self.connect()

	def connect(self):
		try:
			self.connection = pgSQL.connect(user = 'postgres', password = '', host = '127.0.1.1', port = '5432', database = 'livros')
			self.cursor = self.connection.cursor()
		except (Exception, pgSQL.Error) as error:
			if (self.connection):
				print(f'\nErro ao executar query: {error}')
			else:
				print(f'\nErro ao conectar ao PostgreSQL: {error}')

			self.connection = None
			self.cursor = None

	def query(self, fetchData: bool = False):
		result = {
			'rowCount': '0',
			'error': '',
			'data': '[]'
		}

		if (self.connection):
			try:
				if (fetchData):
					result['data'] = str(self.cursor.fetchall())
				else:
					self.connection.commit()
				result['rowCount'] = str(self.cursor.rowcount)
			except (Exception, pgSQL.Error) as error:
				result['error'] = str(error)

			self.disconnect()
		else:
			result['error'] = 'Conexão com o BD não estabelecida.'
		return json.dumps(result)

	def disconnect(self):
		if (self.connection):
			self.cursor.close()
			self.connection.close()

	def execute(self, query: str, data: tuple):
		try:
			self.cursor.execute(query, data)
		except (Exception, pgSQL.Error) as error:
				print(f'Erro: {error}')