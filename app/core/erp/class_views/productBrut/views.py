from unicodedata import category
from urllib import request
from core.erp.forms import CategoryForm, ProductForm
from django.shortcuts import render
from core.erp.models import Category, Product, ProductBrut
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView



class productbrutListView(LoginRequiredMixin, TemplateView):
    model = ProductBrut
    template_name = 'template/productBrut/list.html'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'searchdata':
                data = []
                for i in ProductBrut.objects.all():
                    data.append(i.toJSON())
            elif action == 'add':
                cli = ProductBrut()
                cli.name = request.POST['name']
                cli.uni_id = request.POST['uni']
                cli.price = request.POST['price']
                cli.stock = request.POST['stock']
                cli.save()
            elif action == 'edit':
                cli = ProductBrut.objects.get(pk=request.POST['id'])
                cli.name = request.POST['name']
                cli.uni_id = request.POST['uni']
                cli.price = request.POST['price']
                cli.stock = request.POST['stock']
                cli.save()
            elif action == 'delete':
                cli = ProductBrut.objects.get(pk=request.POST['id'])
                cli.delete()
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
        context['form'] = ProductForm()
        return context