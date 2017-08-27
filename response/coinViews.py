

from django.http import JsonResponse
from api.dbConnect import DBConnect

def posscoin(request):
    #create db
    db = DBConnect()
    rows = db.selectQuery("""
                    SELECT *
                    FROM EXCHANGE_COIN
                    """)
    print type(rows)
    return JsonResponse({'result' : 'success'});




