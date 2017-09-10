#_*_coding:utf-8_*_
from api.coinRepository import DBRepository
import json
class CoinService:
    def __init__(self):
        self.db = DBRepository.getInstance()

    def getOrderBook(self , exchange, coin):
        result = self.db.selectOrderBook(exchange, coin)
        return result


    def getTicker(self , request_body):
        #request_body = json.dumps({"bithumb":["BTC","ETH"],"coinone":["ETH"]})
        # tuple 형태로 request 거래이름와 코인이름 요청
        dict = json.loads(request_body)
        dict_set = {}
        for exchange_name in dict.keys() :
            for coin_name in dict[exchange_name]:
                dict_set.setdefault(exchange_name , [])
                dict_set[exchange_name] += [coin_name]

        print(dict_set)
        result = self.db.getTicker(dict_set)
        print(result)
        return result



    def getPosscoin(self):
        # 조회가능 코인 조회

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
