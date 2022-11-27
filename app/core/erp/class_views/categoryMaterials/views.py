from unicodedata import category
from urllib import request
from core.erp.forms import CategoryForm, CategoryMaterialsForm
from django.shortcuts import render
from core.erp.models import Category, CategoryMaterials
from core.erp.mixins import IsSuperuserMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.http import JsonResponse
from django.views.generic import TemplateView



class categoryMaterialsListView(LoginRequiredMixin, TemplateView):
    model = CategoryMaterials
    template_name = 'template/categoryMaterials/list.html'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *arg, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'searchdata':
                data = []
                for i in CategoryMaterials.objects.all():
                    data.append(i.toJSON())
            elif action == 'add':
                cat = CategoryMaterials()
                cat.name = request.POST['name']
                cat.unity = request.POST['unity']
                cat.user_create = request.user.username
                cat.save()
            elif action == 'edit':
                cat = CategoryMaterials.objects.get(pk=request.POST['id'])
                cat.name = request.POST['name']
                cat.unity = request.POST['unity']
                cat.user_update = request.user.username
                cat.save()
            elif action == 'delete':
                if request.user.is_superuser:
                    cat = CategoryMaterials.objects.get(pk=request.POST['id'])
                    cat.user_update = request.user.username
                    cat.save()
                    cat.delete()
                else:
                    data['error'] = 'No tiene permiso para ingresar a este modulo'
            else:
                data['error'] = 'Ha ocurrido un error'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Lista de categorias'
        context['create_url'] = reverse_lazy('erp:categorymaterials_create')
        context['list_url'] = reverse_lazy('erp:categorymaterials_list')
        context['entity'] = 'Categorias'
        context['form'] = CategoryMaterialsForm()
        return context