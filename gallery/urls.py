from django.conf.urls import patterns, url

from jmbo.views import ObjectDetail


urlpatterns = patterns(
    '',
    url(r'^(?P<slug>[\w-]+)/$', ObjectDetail.as_view(), name='gallery_object_detail'),
    url(r'^video/(?P<slug>[\w-]+)/$', ObjectDetail.as_view(), name='videoembed_object_detail'),
    url(r'^image/(?P<slug>[\w-]+)/$', ObjectDetail.as_view(), name='galleryimage_object_detail'),
)
