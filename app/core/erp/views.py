from django.http import HttpResponse, JsonResponse
from django.shortcuts import render


# Create your views here.
def myfirstview(request):
    data = {
            'name': "Yoni"
    } 
    return JsonResponse(data)
