from abc import abstractmethod
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.forms import model_to_dict

# Create your models here.
class user(AbstractUser):
    ci = models.CharField(max_length=150, verbose_name='CI')


    def toJSON(self):
        item = model_to_dict(self, exclude=['password', 'groups', 'user_permissions', 'last_login'])
        if self.last_login:
            item['last_login'] = self.last_login.strftime('%Y-%m-%d')
        item['date_joined'] = self.date_joined.strftime('%Y-%m-%d')
        return item

    def save(self, *args, **kwargs):
        if self.pk is None:
            self.set_password(self.password)
        super().save(*args, **kwargs)