import dbConnect

class commonProcess:
    def __init__(self):
        pass
    def dbConnect(self, DB):
        self.DB = DB

    def updatePrice(self, exchange, coin, first_price, last_price):
        self.DB.updatePrice(exchange, coin, first_price, last_price)

    def setJsonObj(self, jObj):
        self.jObj = jObj

    def jsonParse(self):
        pass

class bithumb(commonProcess):
    def __init__(self):
        self.coins = ['BTC', 'ETH', 'DASH', 'LTC', 'ETC', 'XRP'];
        self.exchange = 'bithumb'

    def jsonParse(self):
        ret_arr = {}
        ret_arr['exchange'] = self.exchange
        for coin in self.coins:
            first_price = self.jObj['data'][coin]['opening_price']
            last_price = self.jObj['data'][coin]['closing_price']
            self.updatePrice(self.exchange, coin, first_price, last_price)
        return 'success'

class coinone(commonProcess):
    def __init__(self):
        self.coins = ['BTC', 'ETH', 'ETC', 'XRP']
        self.exchange = 'coinone'

    def jsonParse(self):
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

    def jsonParse(self):
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
