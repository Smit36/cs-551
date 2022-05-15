from djongo import models

# Create your models here.
class Stocks(models.Model):
    _id=models.ObjectIdField()
    userId=models.CharField(max_length=500)
    stockName=models.CharField(max_length=500)

