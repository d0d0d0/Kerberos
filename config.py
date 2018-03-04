### Contains configuration paramaters for KDS ###

import os

CUR_DIR = os.getcwd()
KEY_DIR = CUR_DIR + "/keys"
DB = CUR_DIR + "/kerberos.db"

DEFAULT_KEY = ""

AUTH_KEY = KEY_DIR + "/auth.key"
AUTH_CRT = KEY_DIR + "/auth.crt"
AUTH_PORT = 4433

TGS_KEY = KEY_DIR + "/tgs.key"
TGS_CRT = KEY_DIR + "/tgs.crt"
TGS_PORT = 4434

SERVICES = {
	### [id, ACL] ###
	"Finance" : [0, [1, 2]],
	"Management" : [1, [1]], 
	"Human Resources" : [2, [2]]
}

USER_LIST = [
	{
	    "uid": 1,
	    "uname": "Dodo",
	    "sid": 2,
	    "addr": "10.30.0.1",
	    "ticket_expr": "07/10/2018"
	}, 

	{
	    "uid": 2,
	    "uname": "Hodo",
	    "sid": 1,
	    "addr": "",
	    "ticket_expr": "11/13/2017"
	}
]

