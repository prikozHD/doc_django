#encoding:utf-8
from django.contrib import admin
from models import *

class AdminProducts(admin.ModelAdmin):
    list_display = ('title','display_admin_prev_img', 'price', 'pub_date', 'num_pages', 'product_count', 'isbn', 'display_admin_stock','display_admin_author')
    list_filter = ('title','price',)
    search_fields = ('title',)
    date_hierarchy =  'pub_date'
    prepopulated_fields = {'slug':('title', )}

admin.site.register(Products, AdminProducts)

admin.site.register(SubCategory)
admin.site.register(Author)
admin.site.register(MainCategory)




