from api.daemonRepository import DBRepository

class commonProcess:
    def __init__(self):
        pass

    def selectHistory(self, exchange, coin):
        return DBRepository.getInstance().selectRecentHistory(exchange, coin)

    def insertHistory(self, exchange, coin, price, qnty, transaction_date):
        return DBRepository.getInstance().insertHistory(exchange, coin, price, qnty, transaction_date)

    def setJsonObj(self, jObj):
        self.jObj = jObj

    def jsonParse(self):
        pass


class bithumb(commonProcess):
    def __init__(self):
        self.exchange = 'bithumb'


    def historyParse(self, coin):
        recent_date = self.selectHistory(self.exchange, coin)
        i = 0
        if self.jObj['status'] != "0000" :
            return ('receive ERROR! ' + self.jObj['status'])
        for data in self.jObj['data'] :
            if recent_date < data['transaction_date'] :
                price = self.jObj['data'][i]['price']
                qnty = self.jObj['data'][i]['units_traded']
                transaction_date = self.jObj['data'][i]['transaction_date']
                self.insertHistory(self.exchange, coin, price, qnty, transaction_date)
            else :
                break
        # while (recent_date < self.jObj['data'][i]['transaction_date']):
        #     price = self.jObj['data'][i]['price']
        #     qnty = self.jObj['data'][i]['units_traded']
        #     transaction_date = self.jObj['data'][i]['transaction_date']
        #     self.insertHistory(self.exchange, coin, price, qnty, transaction_date )
        #     i = i + 1
        return recent_date


class poloniex(commonProcess):
    def __init__(self):
        self.exchange = 'poloniex'


    def historyParse(self, coin):
        recent_date = self.selectHistory(self.exchange, coin)
        i = 0
        if self.jObj['status'] != "0000" :
            return ('receive ERROR! ' + self.jObj['status'])

        while (recent_date < self.jObj['data'][i]['transaction_date'] or recent_date == 0):
            price = self.jObj['data'][i]['price']
            qnty = self.jObj['data'][i]['units_traded']
            transaction_date = self.jObj['data'][i]['transaction_date']
            self.insertHistory(self.exchange, coin, price, qnty, transaction_date )
            i = i + 1
        return recent_date

class coinone(commonProcess):
    def __init__(self):
        self.exchange = 'coinone'


    def historyParse(self, coin):
        recent_date = self.selectHistory(self.exchange, coin)
        i = 0
        if self.jObj['status'] != "0000" :
            return
        while (recent_date > self.jObj['data'][i]['transaction_date']):
            price = self.jObj['data'][i]['price']
            qnty = self.jObj['data'][i]['units_traded']
            transaction_date = self.jObj['data'][i]['transaction_date']
            self.insertHistory(self.exchange, coin, price, qnty, transaction_date )
        return 'success'