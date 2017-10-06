from api.daemonRepository import DBRepository

class commonProcess:
    def __init__(self):
        pass

    def updatePrice(self, exchange, coin, first_price, last_price):
        DBRepository.getInstance().updatePrice(exchange, coin, first_price, last_price)

    def setJsonObj(self, jObj):
        self.jObj = jObj

    def updateOrderBook(self, exchange, coin, bid, ask):
        DBRepository.getInstance().updateOrderBook(exchange, coin, bid, ask)

    def orderBookParse(self, coin):
        self.coin = coin

class bithumb(commonProcess):
    def __init__(self):
        self.exchange = 'bithumb'

    def odBookParse(self, coin):
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

        return 'success'

class coinone(commonProcess):
    def __init__(self):
        self.exchange = 'coinone'

    def odBookParse(self, coin):


        if self.jObj['errorCode'] == "0" :
            ask = {}
            ask['tick'] = {}
            ask['qnty'] = {}

            bid = {}
            bid['tick'] = {}
            bid['qnty'] = {}
            coin = self.jObj['currency']
            for i in range(0, 5) :
                ask['tick'][i] = {}
                ask['qnty'][i] = {}
                bid['tick'][i] = {}
                bid['qnty'][i] = {}

                ask['tick'][i] = self.jObj['ask'][i]['price']
                ask['qnty'][i] = self.jObj['ask'][i]['qty']
                bid['tick'][i] = self.jObj['bid'][i]['price']
                bid['qnty'][i] = self.jObj['bid'][i]['qty']
            self.updateOrderBook(self.exchange, coin.upper(), bid, ask)

            return 'success'
        else :
            return 'failed'

class poloniex(commonProcess):
    def __init__(self):
        self.exchange = 'poloniex'

    def odBookParse(self, coin):
        ask = {}
        ask['tick'] = {}
        ask['qnty'] = {}

        bid = {}
        bid['tick'] = {}
        bid['qnty'] = {}
        for i in range(0, 5):
            ask['tick'][i] = {}
            ask['qnty'][i] = {}
            bid['tick'][i] = {}
            bid['qnty'][i] = {}

            ask['tick'][i] = self.jObj['asks'][i][0]
            ask['qnty'][i] = self.jObj['asks'][i][1]
            bid['tick'][i] = self.jObj['bids'][i][0]
            bid['qnty'][i] = self.jObj['bids'][i][1]
        self.updateOrderBook(self.exchange, coin, bid, ask)

        return 'success'