import pymysql
import decimal

class DBConnect:
    def __init__(self):
        dbhost = "localhost"
        dbuser = "admin"
        dbpass = "escape"
        database = "coin"
        id ="tinyaaa"

        self.conn = pymysql.connect(dbhost, dbuser, dbpass, database, charset='utf8')

    def getConnection(self):
        return self.conn 

    def updatePrice(self, exchange, coin, firstPrice, lastPrice):
        curs = self.conn.cursor()
        curs.execute("""UPDATE COIN_PRICE 
                        SET OPEN_PRICE= %s, LAST_PRICE= %s , UPDATE_TIME=CURTIME() 
                        WHERE EXCHANGE= %s  and COIN= %s 
                     """, (firstPrice, lastPrice, exchange, coin))
        self.conn.commit()

    def updateOrderBook(self, exchange, coin, bid, ask):
        curs = self.conn.cursor()

        for i in range(0,5) :
            curs.execute("""UPDATE ORDER_BOOK
                            SET TICK = %s
                              , QNTY = %s
                            WHERE IDX = %s AND BID_ASK = 'BID' AND EXCHANGE = %s AND COIN = %s
                         """, (bid['tick'][i] , bid['qnty'][i], i+1, exchange, coin))

        for i in range(0,5) :
            curs.execute("""UPDATE ORDER_BOOK
                            SET TICK = %s
                              , QNTY = %s
                            WHERE IDX = %s AND BID_ASK = 'ASK' AND EXCHANGE = %s AND COIN = %s
                         """, (ask['tick'][i] , ask['qnty'][i], i+1, exchange, coin))

        self.conn.commit()
    def closeConnection(self):
        self.conn.close()
