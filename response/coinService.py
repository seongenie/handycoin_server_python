from api.coinRepository import DBRepository
class CoinService:
    def __init__(self):
        self.db = DBRepository.getInstance()

    def getOrderBook(self , coin, exchange):
        result = DBRepository.getInstance().selectOrderBook(coin, exchange)
        return result


    def getTicker(self , coins):
        pass
    def getPosscoin(self):
        result = self.db.getPossCoin()
        print result

    # for coin in coins :
    #
    # result = DBRepository.getInstance().selectTicker(coin, exchange)
    # return result
