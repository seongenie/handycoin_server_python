import pymysql
import decimal

class DBConnect:
    def __init__(self):
        dbhost = "localhost"
        dbuser = "admin"
        dbpass = "escape"
        database = "coin"

        self.conn = pymysql.connect(dbhost, dbuser, dbpass, database, charset='utf8')

    def getConnection(self):
        return self.conn


    def closeConnection(self):
        self.conn.close()
