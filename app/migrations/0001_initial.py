# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Products'
        db.create_table('app_products', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=200)),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('pub_date', self.gf('django.db.models.fields.DateField')(auto_now=True, blank=True)),
            ('product_count', self.gf('django.db.models.fields.IntegerField')(default=0)),
        ))
        db.send_create_signal('app', ['Products'])

        # Adding model 'Category'
        db.create_table('app_category', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('products', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['app.Products'])),
        ))
        db.send_create_signal('app', ['Category'])


    def backwards(self, orm):
        # Deleting model 'Products'
        db.delete_table('app_products')

        # Deleting model 'Category'
        db.delete_table('app_category')


    models = {
        'app.category': {
            'Meta': {'object_name': 'Category'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'products': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['app.Products']"})
        },
        'app.products': {
            'Meta': {'ordering': "['-id']", 'object_name': 'Products'},
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'product_count': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'pub_date': ('django.db.models.fields.DateField', [], {'auto_now': 'True', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '200'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['app']