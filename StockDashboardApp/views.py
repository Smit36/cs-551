from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from rest_framework.response import Response
import yfinance as yf



from StockDashboardApp.models import Stocks
from StockDashboardApp.serializers import StockSerializer

# Create your views here.
#D10J66XZ7XGVJ5PZ
def stockApi(request,id=0):
    if request.method=='GET':
        msft = yf.Ticker("MSFT")
        return JsonResponse(msft.info)