#_*_coding:utf-8_*_
from api.dbConnect import DBConnect
import requests

class DBRepository:
    INSTANCE = None
    rate_url = 'http://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20yahoo.finance.xchange%20where%20pair%3D%22USDKRW%22&format=json&diagnostics=true&env=store%3A%2F%2Fdatatables.org%2Falltableswithkeys'

    def __init__(self):
        self.localSource = DBConnect.getInstance()

    @classmethod
    def getInstance(cls): # type : () -> DBRepository
        if cls.INSTANCE is None:
            cls.INSTANCE = DBRepository()
        return cls.INSTANCE

    def getTicker(self , args):
        # select문 수정
        result = ()
        for exchange_name in args.keys() :
            query = """ 
                 SELECT  TRIM(exchange) 
                           , TRIM(coin)
                           , open_price
                           , last_price
                     FROM COIN_PRICE 
                     WHERE EXCHANGE = %s 
                     AND COIN IN ( """
            for i in args[exchange_name][1:]:
                query += " %s, "
            query += " %s )"
            print(query)
            print((exchange_name,) + tuple(args[exchange_name]))
            result += self.localSource.selectQuery( query, (exchange_name,) + tuple(args[exchange_name]));
        result_dict ={'data' :{}}
        #request usd rate
        # response = requests.get(DBRepository.rate_url)
        # response.raise_for_status()
        # rate_data = response.json()
        result_dict['USDKRW'] = self.selectCurrency("USD", "KRW")
        for coin_tick in result:
            result_dict['data'].setdefault(coin_tick[0] , {})
            result_dict['data'][coin_tick[0]].setdefault(coin_tick[1] , {})
            result_dict['data'][coin_tick[0]][coin_tick[1]]['first_price'] = coin_tick[2]
            result_dict['data'][coin_tick[0]][coin_tick[1]]['last_price'] = coin_tick[3]

        return result_dict

    def selectCurrency(self, source, destination):
        """
        :param source: ex) USD
        :param destination: ex) KRW
        :return: 1140.24
        """
        result = self.localSource.selectQuery(
            """
            SELECT  price
            FROM    CURRENCY
            WHERE   source = %s
            AND     destination = %s
            """, (source, destination))
        ret = 0
        for price in result:
            ret = price[0]
        return ret


    def selectOrderBook(self, exchange, coin):
        result = self.localSource.selectQuery(
            """
            SELECT  TRIM(BID_ASK),
                    TICK ,
                    QNTY 
            FROM    ORDER_BOOK
            WHERE   EXCHANGE = %s
            AND     COIN = %s
            """, (exchange, coin))
        result_dict ={'data': {}}
        result_dict['data']['BID'] = {}
        result_dict['data']['ASK'] = {}


        for order_info in result :
            result_dict['data'][order_info[0]][order_info[1]] = order_info[2]

        result = self.localSource.selectQuery(
            """
            SELECT  open_price
                ,   last_price
                ,   max_price
                ,   min_price
                ,   volume
            FROM    COIN_PRICE
            WHERE   EXCHANGE = %s
            AND     COIN = %s """, (exchange, coin))

        for price in result :
            result_dict['data']['prev_price'] = price[0]
            result_dict['data']['last_price'] = price[1]
            result_dict['data']['max_price'] = price[2]
            result_dict['data']['min_price'] = price[3]
            result_dict['data']['volume'] = price[4]

        result_dict['data']['exchange'] = exchange
        result_dict['data']['coin'] = coin

        return result_dict

    def selectTradeHistory(self, exchange, coin, count):
        result_dict = {'data': {}}

        result = self.localSource.selectQuery(
            "select price, qnty, transaction_date, idx from transaction_history where exchange=%s and coin=%s order by idx desc limit %s"
            , (exchange, coin, count))

        i = 0
        for history in result :
            history_dict = {}
            history_dict['price'] = history[0]
            history_dict['qnty'] = history[1]
            history_dict['transaction_date'] = history[2]
            history_dict['index'] = history[3]
            result_dict['data'][i] = history_dict

        result_dict['exchange'] = exchange
        result_dict['coin'] = coin

        return result_dict

    def getPossCoin(self):
        result = self.localSource.selectQuery(
            """
            SELECT * FROM EXCHANGE_COIN ORDER BY EXCHANGE
            """ ,()
        )
        print str(result) + str(type(result))
        return result