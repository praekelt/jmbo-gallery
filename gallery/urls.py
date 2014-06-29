from django.conf.urls.defaults import patterns, url


urlpatterns = patterns(
    '',
    url(r'^(?P<slug>[\w-]+)/$', 'jmbo.views.object_detail', name='gallery_object_detail'),
    url(r'^video/(?P<slug>[\w-]+)/$', 'jmbo.views.object_detail', name='videoembed_object_detail'),
    url(r'^image/(?P<slug>[\w-]+)/$', 'jmbo.views.object_detail', name='galleryimage_object_detail'),
)
