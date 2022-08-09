from django.shortcuts import render

def category_list(request):
    data = {
        'title': 'Listado de categorias'
    }
    return render(request, 'category/list.html', data)