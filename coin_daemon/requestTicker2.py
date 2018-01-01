# !/usr/bin/env python

import daemon
import sys
sys.path.append("/home/ubuntu/git_repository/server")
import logging
import urllib2
import json
import time
import tickerService2

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

exchange_url['coinnest'] = 'https://api.coinnest.co.kr/api/pub/ticker?coin='
hdr = {'User-Agent': 'Mozilla/5.0', 'referer' : 'http://m.naver.com'}

coin_list = {}
coin_list['coinnest'] = ['TRON']

class restFulApi:
    def __init__(self, command):
        self.exch = command

    def api_query(self, coin, req={}):
        ret = urllib2.urlopen(urllib2.Request(exchange_url[self.exch] + coin, headers=hdr))
        self.jObj = json.loads(ret.read())
        return self.jObj

    def request(self, coin):
        if self.exch == "coinnest" :
            return self.api_query(coin.lower())
        else :
            return self.api_query(coin)

    def returnCommon(self):
        if self.exch == "coinnest" :
            return tickerService2.coinnest()


# with daemon.DaemonContext(files_preserve=[file_logger.stream.fileno()]):
argu = sys.argv[1]
restFul = restFulApi(argu)
common = restFul.returnCommon()
    # while True:
for coin in coin_list[argu]:
    jObj = restFul.request(coin)
    common.setJsonObj(jObj)
    common.jsonParse(coin)
        # message = "RECEIVE SUCCESS"
        # time = str(datetime.now())
        # logger.info(time + ' : ' + message)
sleep(1)
