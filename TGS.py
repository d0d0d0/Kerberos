### Implements Authentication Server ###

from TLSServer import TLSServer

class TGS(TLSServer):

	def __init__(self, host, port, key, crt, db):
		super(TGS, self).__init__(host, port, key, crt)

	def handleRequest(self, req):
		print "TGSServer: This is my turn!!"
