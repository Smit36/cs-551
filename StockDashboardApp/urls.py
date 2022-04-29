from django.conf.urls import url
from StockDashboardApp import views

urlpatterns=[
    url(r'^stocks$',views.stockApi),
    url(r'^stocks/([0-9]+)$',views.stockApi)
]