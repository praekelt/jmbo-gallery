import os

from django.core.urlresolvers import reverse
from django.db import models

from jmbo.models import ModelBase

from preferences import Preferences

from PIL import Image, ImageDraw


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
 
    def save(self, *args, **kwargs):
        pref = GalleryPreference.objects.all()
        if pref:
            if self.image:
                image = Image.open(self.image.url)
                image_overlay = Image.open(pref.video_play_image.url)
                # downsize image_overlay if it is larger than image
                w1, h1 = image.size
                w2, h2 = image_overlay.size
                if w2 > w1 or h2 > h1:
                    ratio1 = w1 / float(h1)
                    ratio2 = w2 / float(h2)
                    if ratio1 > ratio2:
                        resize_fract = h1 / float(h2)
                    else:
                        resize_fract = w1 / float(w2)
                    
                    image_overlay.resize(w2 * resize_fract, h2 * resize_fract, Image.ANTIALIAS)
                
                image.paste(image_overlay, ((w1 - w2) / 2.0, (h1 - h2) / 2.0))
                image.save("%s_b%s" % os.path.splitext(self.image.url))
                self.image = "%s_b%s" % os.path.splitext(self.image.name)
                
        else:
            raise GalleryPreference.DoesNotExist("The video play overlay image is required.")

        super(VideoEmbed, self).save(*args, **kwargs)

class VideoFile(GalleryItem):
    file = models.FileField(upload_to='content/videofile')
    class Meta():
        verbose_name = "Video file"
        verbose_name_plural = "Video files"


class GalleryPreferences(Preferences):
    __module__ = 'preferences.models'

    video_play_image = models.ImageField(
        upload_to="preferences",
        help_text="The play button image that is overlaid on a video image"
    )
    
    
