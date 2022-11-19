from abc import abstractmethod
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.forms import model_to_dict

# Create your models here.
class user(AbstractUser):
    ci = models.CharField(max_length=150, verbose_name='CI')


    def toJSON(self):
        item = model_to_dict(self, exclude=['password', 'groups', 'user_permissions'])
        item['last_login'] = self.last_login.strftime('%Y-%m-%d')
        item['date_joined'] = self.date_joined.strftime('%Y-%m-%d')
        return item
