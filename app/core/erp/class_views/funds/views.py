import datetime
import decimal
import json
from django.db import transaction
from unicodedata import category
from urllib import request
from core.erp.forms import CategoryForm, CierreCajaForm, SaleForm, WithdrawForm, clientForm
from django.shortcuts import render
from core.erp.models import  CierreCaja, Client, DetSale, Fund, Product, Sale, Withdraw, typeFunds
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



class FundListView(LoginRequiredMixin, ListView):
    model = Fund
    template_name = 'template/funds/list.html'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'searchdata':
                data = []
                fondos = Fund.objects.all()
                for i in fondos:
                    data.append(i.toJSON())
            elif action == 'TypeList':
                data = []
                for i in typeFunds.objects.all():
                    data.append(i.toJSON())
            elif action == 'addwithdraw':
                    det = Withdraw()
                    det.typeF_id = request.POST['typeF']
                    det.reason = request.POST['reason']
                    det.cant = request.POST['cant']
                    det.date_joined = request.POST['date_joined']
                    det.save()
                    det.typeF.impo -= (decimal.Decimal(det.cant))
                    det.typeF.save()

                    
                    fun = Fund()
                    fun.typeF_id = det.typeF_id
                    fun.typeMove = 'Retiro de dinero'
                    fun.amount = det.cant
                    fun.payNro = '-------'
                    fun.payowner = '-------'
                    fun.methodpay_id = 3
                    fun.date_joined = det.date_joined
                    fun.save()

            elif action == 'addCargar':
                    det = Withdraw()
                    det.typeF_id = request.POST['typeF']
                    det.reason = '--------'
                    det.cant = request.POST['cant']
                    det.date_joined = request.POST['date_joined']
                    det.save()
                    det.typeF.impo += (decimal.Decimal(det.cant))
                    det.typeF.save()

                    
                    fun = Fund()
                    fun.typeF_id = det.typeF_id
                    fun.typeMove = 'Carga de dinero'
                    fun.amount = det.cant
                    fun.payNro = '-------'
                    fun.payowner = '-------'
                    fun.methodpay_id = 3
                    fun.date_joined = det.date_joined
                    fun.save()


            elif action == 'addcierre':
                    det = CierreCaja()
                    tf = typeFunds()
                    det.caja = tf.impo[1]
                    det.banco = tf.impo[2]
                    det.impor = (decimal.Decimal(det.caja)) + (decimal.Decimal(det.banco))
                    det.date_joined = request.POST['date_joined']
                    det.save()
                    
                    fun = Fund()
                    fun.typeF_id = 1
                    fun.typeMove = 'Cierre caja'
                    fun.amount = 000
                    fun.payNro = '-------'
                    fun.payowner = '-------'
                    fun.methodpay_id = 3
                    fun.date_joined = det.date_joined
                    fun.save()
            else:
                data['error'] = 'Ha ocurrido un error'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de Fondos'
        context['create_url'] ='' #reverse_lazy('erp:sale_create')
        context['list_url'] =  reverse_lazy('erp:fund_list')
        context['frmCaja'] =  CierreCajaForm()
        context['formwithdraw'] =  WithdrawForm()
        context['entity'] = 'Fondos'
        return context
