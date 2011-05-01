from django.conf.urls.defaults import *

urlpatterns = patterns('main_site.views',
    url(r'^product/$','index_product', name="index_product"),
    url(r'^service/$','index_service', name="index_service"),
    url(r'^about/$','index_about', name="index_about"),
    url(r'^contact/$','index_contact', name="index_contact"),
)
