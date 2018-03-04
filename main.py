### Run main ###

from KDC import KDC
from select import select

kdc = KDC()

serverPool = kdc.getServerPool()
socketPool = kdc.getSocketPool()

INIT_STAGE = 1

for t in ["USER", "SERVICE", "AUTH", "TGS"]:
	kdc.db.createTable(t)

if INIT_STAGE:
	kdc.db.insert("USER", (1, "Dodo"))
	kdc.db.insert("USER", (2, "Can"))

	kdc.db.insert("SERVICE", (1, "Facebook"))
	kdc.db.insert("SERVICE", (2, "Twitter"))

	kdc.db.insert("AUTH", (1, 1, "10.30.0.10"))
	kdc.db.insert("AUTH", (1, 2, "10.30.0.15"))

'''
try:
	while 1:
	    notifiedSocketList = select(socketPool, [], [], 1)[0]
	    for notifiedSocket in notifiedSocketList:
	    	i = socketPool.index(notifiedSocket)
	    	server = serverPool[i]
	        server.activate()
finally:
	for sock in socketPool:
		sock.close()
'''