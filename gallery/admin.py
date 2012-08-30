from django.contrib import admin

from jmbo.admin import ModelBaseAdmin
from preferences.admin import PreferencesAdmin

from gallery.models import Gallery, GalleryImage, VideoEmbed, VideoFile, \
    GalleryPreferences


class GalleryImageAdmin(ModelBaseAdmin):
    list_display = ModelBaseAdmin.list_display + ('gallery',)
    list_filter = ModelBaseAdmin.list_filter + ('gallery',)


class GalleryPreferencesAdmin(PreferencesAdmin):
    pass


admin.site.register(Gallery, ModelBaseAdmin)
admin.site.register(GalleryImage, GalleryImageAdmin)
admin.site.register(VideoEmbed, ModelBaseAdmin)
admin.site.register(VideoFile, ModelBaseAdmin)
admin.site.register(GalleryPreferences, GalleryPreferencesAdmin)
