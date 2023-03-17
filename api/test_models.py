from rest_framework.test import APITestCase
from .models import Crypto
from .serializers import CryptoCurrencySerializer

class CryptoModelTest(APITestCase):
    def setUp(self):
        self.crypto_data = {
            "name": "Bitcoin",
            "price": "45000.00",
            "change_1h": "-1.23",
            "change_24h": "2.34",
            "change_7d": "3.45",
            "market_cap": "800000000000",
            "volume_24h": "20000000000",
            "circulating_supply": "18000000"
        }
        self.crypto = Crypto.objects.create(**self.crypto_data)

    def test_crypto_str(self):
        self.assertEqual(str(self.crypto.name), "Bitcoin")

    def test_crypto_data(self):
        self.assertEqual(self.crypto.name, self.crypto_data['name'])
        self.assertEqual(self.crypto.price, self.crypto_data['price'])
        self.assertEqual(self.crypto.change_1h, self.crypto_data['change_1h'])
        self.assertEqual(self.crypto.change_24h, self.crypto_data['change_24h'])