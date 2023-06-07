from django.shortcuts import redirect
from django.contrib import messages
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from crum import get_current_request



class IsSuperuserMixin(object):
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_superuser:
            return super().dispatch(request, *args, **kwargs)
        messages.error(request, 'No tiene permiso para ingresar a este modulo')
        return redirect('/erp/dashboard/')

class ValidatePermissionRequiredMixin(object):
    permission_required = ''
    url_redirect = None

    # def get_perms(self):
    #     if isinstance(self.permission_required, str):
    #         perms = (self.permission_required,)
    #     else:
    #         perms = self.permission_required
    #     return perms

    def get_url_redirect(self):
        if self.url_redirect is None:
            return reverse_lazy('erp:dashboard')
        return self.url_redirect

    def dispatch(self, request, *args, **kwargs):
        request = get_current_request()
        if 'group' in request.session:
            group = request.session['group']
            if group.permissions.filter(codename=self.permission_required):
                return super().dispatch(request, *args, **kwargs)
        messages.error(request, 'No tiene permiso para ingresar a este módulo')
        return HttpResponseRedirect(self.get_url_redirect())