from api.dbConnect import DBConnect

class DBRepository:
    INSTANCE = None

    def __init__(self):
        self.conn = DBConnect.getInstance()

    @classmethod
    def getInstance(cls): # type : () -> DBRepository
        if cls.INSTANCE is None:
            cls.INSTANCE = DBRepository()
        return cls.INSTANCE

    def updatePrice(self, exchange, coin, first_price, last_price, max_price, min_price):
        DBConnect.getInstance().executeQuery(
            """UPDATE COIN_PRICE 
               SET OPEN_PRICE= %s, LAST_PRICE= %s , MAX_PRICE= %s, MIN_PRICE= %s, UPDATE_TIME=CURTIME() 
               WHERE EXCHANGE= %s  and COIN= %s
            """, (first_price, last_price, max_price, min_price, exchange, coin))

    def updateOrderBook(self, exchange, coin, bid, ask):
        dbInstance = DBConnect.getInstance()
        for i in range(0,5) :
            dbInstance.executeQuery("""UPDATE ORDER_BOOK
                            SET TICK = %s
                              , QNTY = %s
                            WHERE IDX = %s AND BID_ASK = 'BID' AND EXCHANGE = %s AND COIN = %s
                         """, (bid['tick'][i] , bid['qnty'][i], i+1, exchange, coin))

        for i in range(0,5) :
            dbInstance.executeQuery("""UPDATE ORDER_BOOK
                            SET TICK = %s
                              , QNTY = %s
                            WHERE IDX = %s AND BID_ASK = 'ASK' AND EXCHANGE = %s AND COIN = %s
                         """, (ask['tick'][i] , ask['qnty'][i], i+1, exchange, coin))

    def updatePrice(self, exchange, coin, first_price, last_price):
        DBConnect.getInstance().executeQuery(
            """UPDATE COIN_PRICE 
               SET OPEN_PRICE= %s, LAST_PRICE= %s , UPDATE_TIME=CURTIME() 
               WHERE EXCHANGE= %s  and COIN= %s
            """, (first_price, last_price, exchange, coin))

    def updateCurrency(self, source, destination, price):
        DBConnect.getInstance().executeQuery(
            """UPDATE CURRENCY
               SET price= %s, update_time = CURTIME() 
               WHERE source = %s  and destination = %s
            """, (price, source, destination))