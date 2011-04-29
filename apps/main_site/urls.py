from django.conf.urls.defaults import *

urlpatterns = patterns('main_site.views',
    url(r'^blog/$','index_blog', name="index_blog"),
)
