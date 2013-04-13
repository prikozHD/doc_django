#encoding:utf-8
from django.db import models
import datetime

class Category(models.Model):
    name = models.CharField(max_length=200)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = u"Категория"
        verbose_name_plural = u"Категории"

class Author(models.Model):
    first_name = models.CharField(max_length=100, default = '', blank=True)
    last_name = models.CharField(max_length=100, default = '', blank=True)
    email = models.EmailField(max_length=200, default = '', blank=True)

class Products(models.Model):
    IN_STOCK_CHOICES = (
        (1, u"Да"),
        (1, u"Нет")
    )


    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)
    description = models.TextField()
    pub_date = models.DateField(auto_now=True)
    num_pages = models.IntegerField(default=0, null=True)
    product_count = models.IntegerField(default=0)
    article = models.CharField(max_length=200,default='')
    price = models.DecimalField(default=0.00, max_length=8, max_digits=6, decimal_places=2)
    category = models.ForeignKey(Category)
    prev_img = models.ImageField(upload_to=u'prev_img_book', blank=True, null=True)
    in_stock = models.BooleanField(default=1, choices=IN_STOCK_CHOICES)
    isbn = models.CharField(default='', blank=True, max_length=200)


    def save(self, *args, **kwargs):
        if(self.prev_img):
            from PIL import Image
            from django.core.files.base import ContentFile
            from StringIO import StringIO
            im = Image.open(self.prev_img)
            im.thumbnail((168,240), Image.ANTIALIAS)
            sIO = StringIO()
            im.save(sIO, 'PNG')
            cnt = ContentFile(sIO.getvalue())
            self.prev_img.save(self.prev_img.name, cnt, save=False)

        super(Products, self).save(*args, **kwargs)






    def __unicode__(self):
        return self.title

    @models.permalink
    def get_absolute_url(self):
        return ('product', (), {'slug' : self.slug })

    class Meta:
        ordering = ['-id']
        get_latest_by = 'pub_date'
        verbose_name = u"Продукт"
        verbose_name_plural = u"Продукты"







