from api.daemonRepository import DBRepository

class commonProcess:
    def __init__(self):
        pass

    def updatePrice(self, exchange, coin, first_price, last_price, max_price, min_price, volume):
        DBRepository.getInstance().updatePrice(exchange, coin, first_price, last_price, max_price, min_price, volume)

    def setJsonObj(self, jObj):
        self.jObj = jObj

    def jsonParse(self):
        pass

class coinnest(commonProcess):
    def __init__(self):
        self.exchange = 'coinnest'

    def jsonParse(self, coin):

        first_price = 0
        last_price = self.jObj['last']
        max_price = self.jObj['high']
        min_price = self.jObj['low']
        volume = self.jObj['vol']
        self.updatePrice(self.exchange, coin, first_price, last_price, max_price, min_price, volume)

        return 'success'

