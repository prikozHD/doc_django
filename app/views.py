# Create your views here.

from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render, render_to_response, RequestContext, get_object_or_404
from models import Products,Category

def render_category(fn):
    def wrapper(request, *args,**kwargs):
        all_category = Category.objects.all()
        return fn(request,all_category)
    return wrapper

@render_category
def products(request, all_category):
    products_list = Products.objects.all()
    return render_to_response('products.html', locals(), context_instance=RequestContext(request))


def get_product(request, slug):
    product = get_object_or_404(Products, slug = slug)
    return render(request, 'product.html', locals())





