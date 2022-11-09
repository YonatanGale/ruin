from core.reports.forms import ReportForm
from django.shortcuts import render
from django.views.generic import TemplateView
from django.urls import reverse_lazy


# Create your views here.
class RepostSaleView(TemplateView):
    template_name = 'core/reports/templates/sale/report.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Reporte de las ventas'
        context['entity'] = 'Reportes'
        context['list_url'] = reverse_lazy('sale_report')
        context['form'] = ReportForm()
        return context
