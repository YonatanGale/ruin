from unicodedata import category
from django.shortcuts import render
from core.erp.models import Category
from django.views.generic import ListView

def category_list(request):
    data = {
        'title': 'Listado de categorias',
        'categories': Category.objects.all()
    }
    return render(request, 'category/list.html', data)

class categoryListView(ListView):
    model = Category
    template_name = 'category/list.html'


