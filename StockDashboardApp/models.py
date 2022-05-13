from django.db import models

# Create your models here.
class Stocks(models.Model):
    stockId=models.AutoField(primary_key=True)
    userId=models.CharField(max_length=500)
    stockName=models.CharField(max_length=500)

