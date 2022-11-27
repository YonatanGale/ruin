from unicodedata import category
from urllib import request
from core.erp.forms import CategoryForm, MaterialsForm, ProductForm, RecycleMaterialsForm
from django.shortcuts import render
from core.erp.models import Category, Product, Materials, RecycleMaterials
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView



class materialsListView(LoginRequiredMixin, TemplateView):
    model = Materials
    template_name = 'template/materials/list.html'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'searchdata':
                data = []
                for i in Materials.objects.all():
                    data.append(i.toJSON())
            elif action == 'add':
                cli = Materials()
                cli.name = request.POST['name']
                cli.cate_id = request.POST['cate']
                cli.price = request.POST['price']
                cli.stock = request.POST['stock']
                cli.user_create = request.user.username
                cli.save()
            elif action == 'recycle':
                    det = RecycleMaterials()
                    det.prod_id = request.POST['prod']
                    det.cant = request.POST['cant']
                    det.type = 'Retiro de stock'
                    det.user_create = request.user.username
                    det.save()
                    det.prod.user_update = request.user.username
                    det.prod.stock -= int(det.cant)
                    det.prod.save()
            elif action == 'edit':
                cli = Materials.objects.get(pk=request.POST['id'])
                cli.name = request.POST['name']
                cli.cate_id = request.POST['cate']
                cli.price = request.POST['price']
                cli.stock = request.POST['stock']
                cli.user_update = request.user.username
                cli.save()
            elif action == 'delete':
                if request.user.is_superuser:
                    cli = Materials.objects.get(pk=request.POST['id'])
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
        context['title'] = 'Lista de materiales'
        context['list_url'] = reverse_lazy('erp:materials_list')
        context['entity'] = 'Materiales'
        context['form'] = MaterialsForm()
        context['form_re'] = RecycleMaterialsForm()
        return context