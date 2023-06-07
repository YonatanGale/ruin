from abc import abstractmethod
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.forms import model_to_dict
from crum import get_current_request


# Create your models here.
class user(AbstractUser):
    ci = models.CharField(max_length=150, verbose_name='CI')


    def toJSON(self):
        item = model_to_dict(self, exclude=['password', 'user_permissions', 'last_login'])
        if self.last_login:
            item['last_login'] = self.last_login.strftime('%Y-%m-%d')
        item['date_joined'] = self.date_joined.strftime('%Y-%m-%d')
        item['full_name'] = self.get_full_name()
        item['groups'] = [{'id': g.id, 'name': g.name}for g in self.groups.all()]
        return item

    def get_group_session(self):
        try:
            request = get_current_request()
            groups = self.groups.all()
            if groups.exists():
                if 'group' not in request.session:
                    request.session['group'] = groups[0]
        except:
            pass

