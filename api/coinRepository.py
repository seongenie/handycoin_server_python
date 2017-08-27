from api.dbConnect import DBConnect

class DBRepository:
    INSTANCE = None

    def __init__(self):
        pass

    @classmethod
    def getInstance(cls): # type : () -> DBRepository
        if cls.INSTANCE is None:
            cls.INSTANCE = DBRepository()
        return cls.INSTANCE

    def selectTicker(self):
        result = DBConnect.getInstance().executeQuery(
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