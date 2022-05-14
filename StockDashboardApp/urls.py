from django.conf.urls import url
from django.urls import path, re_path
from StockDashboardApp import views

urlpatterns=[
    # path('admin/', admin.site.urls),
    path('stocks', views.stockApi),
    path('stocks/crypto', views.stockCryptoApi),
    path('portfolio', views.newPortfolio),
    path('portfolio/<str:id>', views.portfolioApi),
    
]