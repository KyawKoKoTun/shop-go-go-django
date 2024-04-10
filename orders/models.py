from django.db import models
from django.contrib.auth import get_user_model
from products.models import Product
from userdata.models import ShippingAddress

User = get_user_model()

class Order(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('paid', 'Paid'),
        ('canceled', 'Canceled'),
        ('delivered', 'Delivered')
    ]
    user = models.ForeignKey(User, related_name='orders', on_delete=models.CASCADE)
    address = models.ForeignKey(ShippingAddress, related_name='orders', on_delete=models.SET_NULL, null=True)
    screenshot = models.ImageField(upload_to='payment_screenshots/', null=False)
    status = models.CharField(choices=STATUS_CHOICES, max_length=20, default='pending')
    
class Item(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='order_items', on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField(default=1)
    total = models.DecimalField(decimal_places=2, max_digits=10, blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.pk: 
            if self.product:
                discount_multiplier = 1 - (self.product.discount / 100)
                self.total = self.product.price * discount_multiplier * self.quantity
        super().save(*args, **kwargs)