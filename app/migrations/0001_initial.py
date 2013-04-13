# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'MainCategory'
        db.create_table('app_maincategory', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('main_category_name', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal('app', ['MainCategory'])

        # Adding model 'SubCategory'
        db.create_table('app_subcategory', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('main_category', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['app.MainCategory'])),
        ))
        db.send_create_signal('app', ['SubCategory'])

        # Adding model 'Author'
        db.create_table('app_author', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('first_name', self.gf('django.db.models.fields.CharField')(default='', max_length=100, blank=True)),
            ('last_name', self.gf('django.db.models.fields.CharField')(default='', max_length=100, blank=True)),
            ('email', self.gf('django.db.models.fields.EmailField')(default='', max_length=200, blank=True)),
            ('about_author', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('app', ['Author'])

        # Adding model 'Products'
        db.create_table('app_products', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=200)),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('pub_date', self.gf('django.db.models.fields.DateField')(auto_now=True, blank=True)),
            ('num_pages', self.gf('django.db.models.fields.IntegerField')(default=0, null=True)),
            ('product_count', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('article', self.gf('django.db.models.fields.CharField')(default='', max_length=200)),
            ('price', self.gf('django.db.models.fields.DecimalField')(default=0.0, max_length=8, max_digits=6, decimal_places=2)),
            ('subsategory', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['app.SubCategory'])),
            ('prev_img', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True)),
            ('in_stock', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('isbn', self.gf('django.db.models.fields.CharField')(default='', max_length=200, blank=True)),
        ))
        db.send_create_signal('app', ['Products'])

        # Adding M2M table for field authors on 'Products'
        db.create_table('app_products_authors', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('products', models.ForeignKey(orm['app.products'], null=False)),
            ('author', models.ForeignKey(orm['app.author'], null=False))
        ))
        db.create_unique('app_products_authors', ['products_id', 'author_id'])


    def backwards(self, orm):
        # Deleting model 'MainCategory'
        db.delete_table('app_maincategory')

        # Deleting model 'SubCategory'
        db.delete_table('app_subcategory')

        # Deleting model 'Author'
        db.delete_table('app_author')

        # Deleting model 'Products'
        db.delete_table('app_products')

        # Removing M2M table for field authors on 'Products'
        db.delete_table('app_products_authors')


    models = {
        'app.author': {
            'Meta': {'object_name': 'Author'},
            'about_author': ('django.db.models.fields.TextField', [], {}),
            'email': ('django.db.models.fields.EmailField', [], {'default': "''", 'max_length': '200', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '100', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '100', 'blank': 'True'})
        },
        'app.maincategory': {
            'Meta': {'object_name': 'MainCategory'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'main_category_name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'app.products': {
            'Meta': {'ordering': "['-id']", 'object_name': 'Products'},
            'article': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '200'}),
            'authors': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['app.Author']", 'symmetrical': 'False'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'in_stock': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'isbn': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '200', 'blank': 'True'}),
            'num_pages': ('django.db.models.fields.IntegerField', [], {'default': '0', 'null': 'True'}),
            'prev_img': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'price': ('django.db.models.fields.DecimalField', [], {'default': '0.0', 'max_length': '8', 'max_digits': '6', 'decimal_places': '2'}),
            'product_count': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'pub_date': ('django.db.models.fields.DateField', [], {'auto_now': 'True', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '200'}),
            'subsategory': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['app.SubCategory']"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'app.subcategory': {
            'Meta': {'object_name': 'SubCategory'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'main_category': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['app.MainCategory']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['app']