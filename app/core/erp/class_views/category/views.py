from unicodedata import category
from urllib import request
from django.shortcuts import render
from core.erp.models import Category
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import ListView


class categoryListView(ListView):
    model = Category
    template_name = 'category/list.html'

    # @method_decorator(login_required)
    # def dispatch(self, request, *args, **kwargs):
    #     return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Lista de categorias'
        return context
