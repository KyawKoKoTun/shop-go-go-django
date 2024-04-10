from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Product(models.Model):
    name = models.CharField(max_length=1024, null=False, unique=True)
    image = models.ImageField(upload_to='product_images/', null=False)
    price = models.DecimalField(decimal_places=2, null=False, max_digits=12)
    discount = models.IntegerField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name} - MMK {self.price}'

class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='product_images/', null=False)
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f'Product Image {self.id} of {self.product.name}'



class ProductReview(models.Model):

    RATING_CHOICES = [
        (1, 'Rating 1'),
        (1, 'Rating 2'),
        (1, 'Rating 3'),
        (1, 'Rating 4'),
        (1, 'Rating 5'),
    ]
    
    user = models.ForeignKey(User, related_name='reviews', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    rating = models.IntegerField(choices=RATING_CHOICES, null=False)
    content = models.TextField(null=False)
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f'Product Review of {self.product.name} by {self.user.email}'