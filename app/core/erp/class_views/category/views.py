from unicodedata import category
from urllib import request
from core.erp.forms import CategoryForm
from django.shortcuts import render
from core.erp.models import Category
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy


class categoryListView(ListView):
    model = Category
    template_name = 'template/category/list.html'

    @method_decorator(csrf_exempt)
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Lista de categorias'
        context['create_url'] = reverse_lazy('erp:category_create')
        context['entity'] = 'Categorias'
        return context

class categoryCreateView(CreateView):
    model = Category
    form_class = CategoryForm
    template_name = 'template/category/create.html'
    success_url = reverse_lazy('erp:category_list')

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Creacion de categorias'
        context['entity'] = 'Categorias'
        return context

class categoryUpdateView(UpdateView):
    model = Category
    form_class = CategoryForm
    template_name = 'template/Category/create.html'
    success_url = reverse_lazy('erp:category_list')

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'edicion de categorias'
        context['entity'] = 'Categorias'
        return context

class categoryDeleteView(DeleteView):
    model = Category
    template_name = 'template/category/delete.html'
    success_url = reverse_lazy('erp:category_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'eliminacion de categorias'
        context['entity'] = 'Categorias'
        context['list_url'] = reverse_lazy('erp:category_list')
        return context