from api.dbRepository import DBRepository

class commonProcess:
    def __init__(self):
        pass

    def updatePrice(self, exchange, coin, first_price, last_price):
        DBRepository.getInstance().updatePrice(exchange, coin, first_price, last_price)

    def setJsonObj(self, jObj):
        self.jObj = jObj

    def updateOrderBook(self, exchange, coin, bid, ask):
        DBRepository.getInstance().updateOrderBook(exchange, coin, bid, ask)

    def odBookParse(self):
        pass

class bithumb(commonProcess):
    def __init__(self):
        self.exchange = 'bithumb'

    def odBookParse(self):
        ask = {}
        ask['tick'] = {}
        ask['qnty'] = {}
        bid = {}
        bid['tick'] = {}
        bid['qnty'] = {}
        coin = self.jObj['data']['order_currency']
        for i in range(0, 5) :
            ask['tick'][i] = {}
            ask['qnty'][i] = {}
            bid['tick'][i] = {}
            bid['qnty'][i] = {}

            ask['tick'][i] = self.jObj['data']['asks'][i]['price']
            ask['qnty'][i] = self.jObj['data']['asks'][i]['quantity']
            bid['tick'][i] = self.jObj['data']['bids'][i]['price']
            bid['qnty'][i] = self.jObj['data']['bids'][i]['quantity']

        self.updateOrderBook(self.exchange, coin, bid, ask)

        # def updateOrderBook(self, exchange, coin, bid, ask):
        #     for i in range(0,5) :
        #         curs.execute("""UPDATE ORDER_BOOK
        #                         SET TICK = %s
        #                           , QNTY = %s
        #                         WHERE IDX = %s AND BID_ASK = 'BID' AND EXCHANGE = %s AND COIN = %s
        #                      """, (bid['tick'][i] , bid['qnty'][i], i+1, exchange, coin))
        #
        #     for i in range(0,5) :
        #         curs.execute("""UPDATE ORDER_BOOK
        #                         SET TICK = %s
        #                           , QNTY = %s
        #                         WHERE IDX = %s AND BID_ASK = 'ASK' AND EXCHANGE = %s AND COIN = %s
        #                      """, (ask['tick'][i] , ask['qnty'][i], i+1, exchange, coin))









        return 'success'

class coinone(commonProcess):
    def __init__(self):
        self.coins = ['BTC', 'ETH', 'ETC', 'XRP']
        self.exchange = 'coinone'

    def odBookParse(self):
        ret_arr = {}
        ret_arr['exchange'] = self.exchange
        for coin in self.coins:
            first_price = self.jObj[coin.lower()]['first']
            last_price = self.jObj[coin.lower()]['last']
            self.updatePrice(self.exchange, coin, first_price, last_price)
        return 'success'

class poloniex(commonProcess):
    def __init__(self):
        self.coins = ['BTC', 'ETH', 'LTC', 'XRP', 'ETC', 'ZEC', 'NXT', 'STR', 'DASH' ,'XMR' ,'REP']
        self.exchange = 'poloniex'

    def odBookParse(self):
        ret_arr = {}
        ret_arr['exchange'] = self.exchange
        for coin in self.coins:
            ccoin = "USDT_" + coin
            change = float(self.jObj[ccoin]['percentChange'])
            change = 1 / (1 + change)
            last_price = self.jObj[ccoin]['last']
            first_price = change * float(last_price)
            self.updatePrice(self.exchange, coin, first_price, last_price)
        return 'success'
