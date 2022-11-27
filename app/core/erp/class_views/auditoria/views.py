import datetime
import decimal
import json
from django.db import transaction
from unicodedata import category
from urllib import request
from core.erp.forms import CategoryForm, CierreCajaForm, FundForm, SaleForm, WithdrawForm, clientForm
from django.shortcuts import render
from core.erp.models import  Auditoria, CierreCaja, Client, DetSale, Fund, Product, Sale, Withdraw, typeFunds
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



class AuditoriaListView(LoginRequiredMixin, IsSuperuserMixin, ListView):
    model = Auditoria
    template_name = 'template/audi/list.html'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'searchdata':
                data = []
                fondos = Auditoria.objects.all()
                for i in fondos:
                    data.append(i.toJSON())
            else:
                data['error'] = 'Ha ocurrido un error'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Auditoria'
        context['create_url'] ='' #reverse_lazy('erp:sale_create')
        context['list_url'] =  reverse_lazy('erp:auditoria_list')
        context['entity'] = 'Auditoria'
        return context