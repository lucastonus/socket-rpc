# coding: utf-

import json
from db import DB

class Functions:
	def execute(self, data: str) -> str:
		data = json.loads(data)

		if (data['action'] == 'createBook'):
			code = int(data['code'])
			title = str(data['title'])
			number = int(data['number'])
			year = int(data['year'])
			authorCode = int(data['authorCode'])
			return self.createBook(code, title, number, year, authorCode)
		elif (data['action'] == 'searchBook'):
			title = '%' + str(data['title']) + '%'
			author = '%' + str(data['author']) + '%'
			return self.searchBook(title, author)
		elif (data['action'] == 'searchByYearAndEdition'):
			year = int(data['year'])
			edition = str(data['edition'])
			return self.searchByYearAndEdition(year, edition)
		elif (data['action'] == 'deleteBook'):
			code = data['code']
			return self.deleteBook(code)
		elif (data['action'] == 'updateBook'):
			author = '%' + str(data['author']) + '%'
			title = str(data['title'])
			number = int(data['number'])
			year = int(data['year'])
			return self.updateBook(author, title, number, year)

	def createBook(self, code: int, title: str, number: int, year: int, authorCode: int) -> str:
		db = DB()
		query = 'INSERT INTO livros VALUES (%s, %s)'
		db.execute(query, (code, title))
		query = 'INSERT INTO edicao VALUES (%s, %s, %s)'
		db.execute(query, (code, number, year))
		query = 'INSERT INTO livroautor VALUES(%s, %s)'
		db.execute(query, (code, authorCode))
		return db.query()

	def searchBook(self, title: str, author: str) -> str:
		db = DB()
		query = 'SELECT CAST(l.codigo AS VARCHAR), l.titulo FROM livros l JOIN livroautor la ON la.codigolivro = l.codigo JOIN autor a ON a.codigo = la.codigoautor WHERE l.titulo LIKE %s AND a.nome LIKE %s ORDER BY l.titulo LIMIT 10'
		db.execute(query, (title, author))
		return db.query(True)

	def searchByYearAndEdition(self, year: int, edition: str) -> str:
		db = DB()
		query = 'SELECT CAST(l.codigo AS VARCHAR), l.titulo FROM livros l JOIN edicao e ON e.codigolivro = l.codigo WHERE e.ano = %s AND e.numero = %s ORDER BY l.titulo LIMIT 10'
		db.execute(query, (year, edition))
		return db.query(True)

	def deleteBook(self, code: int) -> str:
		db = DB()
		query = 'DELETE FROM livroautor WHERE codigolivro = %s'
		db.execute(query, (code, ))
		query = 'DELETE FROM edicao WHERE codigolivro = %s'
		db.execute(query, (code, ))
		query = 'DELETE FROM livros WHERE codigo = %s'
		db.execute(query, (code,))
		return db.query()

	def updateBook(self, author: str, title: str, number: int, year: int) -> str:
		db = DB()
		query = 'UPDATE edicao e SET numero = %s, ano = %s FROM livros l JOIN livroautor la ON la.codigolivro = l.codigo JOIN autor a ON a.codigo = la.codigoautor WHERE e.codigolivro = l.codigo AND a.nome LIKE %s AND l.titulo = %s'
		db.execute(query, (number, year, author, title))
		return db.query()