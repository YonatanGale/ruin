import datetime
import decimal
import json
from django.db import transaction
from unicodedata import category
from urllib import request
from core.erp.forms import CategoryForm, CierreCajaForm, FundForm, SaleForm, WithdrawForm, clientForm
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
            auxi = CierreCaja.objects.filter(estado='a').exists()
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
            elif action == 'edit':
                cli = Fund.objects.get(pk=request.POST['id'])
                cli.payNro = request.POST['payNro']
                cli.payowner = request.POST['payowner']
                cli.user_update = request.user.username
                cli.save()
            elif action == 'addwithdraw':
                        if auxi:
                            det = Withdraw()
                            det.typeF_id = request.POST['typeF']
                            det.cant = request.POST['cant']
                            det.date_joined = request.POST['date_joined']
                            det.user_create = request.user.username
                            det.save()
                            det.typeF.impo -= (decimal.Decimal(det.cant))
                            det.typeF.save()

                            
                            fun = Fund()
                            fun.typeF_id = det.typeF_id
                            fun.typeMove = 'Retiro de dinero'
                            fun.amount = det.cant
                            fun.payNro = '-------'
                            fun.payowner = '-------'
                            fun.methodpay_id = 4
                            fun.user_create = request.user.username
                            fun.date_joined = det.date_joined
                            fun.save()
                        else:
                            data['error'] = 'La caja esta cerrada'
            elif action == 'addCargar':
                        if auxi:
                            det = Withdraw()
                            det.typeF_id = request.POST['typeF']
                            det.reason = '--------'
                            det.cant = request.POST['cant']
                            det.date_joined = request.POST['date_joined']
                            det.user_create = request.user.username
                            det.save()
                            det.typeF.impo += (decimal.Decimal(det.cant))
                            det.typeF.save()

                            
                            fun = Fund()
                            fun.typeF_id = det.typeF_id
                            fun.typeMove = 'Carga de dinero'
                            fun.amount = det.cant
                            fun.payNro = '-------'
                            fun.payowner = '-------'
                            fun.methodpay_id = 4
                            fun.user_create = request.user.username
                            fun.date_joined = det.date_joined
                            fun.save()
                        else:
                            data['error'] = 'La caja esta cerrada'

            elif action == 'addcierre':
                        if auxi:
                            aux = CierreCaja.objects.raw('select * from erp_cierrecaja where id = (select max(id) from erp_cierrecaja where estado = \'a\')')
                            for i in aux:
                                det = CierreCaja.objects.get(id = i.id)
                            if det.user_create == request.user.username:
                                tyb = typeFunds.objects.get(pk=1)
                                tyc = typeFunds.objects.get(pk=2)
                                det.closebank_impor = tyb.impo
                                det.closecaja_impor = tyc.impo
                                det.estado = 'c'
                                det.user_update = request.user.username
                                det.save()
                            else:
                                data['error'] = 'La caja no pertenece al usuario'
                        else:
                            data['error'] = 'La caja esta cerrada'

            elif action == 'addapertura':
                    if auxi:
                        data['error'] = 'La caja esta abierta'
                    else:
                        det = CierreCaja()
                        tyb = typeFunds.objects.get(pk=1)
                        tyc = typeFunds.objects.get(pk=2)
                        det.aperbank_impor = tyc.impo
                        det.apercaja_impor = tyb.impo
                        det.estado = 'a'
                        det.user_create = request.user.username
                        det.save()
            else:
                data['error'] = 'Ha ocurrido un error'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

    # def ObtenerEstado (request):
    #     est = CierreCaja.objects.filter(estado='a').exists()
    #     if est:
    #         return JsonResponse({'estado':'abierto'})
    #     return JsonResponse({'estado':'cerrado'})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Movimientos de Fondos'
        context['create_url'] ='' #reverse_lazy('erp:sale_create')
        context['list_url'] =  reverse_lazy('erp:fund_list')
        context['frmCaja'] =  CierreCajaForm()
        context['formwithdraw'] =  WithdrawForm()
        context['formfund'] =  FundForm()
        context['estado'] =  CierreCaja.objects.filter(estado='a').exists()
        context['entity'] = 'Fondos'
        return context

    