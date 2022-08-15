from core.erp.models import Category
from django.forms import *

class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = '__all__'