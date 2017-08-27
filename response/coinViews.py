from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import coinService

@csrf_exempt
def getTicker(request) :
    if request.method == "POST":
        orderBook = coinService.getTicker("~~~~~~")
        # 로직 구현
        #
        #
        # return JsonResponse({          })
    else:
        return HttpResponse("ERROR")



@csrf_exempt
def getOrderBook(request) :
    if request.method == "GET":
        orderBook = coinService.getOrderBook(request.GET['exchange'], request.GET['coin'])
        # 로직 구현
        #
        #
        # return JsonResponse({          })
    else:
        return HttpResponse("ERROR")

