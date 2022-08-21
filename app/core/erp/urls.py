from django.urls import path
from core.erp.class_views.category.views import *
from core.erp.class_views.product.views import *

app_name = 'erp'

urlpatterns = [
    path('category/list/', categoryListView.as_view(), name='category_list'),
    path('category/create/', categoryCreateView.as_view(), name='category_create'),
    path('category/edit/<int:pk>/', categoryUpdateView.as_view(), name='category_update'),
    path('category/delete/<int:pk>/', categoryDeleteView.as_view(), name='category_delete'),
    path('product/list/', productListView.as_view(), name='product_list'),
    path('product/create/', productCreateView.as_view(), name='product_create'),
    path('product/edit/<int:pk>/', productUpdateView.as_view(), name='product_update'),
    path('product/delete/<int:pk>/', productDeleteView.as_view(), name='product_delete'),
]