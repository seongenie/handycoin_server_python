from django.conf.urls import url

from . import coinViews


urlpatterns =[
    url(r'^posscoin$' , coinViews.posscoin , name="posscoin"),
    url(r'^ticker$' , coinViews.ticker , name="ticker"),
]