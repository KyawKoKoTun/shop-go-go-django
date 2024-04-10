from django.contrib import admin
from .models import *

class ItemInline(admin.StackedInline):
    model = Item
    extra = 0
    can_delete = False

class OrderStatusFilter(admin.SimpleListFilter):
    title = 'Order Status'
    parameter_name = 'status'

    def lookups(self, request, model_admin):
        return (
            ('pending', 'Pending'),
            ('paid', 'Paid'),
            ('canceled', 'Canceled'),
            ('delivered', 'Delivered')
        )

    def queryset(self, request, queryset):
        if self.value() == 'pending':
            return queryset.filter(status='pending')
        elif self.value() == 'paid':
            return queryset.filter(status='paid')
        elif self.value() == 'canceled':
            return queryset.filter(status='canceled')
        elif self.value() == 'delivered':
            return queryset.filter(status='delivered')
        
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    inlines = [ItemInline]
    search_fields = ['product__name', 'order__user']
    list_filter = [OrderStatusFilter]
    