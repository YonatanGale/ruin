
from django.urls import path, include
from core.reports.views import *



urlpatterns = [
    #reports
    path('sale/', RepostSaleView.as_view(), name='sale_report'),
    path('buy/', RepostBuyView.as_view(), name='buy_report'),
    path('production/', RepostProductionView.as_view(), name='production_report'),
    path('product/', RepostProductView.as_view(), name='product_report'),
    path('client/', RepostClientView.as_view(), name='client_report'),
    path('fund/', RepostFundView.as_view(), name='fund_report'),

]