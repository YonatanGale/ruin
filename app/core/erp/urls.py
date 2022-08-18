from django.urls import path
from core.erp.class_views.category.views import *
from core.erp.class_views.product.views import *

app_name = 'erp'

urlpatterns = [
    path('category/list/', categoryListView.as_view(), name='category_list'),
    path('category/create/', categoryCreateView.as_view(), name='category_create')
]