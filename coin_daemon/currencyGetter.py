#!/usr/bin/python

import urllib2
import json

import sys
sys.path.append("/Users/seongjinlee/PycharmProjects/coin_server")

from api.daemonRepository import DBRepository

class CurrencyGetter:
    url = 'http://www.apilayer.net/api/live?access_key=4a6efbfeac2e4b788c9fe8668d1248f0&currencies='
    def getCurrency(self, currency):
        url = self.url + currency
        iso = "USD" + currency
        ret = urllib2.urlopen(urllib2.Request(url))
        jObj = json.loads(ret.read())
        if jObj['success'] == True :
            print True
            price = jObj['quotes'][iso]
            DBRepository.getInstance().updateCurrency("USD", currency, price)

if __name__ == "__main__" :
    currencyGetter = CurrencyGetter()
    currencyGetter.getCurrency(sys.argv[1])
    print "success"