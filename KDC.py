### Implements "Key Distriution Center" ###

from AuthServer import AuthServer
from TGS import TGS
from DBManager import DBManager
from config import *

class KDC: 

	def __init__(self, isTGS=0):
		print "Key Distribution Center initiated"

		self.db = DBManager(DB)

		self.isTGS = isTGS

		self._authServer = AuthServer(host='localhost',
							port=AUTH_PORT,
							key=AUTH_KEY, 
							crt=AUTH_CRT,
							db=self.db)
		
		self._TGS = TGS(host='localhost',
					port=TGS_PORT,
					key=TGS_KEY, 
					crt=TGS_CRT,
					db=self.db)
		
	def getServerPool(self):
		try:
			if self.isTGS:
				return [self._authServer, self._TGS]
			else:
				return [self._authServer]
		except Exception as e:
			print str(e)

	def getSocketPool(self):
		try:
			return [s.getSocket() for s in self.getServerPool()]
		except Exception as e:
			print str(e)