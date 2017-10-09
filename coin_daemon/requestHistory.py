# !/usr/bin/env python

import daemon
import sys
sys.path.append("/home/ubuntu/git_repository/server")
import logging
import urllib2
import json
import time
import historyService


from time import sleep
from datetime import datetime

def createTimeStamp(datestr, format="%Y-%m-%d %H:%M:%S"):
    return time.mktime(time.strptime(datestr, format))

logging.basicConfig()

file_logger = logging.FileHandler("/tmp/daemon_" + sys.argv[1] + ".log ", "w")

logger = logging.getLogger()
logger.addHandler(file_logger)
logger.setLevel(logging.INFO)

exchange_url = {}
exchange_url['poloniex'] = 'https://poloniex.com/public?command=returnTicker'
exchange_url['coinone'] = 'https://api.coinone.co.kr/trades?currency='
exchange_url['bithumb'] = 'https://api.bithumb.com/public/recent_transactions/' #BTC?count=10'

coin_list = {}
coin_list['poloniex'] = ['BTC', 'ETH', 'LTC', 'XRP', 'ETC', 'ZEC', 'NXT', 'STR', 'DASH' ,'XMR' ,'REP', 'BCH']
coin_list['bithumb'] = ['BTC', 'ETH', 'DASH', 'LTC', 'ETC', 'XRP', 'XMR', 'ZEC', 'BCH'];
coin_list['coinone'] = ['BTC', 'ETH', 'ETC', 'XRP', 'BCH', 'QTUM']

class restFulApi:
    def __init__(self, command):
        self.exch = command

    def api_query(self, coin, req={}):
        ret = urllib2.urlopen(urllib2.Request(exchange_url[self.exch] + coin))
        self.jObj = json.loads(ret.read())
        return self.jObj

    def request(self, coin):
        if self.exch == "bithumb" :
            return self.api_query(coin + "?count=10")
        elif self.exch == "polniex" :
            return self.api_query(coin)

    def returnCommon(self):
        if self.exch == "bithumb" :
            return historyService.bithumb()
        if self.exch == "coinone" :
            return historyService.coinone()
        if self.exch == "poloniex":
            return historyService.poloniex()


# with daemon.DaemonContext(files_preserve=[file_logger.stream.fileno()]):
argu = sys.argv[1]
restFul = restFulApi(argu)
common = restFul.returnCommon()
# while True:
for coin in coin_list[argu]:
    jObj = restFul.request(coin)
    common.setJsonObj(jObj)
    common.historyParse(coin)
message = "RECEIVE SUCCESS"
time = str(datetime.now())
logger.info(time + ' : ' + message)
sleep(1)

