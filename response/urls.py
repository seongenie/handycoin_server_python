from django.conf.urls import url

import coinViews


urlpatterns =[
    url(r'^posscoin$' , coinViews.posscoin , name="posscoin"),
    url(r'^ticker$' , coinViews.ticker , name="ticker"),
    url(r'^orderbook$', coinViews.orderbook , name="orderbook"),
]