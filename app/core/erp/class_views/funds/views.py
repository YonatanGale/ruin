import json
from django.db import transaction
from unicodedata import category
from urllib import request
from core.erp.forms import CategoryForm, SaleForm, clientForm
from django.shortcuts import render
from core.erp.models import  Client, DetSale, Fund, Product, Sale, typeFunds
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
                for i in Fund.objects.all():
                    data.append(i.toJSON())

            elif action == 'TypeList':
                data = []
                for i in typeFunds.objects.all():
                    data.append(i.toJSON())
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
        context['entity'] = 'Fondos'
        return context
