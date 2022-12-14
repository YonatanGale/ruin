from unicodedata import category
from django.db import transaction

from urllib import request
from core.erp.forms import CategoryForm, ProductForm, RecycleForm
from django.shortcuts import render
from core.erp.models import Category, Product, Recycle
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView



class productListView(LoginRequiredMixin, TemplateView):
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
            elif action == 'add':
                cli = Product()
                cli.name = request.POST['name']
                cli.cate_id = request.POST['cate']
                cli.price = request.POST['price']
                cli.stock = request.POST['stock']
                cli.save()
            elif action == 'recycle':
                    det = Recycle()
                    det.prod_id = request.POST['prod']
                    det.recy = request.POST['recy']
                    det.cant = request.POST['cant']
                    det.save()
                    det.prod.stock -= int(det.cant)
                    det.prod.save()
            elif action == 'edit':
                cli = Product.objects.get(pk=request.POST['id'])
                cli.name = request.POST['name']
                cli.cate_id = request.POST['cate']
                cli.price = request.POST['price']
                cli.stock = request.POST['stock']
                cli.save()
            elif action == 'delete':
                cli = Product.objects.get(pk=request.POST['id'])
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
        context['det'] = []
        context['form_re'] = RecycleForm()
        return context

