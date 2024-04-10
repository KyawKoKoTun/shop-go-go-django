from django.db import models
from django.contrib.auth.models import AbstractUser
from .managers import *
from userdata.models import *

class User(AbstractUser):
    username = models.CharField(unique=False, max_length=256)
    email = models.CharField(unique=True, max_length=256)
    two_factor_auth = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    
    objects = CustomUserManager()
    
    def __str__(self):
        return f'{self.email} - {self.username}'