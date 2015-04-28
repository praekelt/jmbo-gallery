from django.test import TestCase as BaseTestCase
from django.test.client import Client as BaseClient, RequestFactory
from django.contrib.auth.models import User

from gallery.models import Gallery, GalleryImage


class TestCase(BaseTestCase):

    @classmethod
    def setUpClass(cls):
        cls.request = RequestFactory()
        cls.client = BaseClient()

        # Editor
        cls.editor, dc = User.objects.get_or_create(
            username='editor',
            email='editor@test.com',
        )
        cls.editor.set_password("password")
        cls.editor.save()

        # Gallery
        obj = Gallery.objects.create(
            title='Gallery',
            content='This is gallery content',
            owner=cls.editor, state='published',
        )
        obj.sites = [1]
        obj.save()
        cls.gallery = obj

        # Gallery image
        obj = GalleryImage.objects.create(
            title='Gallery Image', gallery=cls.gallery,
            owner=cls.editor, state='published',
        )
        obj.sites = [1]
        obj.save()
        cls.gallery_image = obj

    def test_gallery_detail(self):
        response = self.client.get(self.gallery.get_absolute_url())
        self.failUnless('This is gallery content' in response.content)
        self.failUnless('Gallery Image' in response.content)

    def test_galleryimage_detail(self):
        response = self.client.get(self.gallery_image.get_absolute_url())
        self.failUnless('Gallery Image' in response.content)
