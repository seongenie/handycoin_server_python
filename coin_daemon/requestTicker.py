# !/usr/bin/env python

import daemon
import sys
import logging
import urllib2
import json
import time
import tickerService


from time import sleep
from datetime import datetime

def createTimeStamp(datestr, format="%Y-%m-%d %H:%M:%S"):
    return time.mktime(time.strptime(datestr, format))

logging.basicConfig()

file_logger = logging.FileHandler("/tmp/daemon_" + sys.argv[1] +".log ", "w")

logger = logging.getLogger()
logger.addHandler(file_logger)
logger.setLevel(logging.INFO)

exchange_url = {}
exchange_url['poloniex'] = 'https://poloniex.com/public?command=returnTicker'
exchange_url['coinone'] = 'https://api.coinone.co.kr/ticker?currency=all'
exchange_url['bithumb'] = 'https://api.bithumb.com/public/ticker/all'

class restFulApi:
    def __init__(self, command):
        self.exch = command

    def api_query(self, req={}):
        ret = urllib2.urlopen(urllib2.Request(exchange_url[self.exch]))
        self.jObj = json.loads(ret.read())
        return self.jObj

    def request(self):
        return self.api_query()

    def returnCommon(self):
        if (self.exch == "bithumb"):
            return tickerService.bithumb()
        if (self.exch == "coinone"):
            return tickerService.coinone()
        if (self.exch == "poloniex"):
            return tickerService.poloniex()

with daemon.DaemonContext(files_preserve=[file_logger.stream.fileno()]):
    argu = sys.argv[1]
    restFul = restFulApi(argu)
    common = restFul.returnCommon()
    while True:
        jObj = restFul.request()
        common.setJsonObj(jObj)
        message = common.jsonParse()
        time = str(datetime.now())
        logger.info(time + ' : ' + message)
        sleep(5)
