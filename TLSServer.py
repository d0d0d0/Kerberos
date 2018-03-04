### Implements generic TLS server ###

from socket import *
from ssl import *

class TLSServer(object):

	def __init__(self, host, port, key, crt):
		sock = socket(AF_INET, SOCK_STREAM)
		sock.bind((host, port))
		sock.listen(1)

		self._server = wrap_socket(sock, 
						ssl_version=PROTOCOL_TLSv1,  
						server_side=True, 
						keyfile=key,
						certfile=crt)

		print "TLS Server is ready on IP %s and port %d" % (host, port)

	def handleRequest(self, req):
		pass

	def getSocket(self):
		return self._server

	def activate(self):
		try:
			conn, addr = self._server.accept()
			print "Connection from %s" % (addr[0])	
			
			req = conn.recv(1024)

			self.handleRequest(req)
			
			conn.shutdown(SHUT_RDWR)
			conn.close()
			
		except KeyboardInterrupt:
			self._server.shutdown(SHUT_RDWR)
			self._server.close()
