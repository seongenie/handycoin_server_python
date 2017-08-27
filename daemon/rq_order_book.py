# !/usr/bin/env python

import daemon
import sys
import logging
import urllib
import signal
import urllib2
import json
import time
import odBook_Parser
import dbConnect

import hmac,hashlib

from time import sleep
from datetime import datetime

def createTimeStamp(datestr, format="%Y-%m-%d %H:%M:%S"):
    return time.mktime(time.strptime(datestr, format))

logging.basicConfig()

file_logger = logging.FileHandler("/tmp/dmon_order_book" + sys.argv[1] +".log", "w")

logger = logging.getLogger()
logger.addHandler(file_logger)
logger.setLevel(logging.INFO)

exchange_url = {}
#exchange_url['poloniex'] = 'https://poloniex.com/public?command=returnTicker'

exchange_url['coinone'] = 'https://api.coinone.co.kr/orderbook?currency='
exchange_url['bithumb'] = 'https://api.bithumb.com/public/orderbook/'

coin_list = {}
coin_list['bithumb'] = ['BTC', 'ETH', 'DASH', 'LTC', 'ETC', 'XRP']
coin_list['coinone'] = ['BTC', 'ETH', 'ETC', 'XRP']


class restFulApi:
    def __init__(self, command):
        self.exch = command

    def api_query(self, coin, req={}):
        ret = urllib2.urlopen(urllib2.Request(exchange_url[self.exch] + coin))
        self.jObj = json.loads(ret.read())
        return self.jObj

    def request(self, coin):
        return self.api_query(coin)

    def returnCommon(self):
        if (self.exch == "bithumb"):
            return odBook_Parser.bithumb()
        if (self.exch == "coinone"):
            return odBook_Parser.coinone()
        if (self.exch == "poloniex"):
            return odBook_Parser.poloniex()


with daemon.DaemonContext(files_preserve=[file_logger.stream.fileno()]):
    argu = sys.argv[1]
    restFul = restFulApi(argu)
    common = restFul.returnCommon()
    common.dbConnect(dbConnect.DBConnect())
    while True:
        for coin in coin_list[argu]:
            jObj = restFul.request(coin)
            common.setJsonObj(jObj)
            common.odBookParse()
            sleep(1)
        message = "RECEIVE SUCCESS"
        time = str(datetime.now())
        logger.info(time + ' : ' + message)
        sleep(1)
