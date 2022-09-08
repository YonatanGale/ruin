from core.erp.class_views.dashboard.dashboard import DashboardView
from django.urls import path
from core.erp.class_views.category.views import *
from core.erp.class_views.product.views import *
from core.erp.class_views.buy.views import *

app_name = 'erp'

urlpatterns = [
    #categoria
    path('category/list/', categoryListView.as_view(), name='category_list'),
    path('category/create/', categoryCreateView.as_view(), name='category_create'),
    path('category/edit/<int:pk>/', categoryUpdateView.as_view(), name='category_update'),
    path('category/delete/<int:pk>/', categoryDeleteView.as_view(), name='category_delete'),
    #producto
    path('product/list/', productListView.as_view(), name='product_list'),
    path('product/create/', productCreateView.as_view(), name='product_create'),
    path('product/edit/<int:pk>/', productUpdateView.as_view(), name='product_update'),
    path('product/delete/<int:pk>/', productDeleteView.as_view(), name='product_delete'),
    #dashboard
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
    #buy
    path('buy/list/', buyListView.as_view(), name='buy_list'),
    path('buy/create/', buyCreateView.as_view(), name='buy_create'),
    path('buy/delete/<int:pk>/', buyDeleteView.as_view(), name='buy_delete'),
]