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
        exclude = ['user_update', 'user_creation']
    
    def save(self, commit=True):
        data = {}
        form = super()
        try:
            if form.is_valid():
                form.save()
            else:
                data['error'] = form.errors
        except Exception as e:
            data['error'] = str(e)
        return data

class ProductForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for form in self.visible_fields():
            form.field.widget.attrs['class'] = 'form-control'
            form.field.widget.attrs['autocomplete'] = 'off'
        self.fields['name'].widget.attrs['autofocus'] = True
    
    class Meta:
        model = Product
        fields = '__all__'

        widgets = {
            'name': TextInput(
                attrs={
                    'placeholder' : 'Ingrese un nombre'
                }
            )

        }

class buyForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for form in self.visible_fields():
            form.field.widget.attrs['class'] = 'form-control'
            form.field.widget.attrs['autocomplete'] = 'off'
        self.fields['name'].widget.attrs['autofocus'] = True
    
    class Meta:
        model = buy
        fields = '__all__'

        widgets = {
            'mot': TextInput(
                attrs={
                    'placeholder' : 'Ingrese el motivo'
                }
            ),
            'descrip': TextInput(
                attrs={
                    'placeholder' : 'Ingrese la descripcion de la compra'
                }
            ),
            'prov_name': TextInput(
                attrs={
                    'placeholder' : 'Ingrese el nombre del proveedor'
                }
            ),
            'date_joined': TextInput(
                attrs={
                    'readonly' : True
                }
            ),

        }


class clientForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for form in self.visible_fields():
            form.field.widget.attrs['class'] = 'form-control'
            form.field.widget.attrs['autocomplete'] = 'off'
        self.fields['names'].widget.attrs['autofocus'] = True
    
    class Meta:
        model = Client
        fields = '__all__'

        widgets = {
            'names': TextInput(
                attrs={
                    'placeholder' : 'Ingrese nombre del cliente'
                }
            ),
            'surnames': TextInput(
                attrs={
                    'placeholder' : 'Ingrese apellido del cliente'
                }
            )

        }
