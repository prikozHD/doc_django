# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Products.price'
        db.add_column('app_products', 'price',
                      self.gf('django.db.models.fields.DecimalField')(default=0.0, max_length=8, max_digits=6, decimal_places=2),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Products.price'
        db.delete_column('app_products', 'price')


    models = {
        'app.category': {
            'Meta': {'object_name': 'Category'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'app.products': {
            'Meta': {'ordering': "['-id']", 'object_name': 'Products'},
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['app.Category']"}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'price': ('django.db.models.fields.DecimalField', [], {'default': '0.0', 'max_length': '8', 'max_digits': '6', 'decimal_places': '2'}),
            'product_count': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'pub_date': ('django.db.models.fields.DateField', [], {'auto_now': 'True', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '200'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['app']