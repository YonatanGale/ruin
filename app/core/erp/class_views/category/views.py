from unicodedata import category
from urllib import request
from core.erp.forms import CategoryForm
from django.shortcuts import render
from core.erp.models import Category
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy


class categoryListView(ListView):
    model = Category
    template_name = 'category/list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Lista de categorias'
        context['create_url'] = reverse_lazy('erp:category_create')
        context['entity'] = 'Categorias'
        return context

class categoryCreateView(CreateView):
    model = Category
    form_class = CategoryForm
    template_name = 'category/create.html'
    success_url = reverse_lazy('erp:category_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Creacion de categorias'
        return context