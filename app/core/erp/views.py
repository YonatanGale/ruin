from core.erp.models import Category
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render


# Create your views here.
def myfirstview(request):
    data = {
            'name': "Yoni",
            'categories' : Category.objects.all()
    } 
    return render(request, 'index.html', data)
