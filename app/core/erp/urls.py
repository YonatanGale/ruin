from django.urls import path
from core.erp.class_views.category.views import *

app_name = 'erp'

urlpatterns = [
    path('category/list/', categoryListView.as_view(), name='category_list'),
    path('category/create/', categoryCreateView.as_view(), name='category_create')
]