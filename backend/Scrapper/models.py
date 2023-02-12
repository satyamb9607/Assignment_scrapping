from django.db import models

# Create your models here.

from django.db import models

class Crypto(models.Model):
    name = models.CharField( max_length=200)
    price = models.CharField(max_length=100)
    percent_1h = models.CharField(max_length=100)
    percent_24h =models.CharField(max_length=100)
    percent_7d = models.CharField(max_length=100)
    market_cap = models.CharField(max_length=100)
    volume_24h = models.CharField(max_length=100)
    circulating_supply = models.CharField(max_length=100)

    def __str__(self):
        return self.name
