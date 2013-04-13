#encoding:utf-8
from django.contrib import admin
from models import *

class AdminProducts(admin.ModelAdmin):
    prepopulated_fields = {'slug':('title', )}

admin.site.register(Products, AdminProducts)

admin.site.register(SubCategory)
admin.site.register(Author)
admin.site.register(MainCategory)




