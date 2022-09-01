from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200, unique=True)
    password = models.CharField(max_length=200)
    phone = models.CharField(max_length=12, null=True)
    username = None

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []




