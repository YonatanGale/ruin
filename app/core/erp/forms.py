from select import select
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

class MaterialsForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for form in self.visible_fields():
            form.field.widget.attrs['class'] = 'form-control'
            form.field.widget.attrs['autocomplete'] = 'off'
        self.fields['name'].widget.attrs['autofocus'] = True

    
    class Meta:
        model = Materials
        fields = '__all__'

        widgets = {
            'name': TextInput(
                attrs={
                    'placeholder' : 'Ingrese un nombre'
                }
            )

        }

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

class SaleForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for form in self.visible_fields():
            form.field.widget.attrs['class'] = 'form-control'
            form.field.widget.attrs['autocomplete'] = 'off'

        self.fields['cli'].widget.attrs['autofocus'] = True
        self.fields['cli'].widget.attrs['class'] = 'form-control select2'
        self.fields['cli'].widget.attrs['style'] = 'width: 100%'

        self.fields['date_joined'].widget.attrs = {
            'readonly': True,
            'autocomplete': 'off',
            'class': 'form-control datetimepicker-input',
            'id': 'date_joined',
            'data-target': '#date_joined',
            'data-toggle': 'datetimepicker',
        }

        self.fields['subtotal'].widget.attrs = {
            'readonly': True,
            'class': 'form-control'
        }

        self.fields['total'].widget.attrs = {
            'readonly': True,
            'class': 'form-control'
        }
    
    class Meta:
        model = Sale
        fields = '__all__'
        widgets = {
            'cli': Select(attrs={
                'class': 'form-control select2',
                'style': 'width: 100%'
            }),
            'date_joined': DateInput(format='%Y-%m-%d',
                                     attrs={
                                         'value': datetime.now().strftime('%Y-%m-%d'),
                                     }
                                     ),
            'iva': TextInput()
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
            ),
            'Birthday': DateInput(format='%Y-%m-%d',
                attrs={
                    'value': datetime.now().strftime('%Y-%m-%d'),
                }
            ),

        }

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

class SupplierForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for form in self.visible_fields():
            form.field.widget.attrs['class'] = 'form-control'
            form.field.widget.attrs['autocomplete'] = 'off'
        self.fields['names'].widget.attrs['autofocus'] = True
    
    class Meta:
        model = Supplier
        fields = '__all__'

        widgets = {
            'names': TextInput(
                attrs={
                    'placeholder' : 'Ingrese nombre del proveedor'
                }
            ),
            'surnames': TextInput(
                attrs={
                    'placeholder' : 'Ingrese apellido del proveedor'
                }
            ),

        }

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

class UnityForm(ModelForm):
    class Meta:
        model = Unity
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

search = CharField(widget=TextInput(attrs={
    'class': 'form-control',
    'placeholder': 'Ingrese una descripcion'
}))