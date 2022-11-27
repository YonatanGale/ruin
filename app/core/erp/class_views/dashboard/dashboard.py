from core.erp.models import DetSale, Product, Sale
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse

from django.contrib.auth.mixins import LoginRequiredMixin
from datetime import datetime

from django.db.models.functions import Coalesce
from django.db.models import Sum, DecimalField 




class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'template/dashboard.html'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    def post(self, request, *arg, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'get_graph_sales_month':
                data = {
                    'name': 'Porcentaje de venta',
                    'showInLegend': False,
                    'colorByPoint': True,
                    'data': self.get_graph_sales_month()
                }
            elif action == 'get_graph_sales_product_year':
                data = {
                    'name': 'Porcentaje',
                    'colorByPoint': True,
                    'data': self.get_graph_sales_product_year(),
                }
            else:
                data['error'] = 'Ha ocurrido un error'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False) 

    def get_graph_sales_month(self):
        data = []
        try:
            year = datetime.now().year
            for m in range(1, 12):
                total = Sale.objects.filter(date_joined__year=year, date_joined__month=m).aggregate(r=Coalesce(Sum('total'), 0, output_field=DecimalField())).get('r') 
                data.append(float(total))
        except:
            pass
        return data
    
    def get_graph_sales_product_year(self):
        data = []
        year = datetime.now().year
        month = datetime.now().month
        try:
            for p in Product.objects.all():
                total = DetSale.objects.filter(sale__date_joined__year=year, sale__date_joined__month=month, prod_id=p.id).aggregate(
                        r=Coalesce(Sum('subtotal'), 0, output_field=DecimalField())).get('r') 
                if total > 0:
                    data.append({
                        'name': p.name,
                        'y': float(total)
                    })
        except:
            pass
        return data

    def get_context_data(self, **kwargs):
        contex = super().get_context_data(**kwargs)
        contex['title'] = 'Home'
        contex['graph_sales_month'] = self.get_graph_sales_month()
        return contex