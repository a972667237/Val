from __future__ import unicode_literals

from django.db import models
from DjangoUeditor.models import UEditorField

# Create your models here.
class Article(models.Model):
    title = models.CharField(u'title', max_length=100)
    content = UEditorField(u'content', max_length=200000)
    date = models.DateField(u'create_date', auto_now_add=True, editable=True)
    cover = models.ImageField(u'cover_image', default="/static/img/005.jpg")
    isShow = models.BooleanField(u'show_cover', default=False)
    class Meta:
        verbose_name = u'article'
        verbose_name_plural = verbose_name
    def __unicode__(self):
        return self.title

class Site_image(models.Model):
    name = models.CharField(u'image name', max_length=100)
    link = models.URLField(u'link')
    image = models.ImageField(u'image')
    class Meta:
        verbose_name = u'site image'
        verbose_name_plural = verbose_name
    def __unicode__(self):
        return self.name


class Product_type(models.Model):
    name = models.CharField('type name', max_length=100)
    class Meta:
        verbose_name = 'All product type'
        verbose_name_plural = verbose_name
    def __unicode__(self):
        return self.name


class Product(models.Model):
    kind = models.ForeignKey(Product_type)
    name = models.CharField(u'product name', max_length=100)
    cover = models.ImageField(u'product_image')
    code = models.CharField(u'product code', max_length=100)
    power = models.CharField(u'power', max_length=100)
    electric_data = models.CharField(u'electric data', max_length=100)
    beam_angle = models.CharField(u'beam angle', max_length=100)
    color_temperature = models.CharField(u'color temperature', max_length=100)
    ip_class = models.CharField(u'ip class', max_length=100)
    fixture_size = models.CharField(u'fixture size', max_length=100)
    cutout_size = models.CharField(u'cutout size', max_length=100)
    led_source = models.CharField(u'led source', max_length=100)
    fixture_material = models.CharField(u'fixture material', max_length=100)
    finish = models.CharField(u'finish', max_length=100)
    more_info = UEditorField(u'more info', max_length=200000)
    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = verbose_name
    def __unicode__(self):
        return self.name

class Slide(models.Model):
    name = models.CharField(u'slide name', max_length = 100)
    img = models.ForeignKey(Site_image)
    class Meta:
        verbose_name = "Slide"
        verbose_name_plural = verbose_name
    def __unicode__(self):
        return self.name
