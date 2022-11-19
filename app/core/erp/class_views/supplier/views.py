from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from core.erp.forms import SupplierForm
from core.erp.models import Supplier


class SupplierListView(LoginRequiredMixin, ListView):
    model = Supplier
    template_name = 'template/supplier/list.html'
    permission_required = 'erp.view_supplier'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'searchdata':
                data = []
                for i in Supplier.objects.all():
                    data.append(i.toJSON())
            elif action == 'add':
                cli = Supplier()
                cli.names = request.POST['names']
                cli.surnames = request.POST['surnames']
                cli.ci = request.POST['ci']
                cli.phone = request.POST['phone']
                cli.address = request.POST['address']
                cli.date_joined = request.POST['date_joined']
                cli.save()
            elif action == 'edit':
                cli = Supplier.objects.get(pk=request.POST['id'])
                cli.names = request.POST['names']
                cli.surnames = request.POST['surnames']
                cli.ci = request.POST['ci']
                cli.phone = request.POST['phone']
                cli.address = request.POST['address']
                cli.date_joined = request.POST['date_joined']
                cli.save()
            elif action == 'delete':
                cli = Supplier.objects.get(pk=request.POST['id'])
                cli.delete()
            else:
                data['error'] = 'Ha ocurrido un error'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de Proveedores'
        context['create_url'] = reverse_lazy('erp:supplier_create')
        context['list_url'] = reverse_lazy('erp:supplier_list')
        context['entity'] = 'Proveedores'
        context['form'] = SupplierForm()
        return context
