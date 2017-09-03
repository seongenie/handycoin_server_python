#_*_coding:utf-8_*_
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
        # 조회가능 코인 조회
        # tuple 형태로 응답
        result = self.db.getPossCoin()
        # json 형태로 변경
        json = {}
        for x in result:
            if x[0] in json.keys():
                json[x[0]] = json[x[0]] + [x[1]]
            else:
                json[x[0]] = [x[1]]
        return json


    # for coin in coins :
    #
    # result = DBRepository.getInstance().selectTicker(coin, exchange)
    # return result
