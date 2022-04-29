from django.db import models

# Create your models here.
class Stocks(models.Model):
    StockId=models.AutoField(primary_key=True)
    StockName=models.CharField(max_length=500)
    StockValue=models.FloatField()
