from rest_framework import serializers
from StockDashboardApp import Stocks

class StockSerializer(serializers.ModelSerializer):
    class Meta:
        model=Stocks
        fields=('StockId','StockName','StockValue')
