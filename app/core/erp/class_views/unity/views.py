from urllib import request
from core.erp.forms import CategoryForm, UnityForm
from django.shortcuts import render
from core.erp.models import Unity
from core.erp.mixins import IsSuperuserMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.http import JsonResponse
from django.views.generic import TemplateView



class unityListView(LoginRequiredMixin, IsSuperuserMixin, TemplateView):
    model = Unity
    template_name = 'template/unity/list.html'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *arg, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'searchdata':
                data = []
                for i in Unity.objects.all():
                    data.append(i.toJSON())
            elif action == 'add':
                cat = Unity()
                cat.name = request.POST['name']
                cat.save()
            elif action == 'edit':
                cat = Unity.objects.get(pk=request.POST['id'])
                cat.name = request.POST['name']
                cat.save()
            elif action == 'delete':
                cat = Unity.objects.get(pk=request.POST['id'])
                cat.delete()
            else:
                data['error'] = 'Ha ocurrido un error'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Lista de Unidades de medida'
        context['create_url'] = reverse_lazy('erp:unity_create')
        context['list_url'] = reverse_lazy('erp:unity_list')
        context['entity'] = 'Unidades'
        context['form'] = UnityForm()
        return context