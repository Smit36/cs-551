from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from StockDashboardApp.models import Stocks
from StockDashboardApp.serializers import StockSerializer
# Create your views here.

def stockApi(request,id=0):
    if request.method=='GET':
        stocks=Stocks.objects.all()
        stocks_serializer=StockSerializer(stocks,many=True)
        return JsonResponse(stocks_serializer.data,safe=False)