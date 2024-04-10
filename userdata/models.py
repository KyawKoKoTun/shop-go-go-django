from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class UserData(models.Model):
    user = models.OneToOneField(User, related_name='userdata', on_delete=models.CASCADE)
    phone = models.CharField(max_length=20)
    date_of_birth = models.DateField(null=True, blank=True)

    def __str__(self):
        return f'User Data of {self.user.email}'

class ShippingAddress(models.Model):
    user = models.ForeignKey(User, related_name='shipping_addresses', on_delete=models.CASCADE)
    address = models.CharField(max_length=1024)

    def __str__(self):
        return f'Shipping Address of {self.user.email}'