from django.forms import *

class ReportForm(Form):

    date_ranger = CharField(widget=TextInput(attrs={
        'class': 'form-control',
        'autocomplete': 'off'
    }))