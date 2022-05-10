from django.conf.urls import url
from django.urls import path, re_path
from StockDashboardApp import views

urlpatterns=[
    # path('admin/', admin.site.urls),
    re_path(r'^stocks/$', views.stockApi),
    re_path(r'^stocks/crypto$', views.stockCryptoApi),
]