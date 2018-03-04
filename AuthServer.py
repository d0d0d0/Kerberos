### Implements Authentication Server ###

from TLSServer import TLSServer
from pprint import pprint
from datetime import datetime

## Temporarly ##
from config import *

import json
import base64

class AuthServer(TLSServer):

	def __init__(self, host, port, key, crt, db):
		super(AuthServer, self).__init__(host, port, key, crt)
		self.db = db

	def handleRequest(self, req):
		print "AuthServer: This is my turn!!"

		try:
			dreq = json.loads(base64.b64decode(req))
			
			if not self.isAuth(dreq):
				print "Authentication failed!!"

		except Exception as e:
			print str(e)

	def isAuth(self, req):
		try:
			if ("uid" in req) and ("sid" in req) and ("addr" in req):
				q = (req["uid"], req["sid"], req["addr"])
				return self.db.isAuthExist(q)
			else:
				print "Wrong request type: " + str(req)
				return False
		except Exception as e:
			print str(e)


	def prepAuthResponse(self, req):
		try:
			resp = \
			{
				"ticket": None, 
				"session": None
			}

			resp["ticket"] = self.prepTicketResponse(req)
			resp["session"] = self.prepSessionResponse(req)

			return resp
		except Exception as e:
			print str(e)

	def prepTicketResponse(self, req):
		try:
			resp = \
			{
				"uid": req["uid"], 
				"sid": req["sid"],
				"stamp": datetime.now(),
				"addr": req["addr"],
				"ticket_expr": req["ticket_expr"],
				"session_key": None
			}
		except Exception as e:
			print str(e)

	def prepSessionResponse(self, req):
		pass

