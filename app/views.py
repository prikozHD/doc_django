# Create your views here.

from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render, render_to_response, RequestContext, get_object_or_404
from models import *

def render_category(fn):
    def wrapper(request, *args,**kwargs):
        main_category = MainCategory.objects.all()
        return fn(request,main_category)
    return wrapper

@render_category
def products(request, main_category):
    products_list = Products.objects.all()
    return render_to_response('products.html', locals(), context_instance=RequestContext(request))


def get_product(request, slug):
    product = get_object_or_404(Products, slug = slug)
    return render(request, 'product.html', locals())


def search(request):
    return HttpResponse(request.META['QUERY_STRING'])

def main_category(request, main_category_name):
    pass






