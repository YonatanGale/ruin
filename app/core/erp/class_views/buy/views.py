from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from core.erp.models import *
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from core.erp.forms import buyForm


class buyListView(ListView):
    model = buy
    template_name = 'template/buy/list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Lista de compras'
        context['create_url'] = reverse_lazy('erp:buy_create')
        context['entity'] = 'Compras'
        return context

class buyListView2(ListView):
    model = buy
    template_name = 'template/buy/list2.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Lista de compras'
        context['create_url'] = reverse_lazy('erp:buy_create')
        context['entity'] = 'Compras'
        return context

class buyCreateView(CreateView):
    model = buy
    form_class = buyForm
    template_name = 'template/buy/create.html'
    success_url = reverse_lazy('erp:buy_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Compras realizadas'
        context['entity'] = 'Compras'
        return context

class buyDeleteView(DeleteView):
    model = buy
    template_name = 'template/buy/delete.html'
    success_url = reverse_lazy('erp:buy_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'eliminacion de compra'
        context['entity'] = 'Compras'
        context['list_url'] = reverse_lazy('erp:buy_list')
        return context