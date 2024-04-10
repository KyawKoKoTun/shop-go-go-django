from rest_framework.generics import (
    ListAPIView, RetrieveAPIView, CreateAPIView, DestroyAPIView
)

from rest_framework.pagination import PageNumberPagination
from django_filters import rest_framework as filters
from rest_framework.permissions import IsAuthenticated

from .models import *
from .serializers import *

class DefaultPagination(PageNumberPagination):
    page_size = 20

class ProductFilter(filters.FilterSet):
    name = filters.CharFilter(field_name='name', lookup_expr='icontains')

    class Meta:
        model = Product
        fields = ['name']

class ProductListView(ListAPIView):
    filter_backends = [filters.DjangoFilterBackend]
    filterset_class = ProductFilter
    pagination_class = DefaultPagination
    serializer_class = ProductSerializer
    queryset = Product.objects.all().order_by('-created_at') 
    
class ProductSingleView(RetrieveAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()


class ReviewListView(ListAPIView):
    serializer_class = ProductReviewSerializer
    pagination_class = DefaultPagination

    def get_queryset(self):
        product_id = self.kwargs['product_id']  
        queryset = ProductReview.objects.filter(product_id=product_id).order_by('-created_at') 
        return queryset
    

class ReviewCreateView(CreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ProductReviewSerializer
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
    
    
class ReviewDeleteView(DestroyAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ProductReviewSerializer

    def get_queryset(self):
        return ProductReview.objects.filter(user=self.request.user)
    

class ProductImageListView(ListAPIView):
    serializer_class = ProductImageSerializer
    pagination_class = DefaultPagination

    def get_queryset(self):
        product_id = self.kwargs['product_id']  
        queryset = ProductImage.objects.filter(product_id=product_id).order_by('-created_at') 
        return queryset