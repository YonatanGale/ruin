from unicodedata import category
from urllib import request
from core.erp.forms import CategoryForm
from django.shortcuts import render
from core.erp.models import Category
from core.erp.mixins import IsSuperuserMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.http import JsonResponse
from django.views.generic import TemplateView



class categoryListView(LoginRequiredMixin, TemplateView):
    model = Category
    template_name = 'template/category/list.html'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *arg, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'searchdata':
                data = []
                for i in Category.objects.all():
                    data.append(i.toJSON())
            elif action == 'add':
                cat = Category()
                cat.name = request.POST['name']
                cat.user_create = request.user.username
                cat.save()
            elif action == 'edit':
                cat = Category.objects.get(pk=request.POST['id'])
                cat.name = request.POST['name']
                cat.user_update = request.user.username
                cat.save()
            elif action == 'delete':
                cat = Category.objects.get(pk=request.POST['id'])
                cat.user_update = request.user.username
                cat.save()
                cat.delete()

            else:
                data['error'] = 'Ha ocurrido un error'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Lista de categorias'
        context['create_url'] = reverse_lazy('erp:category_create')
        context['list_url'] = reverse_lazy('erp:category_list')
        context['entity'] = 'Categorias'
        context['form'] = CategoryForm()
        return context