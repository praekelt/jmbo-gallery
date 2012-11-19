from django import forms

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
                obj = GalleryImage(title=item.name, gallery=self.gallery)
                obj.image = item
                obj.save()
                obj.sites = list(self.gallery.sites.all())
                obj.save()
                images.append(obj)

        return images

