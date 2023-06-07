from telnetlib import LOGOUT
from core.login.views import *
from django.urls import path, include



urlpatterns = [
    path('', loginformView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout')
]
