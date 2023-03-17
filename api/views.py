from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import generics
from .models import Crypto
from .serializers import CryptoCurrencySerializer

# @api_view(['POST'])
# def create_coin_stats(request):
#     for each_coin in request.data:
#         serializer = CryptoCurrencySerializer(data=each_coin)
#         if serializer.is_valid():
#             serializer.save()
#         else:
#             return Response(serializer.errors, status=400)
        
#     # after the succesful execution return the results    
#     return Response(serializer.data, status=201)    


class CoinListCreateAPIView(generics.ListCreateAPIView):
    queryset = Crypto.objects.all()
    serializer_class = CryptoCurrencySerializer

    def create(self, request, *args, **kwargs):
        coins_data = request.data
        coins_serializer = self.get_serializer(data=coins_data, many=True)
        coins_serializer.is_valid(raise_exception=True)
        coins = coins_serializer.save()

        return Response(coins_serializer.data, status=201)

class GetCoinClass(generics.ListAPIView):
    queryset = Crypto.objects.all() #self.queryset.filter(node_id=self.kwargs.get('node_pk')).order_by('-timestamp')[:1]
    serializer_class = CryptoCurrencySerializer
    
    # fetching the latest 10 entries
    def get_queryset(self):
        return self.queryset.filter().order_by('-created_at')[:10]
    
    
