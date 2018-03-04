### Implements example client ###

from socket import *
from ssl import *
from config import *

import json
import base64

req = {
    "uid": 1,
    "uname": "Dodo",
    "sid": 2,
    "addr": "10.30.0.1",
    "req_valid": "07/10/2018"
}

req = base64.b64encode(json.dumps(req))
print req

sockA = socket(AF_INET, SOCK_STREAM)

client = wrap_socket(sockA, 
                ssl_version=PROTOCOL_TLSv1, 
                cert_reqs=CERT_REQUIRED,
                ca_certs=AUTH_CRT)

client.connect(('localhost',4433))


client.send(req)

client.shutdown(SHUT_RDWR)
client.close()


'''
sockT = socket(AF_INET, SOCK_STREAM)
client = wrap_socket(sockT, 
                ssl_version=PROTOCOL_TLSv1, 
                cert_reqs=CERT_REQUIRED,
                ca_certs=TGS_CRT)

client.connect(('localhost',4434))

req = "Trying hard means everything."

client.send(req)
client.shutdown(SHUT_RDWR)
client.close()
'''