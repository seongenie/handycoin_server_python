from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from api.dbConnect import DBConnect

@csrf_exempt
def message(request):

    if request.method == "POST":
        return JsonResponse({'message': {'text' : request.POST['content']}})
    else :
        return HttpResponse("ERROR" )

@csrf_exempt
def keyboard(request):
    arr = ['1. bithumb', '2. coinone', '3. poloniex']
    if request.method == "GET":
        return JsonResponse({'type': 'buttons', 'buttons' : arr})

@csrf_exempt
def ticker(request):
    conn = DBConnect.getInstance().getConnection()

    return JsonResponse({'coin': '500'})


