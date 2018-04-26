from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import *

# Create your views here.
def index(requests):
    slide = Slide.objects.all()
    product = Product.objects.all().order_by('-pk')
    product = product[:6]
    return render(requests, 'index.html', locals())

def article(requests):
    pk = requests.GET.get('pk')
    article = get_object_or_404(Article, pk=pk)
    return render(requests, 'article.html', locals())

def news(requests):
    pk = requests.GET.get('pk', 0)
    if pk is 0:
        return render(requests, 'news.html', locals())

def products(requests):
    pk = requests.GET.get('pk', 0)
    t = Product_type.objects.all()
    if pk is 0:
        s = [Product.objects.filter(kind=i) for i in t if
                Product.objects.filter(kind=i).count() > 0]
        return render(requests, 'products.html', locals())
    nt = get_object_or_404(Product_type, pk=pk)
    s = Product.objects.filter(kind=nt)
    return render(requests, 'products_detail.html', locals())

def product_detail(requests):
    pk = requests.GET.get('pk', 0)
    t = Product_type.objects.all()
    p = get_object_or_404(Product, pk=pk)
    more = Product.objects.filter(kind=p.kind)
    return render(requests, 'each_products.html', locals())
