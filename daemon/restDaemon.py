import os
import sys
import time
import urllib
import signal
import urllib2
import json
import time
import hmac,hashlib
import daemon
import logging
import logging.handlers
from time import sleep
from datetime import datetime

class Dummy:
    def write(self, s) :
        pass

if os.fork():
    os._exit(0)

os.setpgrp()
os.umask(0)
sys.stdin.close()
sys.stdout = Dummy()
sys.stderr = Dummy()


def createTimeStamp(datestr, format="%Y-%m-%d %H:%M:%S"):
    return time.mktime(time.strptime(datestr, format))


class poloniex:
    def __init__(self):
        pass

    def post_process(self, before):
        after = before
        # Add timestamps if there isnt one but is a datetime
        if ('return' in after):
            if (isinstance(after['return'], list)):
                for x in xrange(0, len(after['return'])):
                    if (isinstance(after['return'][x], dict)):
                        if ('datetime' in after['return'][x] and 'timestamp' not in after['return'][x]):
                            after['return'][x]['timestamp'] = float(createTimeStamp(after['return'][x]['datetime']))
        return after

    def api_query(self, command, req={}):
        if (command == "returnTicker" or command == "return24Volume"):
            ret = urllib2.urlopen(urllib2.Request('https://poloniex.com/public?command=' + command))
            return json.loads(ret.read())

    def returnTicker(self):
        return self.api_query("returnTicker")


# while True:
exchange = poloniex()
exchange.returnTicker()
print(3)
time.sleep(15)

