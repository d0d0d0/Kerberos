TYPE_SERVICE = (0, 'SERVICE')
TYPE_USER = (1, 'USER')
TYPE_AUTH = (2, 'AUTH')
TYPE_TGS = (3, 'TGS')

CREATE_SERVICE_TABLE = """
			CREATE TABLE IF NOT EXISTS service (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL); 
				"""
INSERT_SERVICE = """ 
			INSERT INTO service VALUES(?, ?)
				"""

CREATE_USER_TABLE = """ 
			CREATE TABLE IF NOT EXISTS user (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL); 
				"""

INSERT_USER = """ 
			INSERT INTO user VALUES(?, ?)
				"""

CREATE_AUTH_TABLE = """
			CREATE TABLE IF NOT EXISTS auth (
                uid INTEGER,
                sid INTEGER,
                addr TEXT,
                FOREIGN KEY(uid) REFERENCES user(id),
				FOREIGN KEY(sid) REFERENCES service(id)); 
				"""

INSERT_AUTH = """ 
			INSERT INTO auth VALUES(?, ?, ?)
				"""

IS_AUTH = """
			SELECT * FROM auth WHERE uid=? and sid=?
			"""

CREATE_TGS_TABLE = ""
INSERT_TGS = ""