from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.shortcuts import render_to_response, get_object_or_404
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib import messages

from gallery.models import Gallery
from gallery.admin_forms import BulkImageUploadForm


@staff_member_required
def bulk_image_upload(request, gallery_id):
    gallery = get_object_or_404(Gallery, id=gallery_id)
    if request.method == 'POST':
        form = BulkImageUploadForm(request.POST, request.FILES, gallery=gallery) 
        if form.is_valid():
            images = form.save()
            messages.success(
                request, 
                "Created %d images" % len(images), 
                fail_silently=True
            )
            if images:
                id__in = ','.join([str(image.id) for image in images])
                return HttpResponseRedirect(
                    '/admin/gallery/galleryimage/?id__in=%s' % id__in
                )
            else:
                return HttpResponseRedirect('/admin/gallery/galleryimage/')
    else:        
        form = BulkImageUploadForm(gallery=gallery)

    extra = dict(form=form)
    return render_to_response('admin/gallery/bulk_image_upload.html', extra, context_instance=RequestContext(request))

