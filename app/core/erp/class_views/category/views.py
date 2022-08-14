from unicodedata import category
from django.shortcuts import render
from core.erp.models import Category
from django.views.generic import ListView


class categoryListView(ListView):
    model = Category
    template_name = 'category/list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Lista de categorias'
        return context
