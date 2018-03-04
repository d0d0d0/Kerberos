### Implements database management for Authentication Server and TGS ###

from Query import *
from sqlite3 import *
from config import *

class DBManager(object):

	def __init__(self, dbname):
		try:
			self.conn = connect(dbname)
			self.cursor = self.conn.cursor()

		except Exception as e:
			print str(e)

	def createTable(self, ttype):
		try:
			if ttype in TYPE_SERVICE:
				self.cursor.execute(CREATE_SERVICE_TABLE)
			elif ttype in TYPE_USER:
				self.cursor.execute(CREATE_USER_TABLE)
			elif ttype in TYPE_AUTH:
				self.cursor.execute(CREATE_AUTH_TABLE)
			elif ttype in TYPE_TGS:
				self.cursor.execute(CREATE_TGS_TABLE)
			else:
				print "Invalid table type."

			self.conn.commit()
		except Exception as e:
			print str(e)

	def insert(self, ttype, val):
		try:
			if ttype in TYPE_SERVICE:
				self.cursor.execute(INSERT_SERVICE, val)
			elif ttype in TYPE_USER:
				self.cursor.execute(INSERT_USER, val)
			elif ttype in TYPE_AUTH:
				self.cursor.execute(INSERT_AUTH, val)
			elif ttype in TYPE_TGS:
				self.cursor.execute(INSERT_TGS, val)
			else:
				print "Invalid table type."

			self.conn.commit()
		except Exception as e:
			print str(e)

	def isAuthExist(self, val):
		try:
			self.cursor.execute(IS_AUTH, val)
			data = self.cursor.fetchone()
			if data == None:
				return False
			return True
			
		except Exception as e:
			print str(e)	


		