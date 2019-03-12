from django.db import models

# Create your models here.

class Stock(models.Model):
    def __str__(self):
        return self.ticker
    ticker = models.CharField(max_length=6)

class Price(models.Model):
    def __str__(self):
        return self.dollar_value
    ticker = models.ForeignKey(Stock, on_delete=models.CASCADE)
    dollar_value = models.CharField(max_length=10)

class TrackedStock(models.Model):
    def __str__(self):
        return self.ticker
    def get_ticker(self):
        return self.ticker
    owning_user = models.CharField(max_length=25)
    ticker = models.CharField(max_length=6)
