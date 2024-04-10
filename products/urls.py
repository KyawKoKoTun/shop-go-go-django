from .views import *
from django.urls import path

urlpatterns = [
    path('products/', ProductListView.as_view(), name='product-list'),
    path('products/<int:pk>/', ProductSingleView.as_view(), name='product-single'),
    path('products/<int:product_id>/images', ProductImageListView.as_view(), name='product-images-list'),
    path('products/<int:product_id>/reviews', ProductImageListView.as_view(), name='product-images-list'),
]