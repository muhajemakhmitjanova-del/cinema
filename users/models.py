from django.db import models
from django.contrib.auth.models import AbstractUser,PermissionManager

from .managers import UserManager
from phonenumber_field.modelfields import PhoneNumberField


class User(AbstractUser):
    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'
        ordering = ['-date_joined']
    
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True, verbose_name='Электронная почта', blank=True, null=True)
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True, verbose_name='Аватар')
    phone_number = PhoneNumberField(blank=True, null=True, verbose_name='Номер телефона')
    bio = models.TextField(verbose_name = 'о себе',null = True,blank = True)
    
    
    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return f'{self.email or self.first_name}'