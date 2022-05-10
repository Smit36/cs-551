
from django.http.response import JsonResponse
import yfinance as yf

# Create your views here.
#D10J66XZ7XGVJ5PZ
def stockCryptoApi(request,id=0):
    if request.method=='GET':
        cyrpto=["ETH-USD","BTC-USD","BNB-USD","SOL-USD",'ADA-USD','XRP-USD']
        result=[]
        for name in cyrpto:
            ticker = yf.Ticker(name)
            ticker_info={
                'name':ticker.info['name'],
                'description':ticker.info['description'],
                'price':ticker.info['regularMarketPrice'],
                'open':ticker.info['regularMarketOpen'],
                'high':ticker.info['regularMarketDayHigh'],
                'low':ticker.info['regularMarketDayLow']
            }        
            result.append(ticker_info)
       
        return JsonResponse(result,safe=False)

def stockApi(request,id=0):
    if request.method=='GET':
        cyrpto=["MSFT","TSLA","AAPL","AMZN","FB"]
        result=[]
        for name in cyrpto:
            ticker = yf.Ticker(name)
            ticker_info={
                'name':ticker.info['shortName'],
                'description':ticker.info['longBusinessSummary'],
                'price':ticker.info['currentPrice'],
                'open':ticker.info['regularMarketOpen'],
                'high':ticker.info['regularMarketDayHigh'],
                'low':ticker.info['dayLow'],
                'logo':ticker.info['logo_url']
            }        
            result.append(ticker_info)
       
        return JsonResponse(result,safe=False)