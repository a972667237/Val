from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.core.paginator import Paginator, EmptyPage, InvalidPage
from .models import *

# Create your views here.
def index(requests):
    slide = Slide.objects.all()
    product = Product.objects.all().order_by('-pk')
    product = product[:6]
    home_gallery = Home_gallery.objects.all()
    return render(requests, 'index.html', locals())

def article(requests):
    pk = requests.GET.get('pk')
    article = get_object_or_404(Article, pk=pk)
    return render(requests, 'article.html', locals())

def news(requests):
    pk = requests.GET.get('pk', 0)
    if pk is 0:
        article = Article.objects.filter(pk__gt=2)
        return render(requests, 'news.html', locals())
    recent_article = Article.objects.filter(pk__gt=2).order_by("-pk")[:5]
    article = get_object_or_404(Article, pk=pk)
    return render(requests, 'each_new.html', locals())

def products(requests):
    pk = requests.GET.get('pk', 0)
    t = Product_type.objects.all()
    if pk is 0:
        s = [Product.objects.filter(kind=i) for i in t if
                Product.objects.filter(kind=i).count() > 0]
        return render(requests, 'products.html', locals())
    nt = get_object_or_404(Product_type, pk=pk)
    s = Product.objects.filter(kind=nt)
    paginator = Paginator(s, 12)
    try:
        page = int(requests.GET.get('page', 1))
        s = paginator.page(page)
    except(EmptyPage, InvalidPage):
        s = paginator.page(1)
        page = 1
    return render(requests, 'products_detail.html', locals())

def product_detail(requests):
    pk = requests.GET.get('pk', 0)
    t = Product_type.objects.all()
    p = get_object_or_404(Product, pk=pk)
    more = Product.objects.filter(kind=p.kind)
    return render(requests, 'each_products.html', locals())

def gallery(requests):
    gal = Gallery.objects.all()
    return render(requests, 'gallery.html', locals())
