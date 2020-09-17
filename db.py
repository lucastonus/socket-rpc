# coding: utf-

# https://pynative.com/python-postgresql-tutorial/
import psycopg2 as pgSQL
import json

class DB:

	connection = None
	cursor = None

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

	def query(self, query: str, data: tuple, fetchData: bool = False):
		result = {'error': ''}

		self.connect()

		if (self.connection):
			try:
				self.cursor.execute(query, data)
				if (fetchData):
					result['data'] = self.cursor.fetchall()
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