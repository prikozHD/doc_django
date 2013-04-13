from django.conf.urls import patterns, include, url

from settings import MEDIA_ROOT
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^products/$', 'app.views.products',  {'main_category':''},name = 'products'),
    url(r'^product/(?P<slug>[a-zA-Z0-9_-]*)/$', 'app.views.get_product', name = 'product'),

    url(r'^admin_tools/', include('admin_tools.urls')),
    url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += patterns('',
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root':MEDIA_ROOT})
)


