import decimal
import json
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db import transaction
from django.db.models import Q
from django.http import JsonResponse, HttpResponseRedirect
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt

from core.erp.forms import BuyForm, ProductForm, ProductionForm, SupplierForm
from django.views.generic import CreateView, ListView, DeleteView, UpdateView

from core.erp.models import Buy, DetProduction, Materials, Product, DetBuy, Production, Supplier

# librerias xhtml2
import os
from django.conf import settings
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.contrib.staticfiles import finders


class ProductionListView(LoginRequiredMixin, ListView):
    model = Buy
    template_name = 'template/production/list.html'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'searchdata':
                data = []
                for i in Production.objects.all():
                    data.append(i.toJSON())
            elif action == 'search_details_prod':
                data = [] 
                for i in DetProduction.objects.filter(crea_id=request.POST['id']):  
                    data.append(i.toJSON())  
            elif action == 'delete':
                if request.user.is_superuser:
                    cli = Production.objects.get(pk=request.POST['id'])
                    cli.user_update = request.user.username
                    pro = Product.objects.get(id = cli.produc_id)
                    pro.stock -= (cli.total)
                    pro.save()
                    cli.save()
                    cli.delete()
                else:
                    data['error'] = 'No tiene permiso para ingresar a este modulo'
            else:
                data['error'] = 'Ha ocurrido un error'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de produccion'
        context['create_url'] = reverse_lazy('erp:production_create')
        context['list_url'] = reverse_lazy('erp:production_list')
        context['entity'] = 'Produccion'
        return context


class ProductionCreateView(LoginRequiredMixin, CreateView):
    model = Production
    form_class = ProductionForm
    template_name = 'template/production/create.html'
    success_url = '' #reverse_lazy('erp:production_list')
    url_redirect = success_url

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'search_products':
                data = []
                ids_exclude = json.loads(request.POST['ids'])
                term = request.POST['term']
                products = Materials.objects.filter(stock__gt=0)
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
                products = Materials.objects.filter(name__icontains=term, stock__gt=0)
                for i in products.exclude(id__in=ids_exclude)[0:10]:
                    item = i.toJSON()
                    item['text'] = i.name
                    data.append(item)
            elif action == 'add':
                with transaction.atomic(): 
                    comp = json.loads(request.POST['comp']) 
                    buy = Production()
                    buy.date_joined = comp['date_joined']
                    buy.produc_id = comp['produc']
                    buy.total = int(comp['total'])
                    buy.user_create = request.user.username
                    buy.save()

                    buy.produc.user_update = request.user.username
                    buy.produc.stock += (buy.total)
                    buy.produc.save()

                    for i in comp['products']:
                        det = DetProduction()
                        det.crea_id = buy.id
                        det.prod_id = i['id'] 
                        det.cant = float(i['cant']) 
                        det.user_create = request.user.username
                        det.save()

                        det.prod.user_update = request.user.username
                        det.prod.stock -= (decimal.Decimal(det.cant))
                        det.prod.save()
                    data = {'id': buy.id}

            elif action == 'search_clients':
                data = []
                term = request.POST['term']
                clients = Product.objects.filter(name__icontains=term)[0:10]
                for i in clients:
                    item = i.toJSON()
                    item['text'] = i.get_full_name()
                    data.append(item)
            elif action == 'create_supplier':
                with transaction.atomic():
                    frmSupplier = ProductForm(request.POST)
                    data = frmSupplier.save()
            else:
                data['error'] = 'No ha ingresado a ninguna opción'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Creación de una produccion'
        context['entity'] = 'Produccion'
        context['list_url'] = self.success_url
        context['action'] = 'add'
        context['det'] = []
        context['frmSupplier'] = ProductForm()
        return context

# class BuyInvoicePdfView(View):

#     def link_callback(self, uri, rel):
#         """
#         Convert HTML URIs to absolute system paths so xhtml2pdf can access those
#         resources
#         """
#         # use short variable names
#         sUrl = settings.STATIC_URL  # Typically /static/
#         sRoot = settings.STATIC_ROOT  # Typically /home/userX/project_static/
#         mUrl = settings.MEDIA_URL  # Typically /static/media/
#         mRoot = settings.MEDIA_ROOT  # Typically /home/userX/project_static/media/

#         # convert URIs to absolute system paths
#         if uri.startswith(mUrl):
#             path = os.path.join(mRoot, uri.replace(mUrl, ""))
#         elif uri.startswith(sUrl):
#             path = os.path.join(sRoot, uri.replace(sUrl, ""))
#         else:
#             return uri  # handle absolute uri (ie: http://some.tld/foo.png)

#         # make sure that file exists
#         if not os.path.isfile(path):
#             raise Exception(
#                 'media URI must start with %s or %s' % (sUrl, mUrl)
#             )
#         return path

#     def get(self, request, *args, **kwargs):
#         try:
#             template = get_template('template/buy/invoice.html')
#             context = {
#                 'buy': Buy.objects.get(pk=self.kwargs['pk']),
#                 'emp': {'name': 'Dulces Mireya', 'ruc': '000000', 'address': 'Ayolas, Misiones'},
#             }
#             html = template.render(context)
#             response = HttpResponse(content_type='application/pdf')
#             # response['Content-Disposition'] = 'attachment; filename="report.pdf"'
#             pisaStatus = pisa.CreatePDF(
#                 html, dest=response,
#                 link_callback=self.link_callback
#             )
#             return response
#         except:
#             pass
#         return HttpResponseRedirect(reverse_lazy('erp:buy_list'))
