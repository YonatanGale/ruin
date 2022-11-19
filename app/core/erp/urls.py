from core.erp.class_views.sale.views import *
from core.erp.class_views.dashboard.dashboard import DashboardView
from django.urls import path
from core.erp.class_views.category.views import *
from core.erp.class_views.product.views import *
from core.erp.class_views.buy.views import *
from core.erp.class_views.client.views import *

app_name = 'erp'

urlpatterns = [
    #categoria
    path('category/list/', categoryListView.as_view(), name='category_list'),
    #producto
    path('product/list/', productListView.as_view(), name='product_list'),
    #dashboard
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
    #buy
    # path('buy/list/', buyListView.as_view(), name='buy_list'),
    # path('buy/add/', buyCreateView.as_view(), name='buy_create'),
    # path('buy/delete/<int:pk>/', buyDeleteView.as_view(), name='buy_delete'),
    #Client
    path('client/list/', ClientListView.as_view(), name='client_list'),
    #Sale
    path('sale/add/', SaleCreateView.as_view(), name='sale_create'),
    path('sale/list/', SaleListView.as_view(), name='sale_list'),
    path('sale/invoice/pdf/<int:pk>/', SaleInvocePdfView.as_view(), name='sale_invoce'),
]