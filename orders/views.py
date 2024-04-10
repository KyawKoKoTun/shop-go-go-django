from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import PageNumberPagination

from .models import Order
from .serializers import OrderSerializer, OrderUpdateSerializer

class DefaultPagination(PageNumberPagination):
    page_size = 20
    
class OrderSubmitView(generics.CreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]
    
class OrderListView(generics.ListAPIView):
    pagination_class = PageNumberPagination
    serializer_class = OrderSerializer
    
    def get_queryset(self):
        return Order.objects.filter(user=self.request.user)
    
class OrderDetailView(generics.RetrieveAPIView):
    serializer_class = OrderSerializer
    
    def get_queryset(self):
        return Order.objects.filter(user=self.request.user)
    
class OrderUpdateView(generics.UpdateAPIView):
    serializer_class = OrderUpdateSerializer
    
    def get_queryset(self):
        return Order.objects.filter(user=self.request.user)
    