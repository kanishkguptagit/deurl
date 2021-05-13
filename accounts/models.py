from django.db import models
from django.contrib.auth.models import AbstractBaseUser

# Create your models here.

class UserProfile(AbstractBaseUser):
    email = models.EmailField(max_length=100, unique=True,)
    name = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']
    