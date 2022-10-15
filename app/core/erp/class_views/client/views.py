from urllib import request
from core.erp.forms import CategoryForm, clientForm
from django.shortcuts import render
from core.erp.models import Category, Client
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

class clientListView(ListView):
    model = Client
    template_name = 'template/client/list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Lista de clientes'
        context['create_url'] = reverse_lazy('erp:client_create')
        context['entity'] = 'Clientes'
        return context

class clientCreateView(CreateView):
    model = Client
    form_class = clientForm
    template_name = 'template/client/create.html'
    success_url = reverse_lazy('erp:client_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Creacion de clientes'
        context['entity'] = 'Clientes'
        return context

class clientUpdateView(UpdateView):
    model = Client
    form_class = clientForm
    template_name = 'template/client/create.html'
    success_url = reverse_lazy('erp:client_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'edicion de clientes'
        context['entity'] = 'Clientes'
        return context

class clientDeleteView(DeleteView):
    model = Client
    template_name = 'template/client/delete.html'
    success_url = reverse_lazy('erp:client_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'eliminacion de clientes'
        context['entity'] = 'Clientes'
        context['list_url'] = reverse_lazy('erp:client_list')
        return context