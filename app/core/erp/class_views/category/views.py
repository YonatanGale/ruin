from unicodedata import category
from urllib import request
from core.erp.forms import CategoryForm
from django.shortcuts import render
from core.erp.models import Category
from core.erp.mixins import IsSuperuserMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.http import JsonResponse


class categoryListView(LoginRequiredMixin, IsSuperuserMixin, ListView):
    model = Category
    template_name = 'template/category/list.html'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *arg, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'searchdata':
                data = []
                for i in Category.objects.all():
                    data.append(i.toJSON())
            else:
                data['error'] = 'Ha ocurrido un error'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Lista de categorias'
        context['create_url'] = reverse_lazy('erp:category_create')
        context['list_url'] = reverse_lazy('erp:category_list')
        context['entity'] = 'Categorias'
        return context

class categoryCreateView(LoginRequiredMixin, CreateView):
    model = Category
    form_class = CategoryForm
    template_name = 'template/category/create.html'
    success_url = reverse_lazy('erp:category_list')

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
        context['title'] = 'Creacion de categorias'
        context['entity'] = 'Categorias'
        context['action'] = 'add'
        context['list_url'] = reverse_lazy('erp:category_list')
        return context

class categoryUpdateView(LoginRequiredMixin,UpdateView):
    model = Category
    form_class = CategoryForm
    template_name = 'template/Category/create.html'
    success_url = reverse_lazy('erp:category_list')


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

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *arg, **kwargs):
        data = {}
        try:
            self.object.delete()
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'eliminacion de categorias'
        context['entity'] = 'Categorias'
        context['list_url'] = reverse_lazy('erp:category_list')
        return context