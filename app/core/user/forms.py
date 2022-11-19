from select import select
from turtle import textinput
from core.user.models import user
from django.forms import *

class UserForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for form in self.visible_fields():
            form.field.widget.attrs['autocomplete'] = 'off'
        self.fields['first_name'].widget.attrs['autofocus'] = True

    class Meta:
        model = user
        fields = 'first_name', 'last_name', 'ci', 'email', 'username', 'password', 'is_superuser'

        widgets = {
            'first_name': TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder' : 'Ingrese sus nombres'
                }
            ),
            'last_name': TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder' : 'Ingrese sus apellidos'
                }
            ),
            'ci': TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder' : 'Ingrese su cedula de identidad'
                }
            ),
            'email': TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder' : 'Ingrese su email'
                }
            ),
            'username': TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder' : 'Ingrese un nombre de usuario'
                }
            ),
            'password': PasswordInput(
                attrs={
                    'class': 'form-control',
                    'placeholder' : 'Ingrese su contraseña'
                }
            ),
            'is_superuser': CheckboxInput(
                attrs={
                    'class': 'form-control',
                }
            ),
        }
        exclude = ['groups', 'user_permissions', 'last_login', 'date_joined', 'is_active', 'is_staff']
    
    def save(self, commit=True):
        data = {}
        form = super()
        try:
            if form.is_valid():
                pwd = self.cleaned_data['password']
                u = form.save(commit=False)
                if u.pk is None:
                    u.set_password(pwd)
                else:
                    User = user.objects.get(pk=u.pk)
                    if user.password != pwd:
                        u.set_password(pwd)
                u.save()
            else:
                data['error'] = form.errors
        except Exception as e:
            data['error'] = str(e)
        return data
