from django.urls import path
from .views import GetCoinClass, CoinListCreateAPIView

app_name = 'crypto'

urlpatterns = [
    path('coin/', CoinListCreateAPIView.as_view(), name='coin-list'),
    path('get/', GetCoinClass.as_view(), name='coin-get'),
]
