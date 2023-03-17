from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Crypto
from .serializers import CryptoCurrencySerializer

class CoinListCreateAPIViewTest(APITestCase):
    def setUp(self):
        self.url = reverse('crypto:coin-list')
        self.crypto_data = [
            {
                "name": "Bitcoin",
                "price": "45000.00",
                "change_1h": "-1.23",
                "change_24h": "2.34",
                "change_7d": "3.45",
                "market_cap": "800000000000",
                "volume_24h": "20000000000",
                "circulating_supply": "18000000"
            },
            {
                "name": "Ethereum",
                "price": "3000.00",
                "change_1h": "0.45",
                "change_24h": "-1.23",
                "change_7d": "4.56",
                "market_cap": "400000000000",
                "volume_24h": "10000000000",
                "circulating_supply": "120000000"
            }
        ]

    def test_create_coins(self):
        response = self.client.post(self.url, data=self.crypto_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Crypto.objects.count(), 2)

    def test_invalid_data(self):
        invalid_crypto_data = [
            {
                "name": "Bitcoin",
                "price": "45000.00",
                "change_1h": "-1.23",
                "change_24h": "2.34",
                "change_7d": "3.45",
                "market_cap": "800000000000",
                "volume_24h": "20000000000",
                "circulating_supply": "18000000"
            },
            {
                "name": "Ethereum",
                "price": "3000.00",
                "change_1h": "0.45",
                "change_24h": "-1.23",
                "change_7d": "4.56",
                "market_cap": "400000000000",
                "volume_24h": "10000000000"
            }
        ]
        response = self.client.post(self.url, data=invalid_crypto_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)