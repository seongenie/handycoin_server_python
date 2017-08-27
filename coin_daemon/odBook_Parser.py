import api.dbConnect

class commonProcess:
    def __init__(self):
        pass
    def dbConnect(self, DB):
        self.DB = DB

    def updatePrice(self, exchange, coin, first_price, last_price):
        self.DB.updatePrice(exchange, coin, first_price, last_price)

    def setJsonObj(self, jObj):
        self.jObj = jObj

    def updateOrderBook(self, exchange, coin, bid, ask):
        self.DB.updateOrderBook(exchange, coin, bid, ask)

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
        self.DB.updateOrderBook(self.exchange, coin, bid, ask)
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
