from core.erp.class_views.unity.views import unityListView
from core.erp.class_views.Materials.views import materialsListView
from core.erp.class_views.supplier.views import SupplierListView
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
    #Unidad
    path('unity/list/', unityListView.as_view(), name='unity_list'),
    #producto
    path('product/list/', productListView.as_view(), name='product_list'),
    #materials
    path('materials/list/', materialsListView.as_view(), name='materials_list'),
    #dashboard
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
    #buy
    path('buy/list/', BuyListView.as_view(), name='buy_list'),
    path('buy/add/', BuyCreateView.as_view(), name='buy_create'),
    path('buy/invoice/pdf/<int:pk>/', BuyInvoicePdfView.as_view(), name='buy_invoce'),
    # path('buy/delete/<int:pk>/', buyDeleteView.as_view(), name='buy_delete'),
    #Supplier
    path('Supplier/list/', SupplierListView.as_view(), name='supplier_list'),
    #Client
    path('client/list/', ClientListView.as_view(), name='client_list'),
    #Sale
    path('sale/add/', SaleCreateView.as_view(), name='sale_create'),
    path('sale/list/', SaleListView.as_view(), name='sale_list'),
    path('sale/invoice/pdf/<int:pk>/', SaleInvocePdfView.as_view(), name='sale_invoce'),
]