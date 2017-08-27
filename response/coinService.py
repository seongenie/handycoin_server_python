from api.coinRepository import DBRepository

def getOrderBook(coin, exchange):
    result = DBRepository.getInstance().selectOrderBook(coin, exchange)
    return result


def getTicker(coins):
    pass
    # for coin in coins :
    #
    # result = DBRepository.getInstance().selectTicker(coin, exchange)
    # return result
