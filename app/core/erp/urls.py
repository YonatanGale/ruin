from core.erp.class_views.funds.views import FundListView, FundUpdateView
from core.erp.class_views.production.views import ProductionCreateView, ProductionListView
from core.erp.class_views.categoryMaterials.views import categoryMaterialsListView
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
    #categoria Materiales
    path('category/materials/list/', categoryMaterialsListView.as_view(), name='categorymaterials_list'),
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
    #production
    path('production/add/', ProductionCreateView.as_view(), name='production_create'),
    path('production/list/', ProductionListView.as_view(), name='production_list'),
    #Funds
    path('funds/update/<int:pk>/', FundUpdateView.as_view(), name='fund_update'),
    path('funds/list/', FundListView.as_view(), name='fund_list'),
]