from django.urls import path
from .views import *

urlpatterns = [
    path('orders/submit/', OrderSubmitView.as_view(), name='submit-order'),
    path('orders/update/', OrderUpdateView.as_view(), name='update-order'),
    path('orders/', OrderListView.as_view(), name='order-list'),
    path('orders/<int:pk>/', OrderDetailView.as_view(), name='order-single'),
]