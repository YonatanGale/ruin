import json
from django.db import transaction
from unicodedata import category
from urllib import request
from core.erp.forms import CategoryForm, SaleForm
from django.shortcuts import render
from core.erp.models import  DetSale, Product, Sale
from core.erp.mixins import IsSuperuserMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.http import JsonResponse


class SaleCreateView(LoginRequiredMixin, CreateView):
    model = Sale
    form_class = SaleForm
    template_name = 'template/sale/create.html'
    success_url = reverse_lazy('erp:dashboard')

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'search_products':
                data = []
                prods = Product.objects.filter(name__icontains=request.POST['term'])[0:10]
                for i in prods:
                    item = i.toJSON()
                    item['value'] = i.name
                    data.append(item)
            elif action == 'add':
                vents = json.loads(request.POST['vents'])
                sale = Sale()
                sale.date_joined = vents['date_joined']
                sale.cli_id = vents['cli']
                sale.subtotal = float(vents['subtotal'])
                sale.iva = float(vents['iva'])
                sale.total = float(vents['total'])
                sale.save()

                for i in vents['products']:
                    det = DetSale()
                    det.sale_id = sale.id
                    det.prod_id = i['id']
                    det.cant = int(i['cant'])
                    det.price = float(i['price'])
                    det.subtotal = float(i['subtotal'])
                    det.save()
            else:
                data['error'] = 'No ha ingresado a ninguna opción'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Creacion de una venta'
        context['entity'] = 'Ventas'
        context['action'] = 'add'
        context['list_url'] = reverse_lazy('erp:category_list')
        return context
