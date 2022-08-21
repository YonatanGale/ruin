from multiprocessing import context
from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView

# Create your views here.
class loginformView(LoginView):
    template_name = 'core/login/template/login.html'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('erp:category_list')
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Iniciar sesion'
        return context