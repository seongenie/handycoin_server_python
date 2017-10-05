from api.daemonRepository import DBRepository

class commonProcess:
    def __init__(self):
        pass

    def updatePrice(self, exchange, coin, first_price, last_price, max_price, min_price):
        DBRepository.getInstance().updatePrice(exchange, coin, first_price, last_price, max_price, min_price)

    def setJsonObj(self, jObj):
        self.jObj = jObj

    def jsonParse(self):
        pass

class bithumb(commonProcess):
    def __init__(self):
        self.coins = ['BTC', 'ETH', 'DASH', 'LTC', 'ETC', 'XRP', 'XMR', 'ZEC', 'BCH'];
        self.exchange = 'bithumb'

    def jsonParse(self):
        ret_arr = {}
        ret_arr['exchange'] = self.exchange
        for coin in self.coins:
            first_price = self.jObj['data'][coin]['opening_price']
            last_price = self.jObj['data'][coin]['closing_price']
            max_price = self.jObj['data'][coin]['max_price']
            min_price = self.jObj['data'][coin]['min_price']
            self.updatePrice(self.exchange, coin, first_price, last_price, max_price, min_price)
        return 'success'

class coinone(commonProcess):
    def __init__(self):
        self.coins = ['BTC', 'ETH', 'ETC', 'XRP', 'BCH', 'QTUM']
        self.exchange = 'coinone'

    def jsonParse(self):
        ret_arr = {}
        ret_arr['exchange'] = self.exchange
        for coin in self.coins:
            first_price = self.jObj[coin.lower()]['first']
            last_price = self.jObj[coin.lower()]['last']
            max_price = self.jObj[coin.lower()]['high']
            min_price = self.jObj[coin.lower()]['low']
            self.updatePrice(self.exchange, coin, first_price, last_price, max_price, min_price)
        return 'success'

class poloniex(commonProcess):
    def __init__(self):
        self.coins = ['BTC', 'ETH', 'LTC', 'XRP', 'ETC', 'ZEC', 'NXT', 'STR', 'DASH' ,'XMR' ,'REP', 'BCH']
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
            max_price = self.jObj[ccoin]['high24hr']
            min_price = self.jObj[ccoin]['low24hr']
            self.updatePrice(self.exchange, coin, first_price, last_price, max_price, min_price)
        return 'success'
