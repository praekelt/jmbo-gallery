from django.contrib import admin
from django.core.urlresolvers import reverse, NoReverseMatch

from jmbo.admin import ModelBaseAdmin
from preferences.admin import PreferencesAdmin

from gallery.models import Gallery, GalleryImage, VideoEmbed, VideoFile, \
    GalleryPreferences


class GalleryAdmin(ModelBaseAdmin):

    def _actions(self, obj):
        result = super(GalleryAdmin, self)._actions(obj)
        try:
            url = reverse('gallery-bulk-image-upload', args=[obj.id])
            return result + '<a href="%s">Bulk upload</a>' % url
        except NoReverseMatch:
            return result + "Bulk upload - add gallery admin_urls to settings, eg. <code>(r'^admin/', include('gallery.admin_urls'))</code>"
    _actions.short_description = 'Actions'
    _actions.allow_tags = True


class GalleryImageAdmin(ModelBaseAdmin):
    list_display = ModelBaseAdmin.list_display + ('gallery',)
    list_filter = ModelBaseAdmin.list_filter + ('gallery',)


class GalleryPreferencesAdmin(PreferencesAdmin):
    pass


admin.site.register(Gallery, GalleryAdmin)
admin.site.register(GalleryImage, GalleryImageAdmin)
admin.site.register(VideoEmbed, ModelBaseAdmin)
admin.site.register(VideoFile, ModelBaseAdmin)
admin.site.register(GalleryPreferences, GalleryPreferencesAdmin)
