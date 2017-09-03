from api.dbConnect import DBConnect

class DBRepository:
    INSTANCE = None

    def __init__(self):
        self.localSource = DBConnect()

    @classmethod
    def getInstance(cls): # type : () -> DBRepository
        if cls.INSTANCE is None:
            cls.INSTANCE = DBRepository()
        return cls.INSTANCE

    def selectTicker(self):
        result = self.localSource.getInstance().executeQuery(
            """
            SELECT  FROM ~~~ 
            """, ());
        return result

    def selectOrderBook(self, exchange, coin):
        result = DBConnect.getInstance().executeQuery(
            """
            SELECT  FROM ~~~ 
            """, ());
        return result

    def getPossCoin(self):
        result = self.localSource.selectQuery(
            """
            SELECT * FROM EXCHANGE_COIN ORDER BY EXCHANGE
            """ ,()
        )
        print str(result) + str(type(result))
        return result