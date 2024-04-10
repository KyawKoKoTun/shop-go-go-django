from django.contrib import admin
from .models import *

class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1

class ProductReviewInline(admin.StackedInline):
    model = ProductReview
    extra=0

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductImageInline, ProductReviewInline]
    list_display = ['name', 'price', 'discount']
    search_fields = ['name']