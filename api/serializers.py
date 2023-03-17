from rest_framework import serializers
from .models import Crypto

        
        

class CryptoCurrencySerializer(serializers.ModelSerializer):
    class Meta:
        model = Crypto
        fields = ['id', 'created_at', 'name', 'price', 'change_1h', 'change_24h', 'change_7d', 'market_cap', 'volume_24h', 'circulating_supply']

    
