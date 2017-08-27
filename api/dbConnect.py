import pymysql
import decimal

class DBConnect:
    INSTANCE = None

    def __init__(self):
        if self.INSTANCE is not None:
            raise ValueError("A instance already exists!")

        self.dbhost = "localhost"
        self.dbuser = "admin"
        self.dbpass = "escape"
        self.database = "coin"

    def getConnection(self):
        return pymysql.connect(self.dbhost, self.dbuser, self.dbpass, self.database, charset='utf8')

    @classmethod
    def getInstance(cls): # type : () -> DBConnect
        if cls.INSTANCE is None:
            cls.INSTANCE = DBConnect()
        return cls.INSTANCE

    def executeQuery(self, query, args):
        conn = self.getConnection()
        curs = conn.cursor()
        curs.execute(query, args)
        conn.commit()
        curs.close()
        conn.close()

    def selectQuery(self, query, args):
        conn = self.getConnection()
        curs = conn.cursor()
        curs.execute(query, args)
        result = curs.fetchall()
        curs.close()
        conn.close()
        return result
