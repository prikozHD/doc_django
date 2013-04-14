#encoding:utf-8
from django.db import models
import datetime
from django.utils.encoding import iri_to_uri

class MainCategory(models.Model):
    main_category_name = models.CharField(max_length=200, verbose_name=u"Категория")

    def __unicode__(self):
        return self.main_category_name

    @models.permalink
    def get_absolute_url(self):
        url = iri_to_uri(self.main_category_name)
        return ('main_category', (), {'main_category_name':url})

    class Meta:
        verbose_name = u"Категория"
        verbose_name_plural = u"Категории"


class SubCategory(models.Model):
    name = models.CharField(max_length=200, verbose_name=u"под категория")
    main_category = models.ForeignKey(MainCategory)


    def __unicode__(self):
        return "%s %s " % (self.main_category.main_category_name, self.name, )

    class Meta:
        verbose_name = u"Под категория"
        verbose_name_plural = u"Под категории"



class Author(models.Model):
    first_name = models.CharField(max_length=100, default = '', blank=True, verbose_name=u"Имя")
    last_name = models.CharField(max_length=100, default = '', blank=True, verbose_name=u"Фамилия")
    email = models.EmailField(max_length=200, default = '', blank=True, verbose_name=u"E-mail")
    about_author = models.TextField( verbose_name=u"Про автора" )

    def __unicode__(self):
        return u"%s %s %s" % (self.first_name, self.last_name, self.email, )

class Products(models.Model):
    IN_STOCK_CHOICES = (
        (1, u"Да"),
        (1, u"Нет")
    )

    title = models.CharField(max_length=200, verbose_name=u"Название книги")
    slug = models.SlugField(max_length=200, verbose_name=u"URL книги")
    description = models.TextField(verbose_name=u"Описание для книги")
    pub_date = models.DateField(blank=True, null=True, verbose_name=u"Дата публикации")
    num_pages = models.IntegerField(default=0, null=True,verbose_name=u"Количество страниц")
    product_count = models.IntegerField(default=0, verbose_name=u"Количество екземпляров на складе")
    article = models.CharField(max_length=200,default='',verbose_name=u"Артикул")
    price = models.DecimalField(default=0.00, max_length=8, max_digits=6, decimal_places=2,verbose_name=u"Цена")
    discount = models.IntegerField(default=0.0, blank=True,verbose_name=u"Скидка")
    discount_from_money = models.FloatField(default=0.0, blank=True,verbose_name=u"Скидка в грн")
    discount_price = models.FloatField(default=0.0,verbose_name=u"Цена с учетом скидки")
    subsategory = models.ForeignKey(SubCategory, verbose_name=u"Под категория")
    prev_img = models.ImageField(upload_to=u'prev_img_book', blank=True, null=True,verbose_name=u"Обложка книги")
    in_stock = models.BooleanField(default=1, choices=IN_STOCK_CHOICES, verbose_name=u"В наличии")
    isbn = models.CharField(default='', blank=True, max_length=200,verbose_name=u"ISBN")
    authors = models.ManyToManyField(Author,verbose_name=u"Автори книги")


    def display_admin_prev_img(self):
        return "<img src = '%s' />" % self.prev_img.url
    display_admin_prev_img.allow_tags = True
    display_admin_prev_img.short_description = u"Обложка книги"

    def display_admin_stock(self):
        return self.in_stock
    display_admin_stock.boolean = True
    display_admin_stock.allow_tags = True
    display_admin_stock.short_description = u"В наличии"

    def display_admin_author(self):

        return "%s" % '; '.join([' '.join([author.first_name, author.last_name]) for author in self.authors.all()])




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

        if self.discount > 0.0:
            self.discount_price  = self.price - (self.price * self.discount)/100 if self.discount > 0.0 else self.price
            self.discount_from_money = (self.price * self.discount)/100 if self.discount > 0.0 else 0.0
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








