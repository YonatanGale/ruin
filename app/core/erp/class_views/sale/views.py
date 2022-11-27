import decimal
import json
from django.db import transaction
from unicodedata import category
from urllib import request
from core.erp.forms import CategoryForm, SaleForm, clientForm
from django.shortcuts import render
from core.erp.models import  CierreCaja, Client, DetSale, Fund, MethodPay, Product, Sale, typeFunds
from core.erp.mixins import IsSuperuserMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import CreateView, ListView, UpdateView, View
from django.urls import reverse_lazy
from django.http import JsonResponse, HttpResponse, HttpResponseRedirect
from django.views.generic import TemplateView
from django.core.serializers.json import DjangoJSONEncoder
from django.db.models import Q


import os
from django.conf import settings
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.contrib.staticfiles import finders


class SaleListView(LoginRequiredMixin, ListView):
    model = Sale
    template_name = 'template/sale/list.html'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'searchdata':
                data = []
                for i in Sale.objects.all():
                    data.append(i.toJSON())
            elif action == 'search_details_prod':
                data = []
                for i in DetSale.objects.filter(sale_id=request.POST['id']):
                    data.append(i.toJSON())
            elif action == 'delete':
                cli = Sale.objects.get(pk=request.POST['id'])
                cli.delete()
            else:
                data['error'] = 'Ha ocurrido un error'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de Ventas'
        context['create_url'] = reverse_lazy('erp:sale_create')
        context['list_url'] = reverse_lazy('erp:sale_list')
        context['entity'] = 'Ventas'
        return context


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
            auxi = CierreCaja.objects.filter(estado='a').exists()
            action = request.POST['action']
            if action == 'search_products':
                data = []
                ids_exclude = json.loads(request.POST['ids'])
                term = request.POST['term']
                products = Product.objects.filter(stock__gt=0)
                if len(term):
                    products = products.filter(name__icontains=term)
                for i in products.exclude(id__in=ids_exclude)[0:10]:
                    item = i.toJSON()
                    item['value'] = i.name
                    #item['text'] = i.name
                    data.append(item)
            elif action == 'search_autocomplete':
                data = []
                ids_exclude = json.loads(request.POST['ids'])
                term = request.POST['term'].strip()
                data.append({'id': term, 'text':term})
                products = Product.objects.filter(name__icontains=term, stock__gt=0)
                for i in products.exclude(id__in=ids_exclude)[0:10]:
                    item = i.toJSON()
                    item['text'] = i.name
                    data.append(item)
            elif action == 'add':
                if auxi:
                    with transaction.atomic():
                        vents = json.loads(request.POST['vents'])
                        sale = Sale()
                        sale.date_joined = vents['date_joined']
                        sale.cli_id = vents['cli']
                        sale.methodpay_id = vents['methodpay']
                        sale.typfund_id = vents['typfund']
                        sale.subtotal = float(vents['subtotal'])
                        sale.iva = float(vents['iva'])
                        sale.total = float(vents['total'])
                        sale.save()

                        sale.typfund.impo += (decimal.Decimal(sale.total))
                        sale.typfund.save()
                        

                        for i in vents['products']:
                            det = DetSale()
                            det.sale_id = sale.id
                            det.prod_id = i['id']
                            det.cant = int(i['cant'])
                            det.price = float(i['price'])
                            det.subtotal = float(i['subtotal'])
                            det.save()
                            det.prod.stock -= (det.cant)
                            det.prod.save()
                        data = {'id': sale.id}

                        fun = Fund()
                        fun.typeF_id = vents['typfund']
                        fun.sale_id = sale.id
                        fun.methodpay_id = vents['methodpay']
                        fun.typeMove = 'Venta'
                        fun.amount = float(vents['total'])
                        fun.date_joined = vents['date_joined']
                        fun.save()
                else:
                        data['error'] = 'La caja esta cerrada'
            
            elif action == 'search_methodpay':
                data = [{ 'id': '', 'text': '--------'}]
                for i in typeFunds.objects.filter(methodpay_id=request.POST['id']):
                    data.append({'id': i.id, 'text': i.name})
            elif action == 'search_clients':
                data = []
                term = request.POST['term']
                clients = Client.objects.filter(Q(names__icontains=term) | Q(surnames__icontains=term) | Q(ci__icontains=term))[0:10]
                for i in clients:
                    item = i.toJSON()
                    item['text'] = i.get_full_name()
                    data.append(item)
            elif action == 'create_client':
                formClient = clientForm(request.POST)
                data = formClient.save()
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
        context['det'] = []
        context['formClient'] = clientForm()
        context['estado'] =  CierreCaja.objects.filter(estado='a').exists()
        return context


class SaleInvocePdfView(View):
    def get(self, request, *args, **kwargs):
        try:
            template = get_template('template/sale/invoice.html')
            context = {
                'sale': Sale.objects.get(pk=self.kwargs['pk']),
                'comp': {'name': 'Dulces Mireya', 'ruc': '000000000', 'address': 'Ayolas, Misiones'}
            }
            html = template.render(context)
            response = HttpResponse(content_type='application/pdf')
            #response['Content-Disposition'] = 'attachment; filename="report.pdf"'
            pisa_status = pisa.CreatePDF(
                html, dest=response)
            return response
        except:
            pass
        return HttpResponseRedirect(reverse_lazy('erp:sale_list'))