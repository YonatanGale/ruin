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

from core.erp.forms import BuyForm, SupplierForm
from django.views.generic import CreateView, ListView, DeleteView, UpdateView

from core.erp.models import Buy, Materials, Product, DetBuy, Supplier

# librerias xhtml2
import os
from django.conf import settings
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.contrib.staticfiles import finders


class BuyListView(LoginRequiredMixin, ListView):
    model = Buy
    template_name = 'template/buy/list.html'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'searchdata':
                data = []
                for i in Buy.objects.all():
                    data.append(i.toJSON())
            elif action == 'search_details_prod':
                data = [] 
                for i in DetBuy.objects.filter(buy_id=request.POST['id']):  
                    data.append(i.toJSON())  
            elif action == 'search_details_prov':
                data = []  
                for i in DetBuy.objects.filter(buy_id=request.POST['id']): 
                    data.append(i.toJSON())  
            elif action == 'delete':
                cli = Buy.objects.get(pk=request.POST['id'])
                cli.delete()
            else:
                data['error'] = 'Ha ocurrido un error'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de Compras'
        context['create_url'] = reverse_lazy('erp:buy_create')
        context['list_url'] = reverse_lazy('erp:buy_list')
        context['entity'] = 'Compras'
        return context


class BuyCreateView(LoginRequiredMixin, CreateView):
    model = Buy
    form_class = BuyForm
    template_name = 'template/buy/create.html'
    success_url = reverse_lazy('erp:buy_list')
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
                    buy = Buy()
                    buy.date_joined = comp['date_joined']
                    buy.prov_id = comp['prov']
                    buy.subtotal = float(comp['subtotal'])
                    buy.iva = float(comp['iva'])
                    buy.total = float(comp['total'])
                    buy.save()
                    for i in comp['products']:
                        det = DetBuy()
                        det.buy_id = buy.id 
                        det.prod_id = i['id'] 
                        det.cant = float(i['cant']) 
                        det.price = float(i['price'])
                        det.subtotal = float(i['subtotal'])
                        det.save()

                        det.prod.stock += (decimal.Decimal(det.cant))
                        det.prod.save()
                    data = {'id': buy.id}

            elif action == 'search_supplier':
                data = []
                term = request.POST['term']
                supplier = Supplier.objects.filter(
                    Q(names__icontains=term) | Q(surnames__icontains=term) | Q(ci__icontains=term))[0:10]
                for i in supplier:
                    item = i.toJSON()
                    item['text'] = i.get_full_name()
                    data.append(item)
            elif action == 'create_supplier':
                with transaction.atomic():
                    frmSupplier = SupplierForm(request.POST)
                    data = frmSupplier.save()
            else:
                data['error'] = 'No ha ingresado a ninguna opción'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Creación de una Compra'
        context['entity'] = 'Compras'
        context['list_url'] = self.success_url
        context['action'] = 'add'
        context['det'] = []
        context['frmSupplier'] = SupplierForm()
        return context

class BuyInvoicePdfView(View):

    def link_callback(self, uri, rel):
        """
        Convert HTML URIs to absolute system paths so xhtml2pdf can access those
        resources
        """
        # use short variable names
        sUrl = settings.STATIC_URL  # Typically /static/
        sRoot = settings.STATIC_ROOT  # Typically /home/userX/project_static/
        mUrl = settings.MEDIA_URL  # Typically /static/media/
        mRoot = settings.MEDIA_ROOT  # Typically /home/userX/project_static/media/

        # convert URIs to absolute system paths
        if uri.startswith(mUrl):
            path = os.path.join(mRoot, uri.replace(mUrl, ""))
        elif uri.startswith(sUrl):
            path = os.path.join(sRoot, uri.replace(sUrl, ""))
        else:
            return uri  # handle absolute uri (ie: http://some.tld/foo.png)

        # make sure that file exists
        if not os.path.isfile(path):
            raise Exception(
                'media URI must start with %s or %s' % (sUrl, mUrl)
            )
        return path

    def get(self, request, *args, **kwargs):
        try:
            template = get_template('template/buy/invoice.html')
            context = {
                'buy': Buy.objects.get(pk=self.kwargs['pk']),
                'emp': {'name': 'Dulces Mireya', 'ruc': '000000', 'address': 'Ayolas, Misiones'},
            }
            html = template.render(context)
            response = HttpResponse(content_type='application/pdf')
            # response['Content-Disposition'] = 'attachment; filename="report.pdf"'
            pisaStatus = pisa.CreatePDF(
                html, dest=response,
                link_callback=self.link_callback
            )
            return response
        except:
            pass
        return HttpResponseRedirect(reverse_lazy('erp:buy_list'))
