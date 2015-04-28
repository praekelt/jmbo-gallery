from django.conf.urls import patterns, url


urlpatterns = patterns(
    '',

    url(
        r'^gallery/gallery/(?P<gallery_id>\d+)/bulk-image-upload/$',
        'gallery.admin_views.bulk_image_upload',
        {},
        name='gallery-bulk-image-upload'
    )

)
