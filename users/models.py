from django.db import models
from django.contrib.auth.models import AbstractUser,PermissionManager

from .managers import UserManager
from django.utils import timizone

class User(AbstractUser):
    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'
        ordering = ['-date_joined']
    
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True,verboose_name = 'Электронная почта', blank=True,null = True)

objects = UserManager()
USERNAME_FILED = 'email'
REQUIRED_FILEDS = []

def __str__(self):
    return f'{str(self.email) or self.firsT_name}'

