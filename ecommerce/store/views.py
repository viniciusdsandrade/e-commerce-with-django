from lib2to3.fixes.fix_input import context

from django.shortcuts import render

from .models import Produto, Categoria


def store(request):
    all_products = Produto.objects.all()
    context = {'my_products': all_products}
    return render(request, 'store/store.html', context)


def categories(request):
    all_categories = Categoria.objects.all()
    return {'all_categories': all_categories}
