from core.erp.models import *
from core.reports.forms import ReportForm
from django.shortcuts import render
from django.views.generic import TemplateView
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.db.models.functions import Coalesce
from django.db.models import Sum, DecimalField 



class RepostSaleView(TemplateView):
    template_name = 'core/reports/templates/sale/report.html'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *arg, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'search_report':
                data = []
                start_date = request.POST.get('start_date', '')
                end_date = request.POST.get('end_date', '')
                search = Sale.objects.all()
                if len(start_date) and len(end_date):
                    search = search.filter(date_joined__range=[start_date, end_date])
                for s in search:
                    data.append([
                        s.id,
                        s.cli.names,
                        s.date_joined.strftime('%Y-%m-%d'),
                        format(s.subtotal, '2f'),
                        format(s.iva, '2f'),
                        format(s.total, '2f'),
                    ])

                subtotal = search.aggregate(r=Coalesce(Sum('subtotal'), 0, output_field=DecimalField())).get('r') 
                iva = search.aggregate(r=Coalesce(Sum('iva'), 0, output_field=DecimalField())).get('r') 
                total = search.aggregate(r=Coalesce(Sum('total'), 0, output_field=DecimalField())).get('r') 

                data.append([
                    '---',
                    '---',
                    '---',
                    format(subtotal, '2f'),
                    format(iva, '2f'),
                    format(total, '2f'),
                ])
            else:
                data['error'] = 'Ha ocurrido un error'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Reporte de las ventas'
        context['entity'] = 'Reportes'
        context['list_url'] = reverse_lazy('sale_report')
        context['form'] = ReportForm()
        return context

class RepostBuyView(TemplateView):
    template_name = 'core/reports/templates/buy/report.html'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *arg, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'search_report':
                data = []
                start_date = request.POST.get('start_date', '')
                end_date = request.POST.get('end_date', '')
                search = Buy.objects.all()
                if len(start_date) and len(end_date):
                    search = search.filter(date_joined__range=[start_date, end_date])
                for s in search:
                    data.append([
                        s.id,
                        s.prov.names,
                        s.date_joined.strftime('%Y-%m-%d'),
                        format(s.subtotal, '2f'),
                        format(s.iva, '2f'),
                        format(s.total, '2f'),
                    ])

                subtotal = search.aggregate(r=Coalesce(Sum('subtotal'), 0, output_field=DecimalField())).get('r') 
                iva = search.aggregate(r=Coalesce(Sum('iva'), 0, output_field=DecimalField())).get('r') 
                total = search.aggregate(r=Coalesce(Sum('total'), 0, output_field=DecimalField())).get('r') 

                data.append([
                    '---',
                    '---',
                    '---',
                    format(subtotal, '2f'),
                    format(iva, '2f'),
                    format(total, '2f'),
                ])
            else:
                data['error'] = 'Ha ocurrido un error'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Reporte de las ventas'
        context['entity'] = 'Reportes'
        context['list_url'] = reverse_lazy('buy_report')
        context['form'] = ReportForm()
        return context
    
class RepostProductionView(TemplateView):
    template_name = 'core/reports/templates/production/report.html'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *arg, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'search_report':
                data = []
                start_date = request.POST.get('start_date', '')
                end_date = request.POST.get('end_date', '')
                search = Production.objects.all()
                if len(start_date) and len(end_date):
                    search = search.filter(date_joined__range=[start_date, end_date])
                for s in search:
                    data.append([
                        s.id,
                        s.produc.name,
                        s.date_joined.strftime('%Y-%m-%d'),
                        format(s.total, '2f'),
                    ])

                total = search.aggregate(r=Coalesce(Sum('total'), 0, output_field=DecimalField())).get('r') 

                data.append([
                    '---',
                    '---',
                    '---',
                    format(total, '2f'),
                ])
            else:
                data['error'] = 'Ha ocurrido un error'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Reporte de produccion'
        context['entity'] = 'Reportes'
        context['list_url'] = reverse_lazy('production_report')
        context['form'] = ReportForm()
        return context
    
class RepostProductView(TemplateView):
    template_name = 'core/reports/templates/product/report.html'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *arg, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'search_report':
                data = []
                start_date = request.POST.get('start_date', '')
                end_date = request.POST.get('end_date', '')
                search = Product.objects.all()
                if len(start_date) and len(end_date):
                    search = search.filter(date_joined__range=[start_date, end_date])
                for s in search:
                    data.append([
                        s.id,
                        s.name,
                        s.cate.name,
                        s.stock,
                        s.price,
                    ])
            else:
                data['error'] = 'Ha ocurrido un error'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Reporte de productos'
        context['entity'] = 'Reportes'
        context['list_url'] = reverse_lazy('product_report')
        context['form'] = ReportForm()
        return context
    
class RepostClientView(TemplateView):
        template_name = 'core/reports/templates/client/report.html'

        @method_decorator(csrf_exempt)
        def dispatch(self, request, *args, **kwargs):
            return super().dispatch(request, *args, **kwargs)

        def post(self, request, *arg, **kwargs):
            data = {}
            try:
                action = request.POST['action']
                if action == 'search_report':
                    data = []
                    start_date = request.POST.get('start_date', '')
                    end_date = request.POST.get('end_date', '')
                    search = Client.objects.all()
                    if len(start_date) and len(end_date):
                        search = search.filter(date_joined__range=[start_date, end_date])
                    for s in search:
                        data.append([
                            s.ci,
                            s.names,
                            s.surnames,
                            s.Birthday,
                            s.addres,
                        ])
                else:
                    data['error'] = 'Ha ocurrido un error'
            except Exception as e:
                data['error'] = str(e)
            return JsonResponse(data, safe=False)    

        def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            context['title'] = 'Reporte de clientes'
            context['entity'] = 'Reportes'
            context['list_url'] = reverse_lazy('client_report')
            context['form'] = ReportForm()
            return context