
import json
from django.http.response import JsonResponse
import yfinance as yf
from StockDashboardApp.models import Stocks
from bson import ObjectId
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
#D10J66XZ7XGVJ5PZ

def stockApi(request,id=0):
    if request.method=='GET':
        cyrpto=["MSFT","TSLA","AAPL","AMZN","FB","NKE","PYPL","TWTR","COIN","SNAP"]
        result=[]
        for name in cyrpto:
            ticker = yf.Ticker(name)
            ticker_info={
                'name':ticker.info['shortName'],
                'symbol':ticker.info['symbol'],
                'logo':ticker.info['logo_url']
            }        
            result.append(ticker_info)
       
        return JsonResponse(result,safe=False)

@csrf_exempt 
def portfolioApi(request,id=0):
    if request.method=='GET':        
        stock=Stocks.objects.filter(userId=id).values()
        result=[]
        for key in stock:
            ticker = yf.Ticker(key['stockName'])
            ticker_info={
                'name':ticker.info['shortName'],
                'symbol':ticker.info['symbol'],
                'description':ticker.info['longBusinessSummary'],
                'price':ticker.info['currentPrice'],
                'open':ticker.info['regularMarketOpen'],
                'high':ticker.info['regularMarketDayHigh'],
                'low':ticker.info['dayLow'],
                'logo':ticker.info['logo_url']
            }        
            ticker_info['id']=str(key['_id'])
            result.append(ticker_info)
        return JsonResponse(result,safe=False)    
    
    elif request.method =='DELETE':
        stock=Stocks.objects.get(_id=ObjectId(id))
        stock.delete()
        return JsonResponse({"message":"Deleted"},safe=False)

@csrf_exempt 
def newPortfolio(request,id=0):
    if request.method == 'POST':
            stock_data = json.loads(request.body.decode("utf-8"))
            stockName=stock_data.get("stockName")
            stock=Stocks(userId=stock_data.get("userId"),stockName=stockName)
            stock.save()
            return JsonResponse({'message':"Inserted"},safe=False)

    
        
