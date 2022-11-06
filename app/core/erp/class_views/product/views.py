from unicodedata import category
from urllib import request
from core.erp.forms import CategoryForm, ProductForm
from django.shortcuts import render
from core.erp.models import Category, Product
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse


class productListView(ListView):
    model = Product
    template_name = 'template/product/list.html'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'searchdata':
                data = []
                for i in Product.objects.all():
                    data.append(i.toJSON())
            else:
                data['error'] = 'Ha ocurrido un error'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Lista de productos'
        context['create_url'] = reverse_lazy('erp:product_create')
        context['list_url'] = reverse_lazy('erp:product_list')
        context['entity'] = 'Productos'
        return context

class productCreateView(CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'template/product/create.html'
    success_url = reverse_lazy('erp:product_list')

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'add':
                form = self.get_form()
                data = form.save()
            else:
                data['error'] = 'No ha ingresado a ninguna opción'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Creacion de productos'
        context['entity'] = 'Productos'
        context['action'] = 'add'
        context['list_url'] = reverse_lazy('erp:product_list')
        return context

class productUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'template/product/create.html'
    success_url = reverse_lazy('erp:product_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'edicion de productos'
        context['entity'] = 'Productos'
        return context

class productDeleteView(DeleteView):
    model = Product
    template_name = 'template/product/delete.html'
    success_url = reverse_lazy('erp:product_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'eliminacion de productos'
        context['entity'] = 'Productos'
        context['list_url'] = reverse_lazy('erp:product_list')
        return context