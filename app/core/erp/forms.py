from select import select
from datetime import datetime
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
            ),
            'user_create': TextInput(
                attrs={
                'type': 'hidden',
                'readonly': True,
                }
            ),
            'user_update': TextInput(
                attrs={
                'type': 'hidden',
                'readonly': True,
                }
            ),

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

class CategoryMaterialsForm(ModelForm):
    class Meta:
        model = CategoryMaterials
        fields = '__all__'

        widgets = {
            'name': TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder' : 'Ingrese un nombre',
                    'autocomplete': 'off'
                }
            ),
            'user_create': TextInput(
                attrs={
                'type': 'hidden',
                'readonly': True,
                }
            ),
            'user_update': TextInput(
                attrs={
                'type': 'hidden',
                'readonly': True,
                }
            ),
            'unity': Select()

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
            ),
            'date_joined': DateInput(format='%Y-%m-%d',
                attrs={
                    'readonly': True,
                    'value': datetime.now().strftime('%Y-%m-%d'),
                }
            ),
            'cate': Select(attrs={
                'class': 'form-control',
                'style': 'width: 100%'
            }),
            'user_create': TextInput(
                attrs={
                'type': 'hidden',
                'readonly': True,
                }
            ),
            'user_update': TextInput(
                attrs={
                'type': 'hidden',
                'readonly': True,
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
            ),
            'user_create': TextInput(
                attrs={
                'type': 'hidden',
                'readonly': True,
                }
            ),
            'user_update': TextInput(
                attrs={
                'type': 'hidden',
                'readonly': True,
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

class SaleForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['cli'].queryset = Client.objects.none()
        for form in self.visible_fields():
            form.field.widget.attrs['class'] = 'form-control'
            form.field.widget.attrs['autocomplete'] = 'off'


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
    methodpay = ModelChoiceField(queryset=MethodPay.objects.all(), widget=Select(attrs={
            'class': 'custom-select select2',
        }))
    typfund = ModelChoiceField(queryset=typeFunds.objects.none(), widget=Select(attrs={
            'class': 'custom-select select2',
        }))
    
    class Meta:
        model = Sale
        fields = '__all__'
        widgets = {
            'cli': Select(attrs={
                'class': 'custom-select select2',
            }),
            'user_create': TextInput(
                attrs={
                'type': 'hidden',
                'readonly': True,
                }
            ),
            'user_update': TextInput(
                attrs={
                'type': 'hidden',
                'readonly': True,
                }
            ),
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
            'date_joined': DateInput(format='%Y-%m-%d',
                attrs={
                    'readonly': True,
                    'value': datetime.now().strftime('%Y-%m-%d'),
                }
            ),
            'Birthday': DateInput(format='%Y-%m-%d',
                attrs={
                    'value': datetime.now().strftime('%Y-%m-%d'),
                }
            ),
            'user_create': TextInput(
                attrs={
                'type': 'hidden',
                'readonly': True,
                }
            ),
            'user_update': TextInput(
                attrs={
                'type': 'hidden',
                'readonly': True,
                }
            ),

        }
        exclude = ['user_create', 'user_update']

    def save(self, commit=True):
        data = {}
        form = super()
        try:
            if form.is_valid():
                instance = form.save()
                data = instance.toJSON()
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
            'user_create': TextInput(
                attrs={
                'type': 'hidden',
                'readonly': True,
                }
            ),
            'user_update': TextInput(
                attrs={
                'type': 'hidden',
                'readonly': True,
                }
            ),


        }
        exclude = ['user_update', 'user_create']

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

class BuyForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['prov'].queryset = Supplier.objects.none()

        for form in self.visible_fields():
            form.field.widget.attrs['class'] = 'form-control'
            form.field.widget.attrs['autocomplete'] = 'off'

            
    methodpay = ModelChoiceField(queryset=MethodPay.objects.all(), widget=Select(attrs={
            'class': 'custom-select select2',
        }))
    typfund = ModelChoiceField(queryset=typeFunds.objects.none(), widget=Select(attrs={
            'class': 'custom-select select2',
        }))
    class Meta:
        model = Buy
        fields = '__all__'
        widgets = {
            'prov': Select(attrs={
                'class': 'custom-select select2',
                # 'style': 'width: 100%'
            }),
            'date_joined': DateInput(
                format='%Y-%m-%d',
                attrs={
                    'value': datetime.now().strftime('%Y-%m-%d'),
                    'autocomplete': 'off',
                    'class': 'form-control datetimepicker-input',
                    'id': 'date_joined',
                    'data-target': '#date_joined',
                    'readonly': True,
                    'data-toggle': 'datetimepicker'
                }
            ),
            'iva': TextInput(attrs={
                'class': 'form-control',
            }),
            'user_create': TextInput(
                attrs={
                'type': 'hidden',
                'readonly': True,
                }
            ),
            'user_update': TextInput(
                attrs={
                'type': 'hidden',
                'readonly': True,
                }
            ),
            'subtotal': TextInput(attrs={
                'readonly': True,
                'class': 'form-control',
            }),
            'total': TextInput(attrs={
                'readonly': True,
                'class': 'form-control',
            })
        }

class ProductionForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['produc'].queryset = Product.objects.none()

        for form in self.visible_fields():
            form.field.widget.attrs['class'] = 'form-control'
            form.field.widget.attrs['autocomplete'] = 'off'

    class Meta:
        model = Production
        fields = '__all__'
        widgets = {
            'produc': Select(attrs={
                'class': 'custom-select select2',
                # 'style': 'width: 100%'
            }),
            'user_create': TextInput(
                attrs={
                'type': 'hidden',
                'readonly': True,
                }
            ),
            'user_update': TextInput(
                attrs={
                'type': 'hidden',
                'readonly': True,
                }
            ),
            'date_joined': DateInput(
                format='%Y-%m-%d',
                attrs={
                    'value': datetime.now().strftime('%Y-%m-%d'),
                    'autocomplete': 'off',
                    'class': 'form-control datetimepicker-input',
                    'id': 'date_joined',
                    'data-target': '#date_joined',
                    'readonly': True,
                    'data-toggle': 'datetimepicker'
                }
            ),
        }

class RecycleForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        

    class Meta:
        model = Recycle
        fields = '__all__'
        widgets = { 
            'type': TextInput(
                attrs={
                'type': 'hidden',
                'readonly': True,
                }
            ),
            'user_create': TextInput(
                attrs={
                'type': 'hidden',
                'readonly': True,
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
    
class RecycleMaterialsForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        

    class Meta:
        model = RecycleMaterials
        fields = '__all__'
        widgets = { 
            'type': TextInput(
                attrs={
                'type': 'hidden',
                'readonly': True,
                }
            ),
            'user_create': TextInput(
                attrs={
                'type': 'hidden',
                'readonly': True,
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

class CierreCajaForm(ModelForm):
    class Meta:
        model = CierreCaja
        fields = '__all__'

        widgets = {
         'aperbank_impor': TextInput(
                attrs={
                'type': 'hidden',
                'readonly': True,
                }
            ),
            'apercaja_impor': TextInput(
                attrs={
                'type': 'hidden',
                'readonly': True,
                }
            ),
            'closebank_impor': TextInput(
                attrs={
                'type': 'hidden',
                'readonly': True,
                }
            ),
            'closecaja_impor': TextInput(
                attrs={
                'type': 'hidden',
                'readonly': True,
                }
            ),
            'estado': TextInput(
                attrs={
                'type': 'hidden',
                'readonly': True,
                }
            ),      
            'user_create': TextInput(
                attrs={
                'type': 'hidden',
                'readonly': True,
                }
            ),
            'user_update': TextInput(
                attrs={
                'type': 'hidden',
                'readonly': True,
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

class WithdrawForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for form in self.visible_fields():
            form.field.widget.attrs['class'] = 'form-control'
            form.field.widget.attrs['autocomplete'] = 'off'
        self.fields['typeF'].widget.attrs['autofocus'] = True

    class Meta:
        model = Withdraw
        fields = '__all__'
        widgets = {
            'date_joined': DateInput(format='%Y-%m-%d',
                attrs={
                    'readonly': True,
                    'value': datetime.now().strftime('%Y-%m-%d'),
                }
            ),
            'user_create': TextInput(
                attrs={
                'type': 'hidden',
                'readonly': True,
                }
            ),
            'user_update': TextInput(
                attrs={
                'type': 'hidden',
                'readonly': True,
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
    
class FundForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        model = Fund
        fields = '__all__'
        widgets = {
            'date_joined': DateInput(format='%Y-%m-%d',
                attrs={
                    'readonly': True,
                    'type': 'hidden',
                    'value': datetime.now().strftime('%Y-%m-%d'),
                }
            ),
            'typeMove': TextInput(
                attrs={
                'type': 'hidden',
                'readonly': True,
                }
            ),   
            'amount': TextInput(
                attrs={
                'type': 'hidden',
                'readonly': True,
                }
            ), 
            'typeF': TextInput(
                attrs={
                'type': 'hidden',
                'readonly': True,
                }
            ), 
            'methodpay': TextInput(
                attrs={
                'type': 'hidden',
                'readonly': True,
                }
            ),
            'sale': TextInput(
                attrs={
                'type': 'hidden',
                'readonly': True,
                }
            ),
            'buy': TextInput(
                attrs={
                'type': 'hidden',
                'readonly': True,
                }
            ), 
            'closing': TextInput(
                attrs={
                'type': 'hidden',
                'readonly': True,
                }
            ),
            'user_create': TextInput(
                attrs={
                'type': 'hidden',
                'readonly': True,
                }
            ),
            'user_update': TextInput(
                attrs={
                'type': 'hidden',
                'readonly': True,
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
    
search = CharField(widget=TextInput(attrs={
    'class': 'form-control',
    'placeholder': 'Ingrese una descripcion'
}))