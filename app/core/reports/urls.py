
from django.urls import path, include
from core.reports.views import *



urlpatterns = [
    #reports
    path('sale/', RepostSaleView.as_view(), name='sale_report'),

]