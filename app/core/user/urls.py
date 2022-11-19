from core.user.views import *
from django.urls import path

app_name = 'user'

urlpatterns = [
    #user
    path('list/', UserListView.as_view(), name='user_list'),
    path('add/', UserCreateView.as_view(), name='user_create'),
    #path('category/edit/<int:pk>/', categoryUpdateView.as_view(), name='category_update'),
    #path('category/delete/<int:pk>/', categoryDeleteView.as_view(), name='category_delete'),
]