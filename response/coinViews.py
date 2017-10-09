#_*_coding:utf-8_*_
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from coinService import CoinService

coinService = CoinService()
@csrf_exempt
def ticker(request) :
    if request.method == "POST":
         json_ticker = coinService.getTicker(request.body)
        # 로직 구현
        #
        #
        # return JsonResponse({          })
         return JsonResponse(json_ticker)
    elif request.method == "GET" :
        json_ticker = coinService.getTicker(request.body)
        return JsonResponse(json_ticker)
    else:
        return HttpResponse("ERROR")



@csrf_exempt
def orderbook(request) :
    if request.method == "GET":
        orderBook = coinService.getOrderBook(request.GET['exchange'], request.GET['coin'])
        return JsonResponse(orderBook)
        # 로직 구현
        #
        #
        # return JsonResponse({          })
    else:
        return HttpResponse("ERROR")

def posscoin(request):
    if request.method == "GET":
        json_poss_coin = coinService.getPosscoin()
        return JsonResponse(json_poss_coin)
    else:
        return HttpResponse("ERROR")


@csrf_exempt
def tradeHistory(request) :
    if request.method == "GET":
        history = coinService.getTradeHistory(request.GET['exchange'], request.GET['coin'])
        return JsonResponse(history)
        # 로직 구현
        #
        #
        # return JsonResponse({          })
    else:
        return HttpResponse("ERROR")
