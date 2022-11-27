from urllib import request
from core.erp.forms import CategoryForm, clientForm
from django.shortcuts import render
from core.erp.models import Category, Client
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.decorators import method_decorator
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.views.generic import TemplateView

class ClientListView(LoginRequiredMixin, TemplateView):
    template_name = 'template/client/list.html'

    @method_decorator(csrf_exempt)
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
                cli.user_create = request.user.username
                cli.save()
            elif action == 'edit':
                cli = Client.objects.get(pk=request.POST['id'])
                cli.names = request.POST['names']
                cli.surnames = request.POST['surnames']
                cli.ci = request.POST['ci']
                cli.Birthday = request.POST['Birthday']
                cli.addres = request.POST['addres']
                cli.user_update = request.user.username
                cli.save()
            elif action == 'delete':
                if request.user.is_superuser:
                    cli = Client.objects.get(pk=request.POST['id'])
                    cli.user_update = request.user.username
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
        context['title'] = 'Listado de Clientes'
        context['list_url'] = reverse_lazy('erp:client_list')
        context['entity'] = 'Clientes'
        context['form'] = clientForm()
        return context
