# coding: utf-8
from django.conf.urls import url
from django.contrib import admin
from django.http import HttpResponseRedirect
from .views import *


urlpatterns = [
    url(r'^$', index),
    url(r'^article', article),
    url(r'^news', news),
    url(r'^products', products),
    url(r'^product_detail', product_detail),
    url(r'^about', lambda x: HttpResponseRedirect('/article?pk=1')),
]
