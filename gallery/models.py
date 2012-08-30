import os
import re
import urllib2
from tempfile import mkdtemp

from django.core.urlresolvers import reverse
from django.db import models
from django.core.files import File

from photologue.models import Image
from jmbo.models import ModelBase

from preferences import Preferences

from PIL import Image, ImageDraw


class Gallery(ModelBase):

    class Meta:
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

    class Meta:
        verbose_name = "Gallery image"
        verbose_name_plural = "Gallery images"


class VideoEmbed(GalleryItem):
    embed = models.TextField(
        help_text="""Embedding markup as supplied by Youtube.""")

    class Meta:
        verbose_name = "Video embed"
        verbose_name_plural = "Video embeds"

    @property
    def youtube_id(self):
        """Extract and return Youtube video id"""
        m = re.search(r'/embed/([A-Za-z0-9\-=_]*)"', self.embed)
        if m:
            return m.group(1)
        return ''
    
    def save(self, *args, **kwargs):
        """Automatically set image"""
        url = "http://img.youtube.com/vi/%s/0.jpg" % self.youtube_id
        try:
            response = urllib2.urlopen(url)
        except Exception, e:
            # Blindly catch exceptions
            pass
        else:            
            # Jump through filesystem hoop to please photologue
            filename = self.youtube_id + '.jpg'
            filepath = os.path.join(mkdtemp(), filename)
            fp = open(filepath, 'wb')
            try:
                fp.write(response.read())
            finally:
                fp.close()
            image = File(open(filepath, 'rb'))
            image.name = filename
            self.image = image
            pref = GalleryPreference.objects.all()
            if pref:
                pil_image = Image.open(image)
                image_overlay = Image.open(pref.video_play_image.url)
                # downsize image_overlay if it is larger than image
                w1, h1 = pil_image.size
                w2, h2 = image_overlay.size
                if w2 > w1 or h2 > h1:
                    ratio1 = w1 / float(h1)
                    ratio2 = w2 / float(h2)
                    if ratio1 > ratio2:
                        resize_fract = h1 / float(h2)
                    else:
                        resize_fract = w1 / float(w2)
                    
                    image_overlay.resize(w2 * resize_fract, h2 * resize_fract, Image.ANTIALIAS)
                
                pil_image.paste(image_overlay, ((w1 - w2) / 2.0, (h1 - h2) / 2.0))
                pil_image.save("%s_b%s" % os.path.splitext(self.image.url))
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
    
    
