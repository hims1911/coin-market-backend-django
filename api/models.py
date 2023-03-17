from django.db import models
    


class Crypto(models.Model):
    id = models.AutoField(primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=50)
    price = models.CharField(max_length=20)
    change_1h = models.CharField(max_length=10)
    change_24h = models.CharField(max_length=10)
    change_7d = models.CharField(max_length=10)
    market_cap = models.CharField(max_length=20)
    volume_24h = models.CharField(max_length=30)
    circulating_supply = models.CharField(max_length=20)

    def __str__(self):
        return self.name
