from django.core.urlresolvers import reverse
from django.db import models

from jmbo.models import ModelBase

class Gallery(ModelBase):
    class Meta():
        verbose_name = "Gallery"
        verbose_name_plural = "Galleries"
    
    def item_count(self):
        return GalleryItem.permitted.filter(gallery=self).count()    

    def __unicode__(self):
        return self.title

    def get_items(self):
        return GalleryItem.permitted.filter(gallery=self).order_by('created')

    
class GalleryItem(ModelBase):
    gallery = models.ForeignKey(
        'gallery.Gallery',
    )

class GalleryImage(GalleryItem):
    class Meta():
        verbose_name = "Gallery image"
        verbose_name_plural = "Gallery images"

class VideoEmbed(GalleryItem):
    embed = models.TextField()
    class Meta():
        verbose_name = "Video embed"
        verbose_name_plural = "Video embeds"

class VideoFile(GalleryItem):
    file = models.FileField(upload_to='content/videofile')
    class Meta():
        verbose_name = "Video file"
        verbose_name_plural = "Video files"
