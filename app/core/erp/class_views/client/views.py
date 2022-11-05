from urllib import request
from core.erp.forms import CategoryForm, clientForm
from django.shortcuts import render
from core.erp.models import Category, Client
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.views.generic import TemplateView

class ClientListView(TemplateView):
    template_name = 'template/client/list.html'

    @method_decorator(csrf_exempt)
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'searchdata':
                data = []
                for i in Client.objects.all():
                    data.append(i.toJSON())
            elif action == 'add':
                cli = Client()
                cli.names = request.POST['names']
                cli.surnames = request.POST['surnames']
                cli.ci = request.POST['ci']
                cli.Birthday = request.POST['Birthday']
                cli.addres = request.POST['addres']
                cli.save()
            else:
                data['error'] = 'Ha ocurrido un error'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de Clientes'
        context['list_url'] = reverse_lazy('erp:client_list')
        context['entity'] = 'Clientes'
        context['action'] = 'add'
        context['form'] = clientForm()
        return context

# class clientCreateView(CreateView):
#     model = Client
#     form_class = clientForm
#     template_name = 'template/client/create.html'
#     success_url = reverse_lazy('erp:client_list')


#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['title'] = 'Creacion de clientes'
#         context['entity'] = 'Clientes'
#         return context

# class clientUpdateView(UpdateView):
#     model = Client
#     form_class = clientForm
#     template_name = 'template/client/create.html'
#     success_url = reverse_lazy('erp:client_list')

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['title'] = 'edicion de clientes'
#         context['entity'] = 'Clientes'
#         return context

# class clientDeleteView(DeleteView):
#     model = Client
#     template_name = 'template/client/delete.html'
#     success_url = reverse_lazy('erp:client_list')

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['title'] = 'eliminacion de clientes'
#         context['entity'] = 'Clientes'
#         context['list_url'] = reverse_lazy('erp:client_list')
#         return context