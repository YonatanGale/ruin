from turtle import textinput
from core.erp.models import *
from django.forms import *

class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = '__all__'

        widgets = {
            'name': TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder' : 'Ingrese un nombre',
                    'autocomplete': 'off'
                }
            )

        }

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

        widgets = {
            'name': TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder' : 'Ingrese un nombre',
                    'autocomplete': 'off'
                }
            )

        }