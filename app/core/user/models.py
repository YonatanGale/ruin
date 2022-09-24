from abc import abstractmethod
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class user(AbstractUser):
    apodo = models.CharField(max_length=150, verbose_name='Apodo')