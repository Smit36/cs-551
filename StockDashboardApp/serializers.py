from rest_framework import serializers
from StockDashboardApp.models import Stocks

class StockSerializer(serializers.ModelSerializer):
    class Meta:
        model=Stocks
        fields=('stockId','stockName','userId')
