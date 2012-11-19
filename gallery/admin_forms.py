import os
import zipfile
from StringIO import StringIO
from tempfile import mkdtemp

from django import forms
from django.core.files import File

from gallery.models import GalleryImage
from gallery.fields import FileMultiField


class BulkImageUploadForm(forms.Form):

    files_label = '''Your browser may allow you to select multiple files at
once. Try holding down the CTRL key when you select files.'''

    files = FileMultiField(max_size=1000000, help_text=files_label, required=False)

    def __init__(self, *args, **kwargs):
        self.gallery = kwargs.pop('gallery')
        super(BulkImageUploadForm, self).__init__(*args, **kwargs)

    def save(self, commit=True):
        images = []
        if self.cleaned_data['files']:
            for item in self.cleaned_data['files']:
                item.seek(0)
                to_add = []

                # Zip file?
                itemfp = StringIO(item.read())
                item.seek(0)
                try:
                    zfp = zipfile.ZipFile(itemfp, 'r')
                except:
                    # zipfile does not raise a specific exception
                    to_add.append(item)
                else:    
                    if not zfp.testzip():
                        # Running into issues using streams, so use temp files
                        tmpdir = mkdtemp()
                        for filename in sorted(zfp.namelist()):
                            tmpfile = os.path.join(tmpdir, filename)
                            data = zfp.read(filename)
                            fp = open(tmpfile, 'wb')
                            fp.write(data)
                            fp.close()
                            afile = File(open(tmpfile), 'rb')
                            afile.name = filename
                            to_add.append(afile)
                    else:                    
                        to_add.append(item)

                for afile in to_add:                    
                    obj = GalleryImage(title=afile.name, gallery=self.gallery)
                    obj.image = afile
                    obj.save()
                    obj.sites = list(self.gallery.sites.all())
                    obj.save()
                    images.append(obj)

        return images

