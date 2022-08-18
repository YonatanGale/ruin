from core.erp.models import Product
from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy

class ProductListView(ListView):
    model = Product
    template_name = 'Product/list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Lista de Productos'
        return context

# class ProductCreateView(CreateView):
#     model = Product
#     form_class = ProductForm
#     template_name = 'Product/create.html'
#     success_url = reverse_lazy('erp:Product_list')

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['title'] = 'Registro de Productos'
#         return context